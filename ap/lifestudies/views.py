import datetime
import logging
import json
import threading
import time

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.core import serializers
from django.core.serializers import serialize
from django.db import transaction, IntegrityError
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.shortcuts import render
from django.db.models import Q

from .forms import NewSummaryForm, NewDisciplineForm, EditSummaryForm, HouseDisciplineForm
from .models import Discipline, Summary
from accounts.models import Trainee
from aputils.trainee_utils import trainee_from_user
from aputils.decorators import group_required
from attendance.utils import Period
from attendance.models import Roll
from leaveslips.models import *
from houses.models import House
from teams.models import Team
from terms.models import Term
from aputils.utils import timeit, timeit_inline, memoize


from rest_framework import viewsets
from .serializers import SummarySerializer
from itertools import chain

from ast import literal_eval

""" API Views Imports """
from rest_framework.decorators import permission_classes
from .permissions import IsOwner

logger = logging.getLogger(__name__)


class DisciplineListView(ListView):
  template_name = 'lifestudies/discipline_list.html'
  model = Discipline
  context_object_name = 'disciplines'

  def post(self, request, *args, **kwargs):
    """'approve' when an approve button is pressed 'delete' when a delete
    button is pressed 'attend_assign' when assgning discipline from
    AttendanceAssign"""

    if 'approve' in request.POST:
      for value in request.POST.getlist('selection'):
        Discipline.objects.get(pk=value).approve_all_summary()
      messages.success(request, "Checked Discipline(s) Approved!")
    if 'delete' in request.POST:
      for value in request.POST.getlist('selection'):
        Discipline.objects.get(pk=value).delete()
      messages.success(request, "Checked Discipline(s) Deleted!")
    if 'trainee_pk' in request.POST:
      trainee_pk = request.POST.getlist('trainee_pk')
      ls_count = request.POST.getlist('ls_count')
      period = int(request.POST.get('period'))
      for idx, pk in enumerate(trainee_pk):
        discipline = Discipline(
          infraction='AT',
          quantity=ls_count[idx],
          due=Period(Term.current_term()).start(period+1) + timedelta(weeks=1), #Due on the second Monday of the next period
          offense='MO',
          trainee=Trainee.objects.get(pk=pk))
        try:
          discipline.save()
        except IntegrityError:
          logger.error('Abort trasanction error')
          transaction.rollback()
      messages.success(request, "Discipline Assigned According to Attendance!")
    return self.get(request, *args, **kwargs)

  # profile is the user that's currently logged in
  def get_context_data(self, **kwargs):
    context = super(DisciplineListView, self).get_context_data(**kwargs)
    try:
      context['current_period'] = Period(Term.current_term()).period_of_date(datetime.now().date())
    except ValueError:
      # ValueError thrown if current date is not in term (interim)
      # return last period of previous period
      context['current_period'] = Period.last_period()
    return context


class DisciplineReportView(ListView):
  template_name = 'lifestudies/discipline_report.html'
  model = Discipline
  context_object_name = 'disciplines'

  # this function is called whenever 'post'
  def post(self, request, *args, **kwargs):
    # turning the 'post' into a 'get'
    return self.get(request, *args, **kwargs)

  # profile is the user that's currently logged in
  def get_context_data(self, **kwargs):
    context = super(DisciplineReportView, self).get_context_data(**kwargs)
    context['trainees'] = Trainee.objects.all()
    context['teams'] = Team.objects.all()
    context['houses'] = House.objects.all()
    if self.request.method == 'POST':
      for discipline in context['object_list']:
        if discipline.pk in self.request.POST:
          discipline.approve_all_summary
    return context


class DisciplineCreateView(SuccessMessageMixin, CreateView):
  model = Discipline
  form_class = NewDisciplineForm
  success_url = reverse_lazy('lifestudies:discipline_list')
  success_message = "Discipline Assigned to Single Trainee Successfully!"


def post_summary(summary, request):
  if 'fellowship' in request.POST:
    summary.set_fellowship()
    messages.success(request, "Marked for fellowship")
  if 'unfellowship' in request.POST:
    summary.remove_fellowship()
    messages.success(request, "Remove mark for fellowship")
  if 'approve' in request.POST:
    summary.approve()
    messages.success(request, "Summary Approved!")
  if 'unapprove' in request.POST:
    summary.unapprove()
    messages.success(request, "Summary Un-Approved!")


class DisciplineDetailView(DetailView):
  model = Discipline
  context_object_name = 'discipline'
  template_name = 'lifestudies/discipline_detail.html'

  def post(self, request, *args, **kwargs):
    if 'summary_pk' in request.POST:
      approve_summary_pk = int(request.POST['summary_pk'])
      summary = Summary.objects.get(pk=approve_summary_pk)
      post_summary(summary, request)
    if 'hard_copy' in request.POST:
      self.get_object().summary_set.create(
          content='approved hard copy summary',
          chapter=0,
          hard_copy=True,
          approved=True
      )
      messages.success(request, "Hard Copy Submission Created!")
    if 'increase_penalty' in request.POST:
      self.get_object().increase_penalty()
      messages.success(request, "Increased Summary by 1")
    return HttpResponseRedirect(reverse_lazy('lifestudies:discipline_list'))


class SummaryCreateView(SuccessMessageMixin, CreateView):
  model = Summary
  form_class = NewSummaryForm
  success_url = reverse_lazy('lifestudies:discipline_list')
  success_message = "Life-study Summary Created Successfully!"
  template_name = 'lifestudies/summary_form.html'

  def get_context_data(self, **kwargs):
    context = super(SummaryCreateView, self).get_context_data(**kwargs)
    return context

  def get_form(self, form_class=NewSummaryForm):
    """
    Returns an instance of the form to be used in this view.
    """
    kargs = self.get_form_kwargs()
    kargs['trainee'] = trainee_from_user(self.request.user)

    return form_class(**kargs)

  def form_valid(self, form):
    summary = form.save(commit=False)
    # Check if minimum words are met
    if form.is_valid:
      summary.discipline = Discipline.objects.get(pk=self.kwargs['pk'])
      summary.date_submitted = datetime.datetime.now()
      summary.save()
    return super(SummaryCreateView, self).form_valid(form)


class SummaryApproveView(DetailView):
  """this is the view that TA will click into when viewing a summary and
  approving it"""
  model = Summary
  context_object_name = 'summary'
  template_name = 'lifestudies/summary_approve.html'

  def get_context_data(self, **kwargs):
    # get curretn id, self.object
    ctx = super(SummaryApproveView, self).get_context_data(**kwargs)
    # context['next'] = # calc here
    print self.args, self.request, self.kwargs['pk']

    nxt = self.get_object().next()
    prev = self.get_object().prev()

    ctx['next_summary'] = nxt.id if nxt else -1
    ctx['prev_summary'] = prev.id if prev else -1
    ctx['summary_wc'] = len(self.get_object().content.split())

    return ctx

  def post(self, request, *args, **kwargs):
    summary = self.get_object()
    post_summary(summary, request)
    return HttpResponseRedirect(reverse_lazy('lifestudies:discipline_list'))


class SummaryUpdateView(SuccessMessageMixin, UpdateView):
  """this is the view that trainee click into in order to update the
  content of the summary"""
  model = Summary
  context_object_name = 'summary'
  template_name = 'lifestudies/summary_detail.html'
  form_class = EditSummaryForm
  success_url = reverse_lazy('lifestudies:discipline_list')
  success_message = "Summary Updated Successfully!"

  def get_context_data(self, **kwargs):
    context = super(SummaryUpdateView, self).get_context_data(**kwargs)
    context['profile'] = self.request.user
    return context


class CreateHouseDiscipline(TemplateView):
  template_name = 'lifestudies/discipline_house.html'

  def get_context_data(self, **kwargs):
    context = super(CreateHouseDiscipline, self).get_context_data(**kwargs)
    context['form'] = HouseDisciplineForm()
    return context

  def post(self, request, *args, **kwargs):
    """this manually creates Disciplines for each house member"""
    if request.method == 'POST':
      form = HouseDisciplineForm(request.POST)
      if form.is_valid():
        house = House.objects.get(id=request.POST['House'])
        listTrainee = Trainee.objects.filter(house=house)
        for trainee in listTrainee:
          discipline = Discipline(
            infraction=form.cleaned_data['infraction'],
            quantity=form.cleaned_data['quantity'],
            due=form.cleaned_data['due'],
            offense=form.cleaned_data['offense'],
            note=form.cleaned_data['note'],
            trainee=trainee)
          try:
            discipline.save()
          except IntegrityError:
            transaction.rollback()
        messages.success(request, "Disciplines Assigned to House!")
        return HttpResponseRedirect(reverse_lazy('lifestudies:discipline_list'))
    else:
      form = HouseDisciplineForm()
    return HttpResponseRedirect(reverse_lazy('lifestudies:discipline_list'))


class AttendanceAssign(ListView):
  """this view mainly displays trainees, their roll status, and the number
   of summary they are to be assigned. The actual assigning is done by
  DisciplineListView"""
  model = Trainee
  template_name = 'lifestudies/attendance_assign.html'
  context_object_name = 'trainees'

  def get_context_data(self, **kwargs):
    """this adds outstanding_trainees, a dictionary
    {trainee : num_summary} for the template to display the trainees who
    need will have outstanding summaries"""
    context = super(AttendanceAssign, self).get_context_data(**kwargs)
    period = int(self.kwargs['period'])
    context['period'] = period
    p = Period(Term.current_term())
    context['start_date'] = p.start(period)
    context['end_date'] = p.end(period)
    return context

  
  def post(self, request, *args, **kwargs):
    self.object_list = Trainee.objects.all()
    context = super(AttendanceAssign, self).get_context_data(*args, **kwargs) 

    """Preview button was pressed"""
    if 'preview_attendance_assign' in request.POST:
    #if 'select_period' in request.body:
      #body_unicode = request.body.decode('utf-8')
      #body = json.loads(body_unicode)
      #period = int(body['select_period'])  

      period = int(request.POST['select_period'])
      context['period'] = period
      p = Period(Term.current_term())
      start_date = p.start(period)
      end_date = p.end(period)
      context['start_date'] = start_date
      context['end_date'] = end_date
      context['preview_return'] = 1
      #outstanding_trainees = list()
      context['outstanding_trainees'] = list()

      '''FILTERING OUT TRAINEES BASED ON INDIVIDUAL LEAVESLIPS'''
      rolls = Roll.objects.all()
      rolls = rolls.filter(date__gte=start_date, date__lte=end_date)
      #gs = GroupSlip.objects.all()
      t = timeit_inline("summary calculation")
      t.start()
      for trainee in Trainee.objects.all():
        print trainee
        #num_summary += trainee.calculate_summary(period)
        # unexcused absence = rolls for trainee that do not have a leaveslip attached and are marked absent 
        # + rolls for trainee that have an individual leaveslip attached, but are unapproved and are marked absent
        a_rolls = rolls.filter(trainee=trainee, status='A')
        uea = a_rolls.filter(leaveslips=None).count() + a_rolls.filter(~Q(leaveslips__status='A')).count()

        t_rolls = rolls.filter(trainee=trainee, status__in=['T', 'U', 'L'])
        uet = t_rolls.filter(leaveslips=None).count() + t_rolls.filter(~Q(leaveslips__status='A')).count() 

        if uea > 1 or uet > 4:
          num_summary = 0
          num_summary += trainee.calculate_summary(period)
          if num_summary > 0:
            context['outstanding_trainees'].append((trainee, num_summary))

        '''FAILED APPROACH: PROCESSING GROUP SLIP ONE BY ONE, CHECKING IF DISCIPLINE SHOULD BE ASSIGNED AFTER EACH GROUP SLIP 
        if uea > 1 or uet > 4:
          for slip in gs.filter(status='A', trainees=trainee):
            uea_rolls = list(chain(a_rolls.filter(leaveslips=None), a_rolls.filter(~Q(leaveslips__status='A'))))
            if uea > 1:
              for uea_roll in uea_rolls:
                roll_start = datetime.combine(uea_roll.date, uea_roll.event.start)
                roll_end = datetime.combine(uea_roll.date, uea_roll.event.end)
                #Get roll date + roll's event start and end, see if it is within group slip start and end 
                if (slip.start <= roll_start <= slip.end) or (slip.start <= roll_end <= slip.end):
                  uea-=1
                  if uea < 2:
                    break
            if uet > 4:
              uet_rolls = list(chain(t_rolls.filter(leaveslips=None), t_rolls.filter(~Q(leaveslips__status='A'))))
              for uet_roll in uet_rolls:
                roll_start = datetime.combine(uet_roll.date, uet_roll.event.start)
                roll_end = datetime.combine(uet_roll.date, uet_roll.event.end)
                #Get roll date + roll's event start and end, see if it is within group slip start and end 
                if (slip.start <= roll_start <= slip.end) or (slip.start <= roll_end <= slip.end):
                  uet-=1
                  if uet < 5:
                    break
            if uea < 2 and uet < 5:
              has_summaries = True
              break
        if has_summaries:          
          num_A = uea
          num_T = uet
          num_summary = 0
          if num_A >= 2:
            num_summary += max(num_A, 0)
          if num_T >= 5:
            num_summary += max(num_T - 3, 0)
          context['outstanding_trainees'].append((trainee, num_summary))
        '''

      
      '''THREADING?'''
      # Create new threads
      # thread1 = myThread("Thread", 1)
      # thread2 = myThread("Thread", 2)

      # Start new Threads
      # thread1.start()
      # thread2.start()

      # thread1.join()
      # thread2.join()
      # print "Exiting the Program!!!"


            #Get approved group leaveslips for the trainee  
            # gs.filter(status='A', trainees=trainee)
            # #start_date = Period(Term.current_term()).start(period)
            # #gs = gs.filter(start__gte=start_date)
            # #gs = gs.values('start', 'end')
            # for slip in gs
            #   #Check if roll
            #   excused_timeframes.append({'start': slip['start'], 'end': slip['end']})
            #   for tf in excused_timeframes:
            #     if (tf['start'] <= start_dt <= tf['end']) or (tf['start'] <= end_dt <= tf['end']):

            # uea-=1
            # #if uea < 2
            #  break
            #group leaveslip has uea
            #drop uea by 1
            #if uea < 2
            #break
      t.end()

      # print outstanding_trainees
      # for outstanding_trianee in outstanding_trainees:
      #   context['outstanding_trainees'].outstanding_trainee.
      # results.update({'account': {'id': account.id, 'title': account.title}})
      # return JsonResponse({

      # })
      return render(request, 'lifestudies/attendance_assign.html', context)   
    return render(request, 'lifestudies/attendance_assign.html', context)

class myThread (threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name
        print_date(self.name, self.counter)
        print "Exiting " + self.name

def print_date(threadName, counter):
    datefields = []
    today = datetime.date.today()
    datefields.append(today)
    print "%s[%d]: %s" % ( threadName, counter, datefields[0] )


class MondayReportView(TemplateView):
  template_name = "lifestudies/monday_report.html"

  def get_context_data(self, **kwargs):
    context = super(MondayReportView, self).get_context_data(**kwargs)
    list_dis = [disc for disc in Discipline.objects.all() if disc.get_num_summary_due()]

    context['disciplines'] = list_dis
    context['date_today'] = datetime.date.today()
    return context

'''
@group_required(('training_assistant',), raise_exception=True)
def preview_attendance_assign(request):
    context = {}
    if request.method == "POST":
      context['preview_return'] = 1
      context['outstanding_trainees'] = {} 
      for trainee in Trainee.objects.all():
        print trainee
        num_summary = 0
        num_summary += trainee.calculate_summary(period)
        if num_summary > 0:
          context['outstanding_trainees'][trainee] = num_summary
    else:
      context['preview_return'] = 0
    return HttpResponse(
      json.dumps(context),
      content_type="application/json"
    )
'''

""" API Views """


@permission_classes((IsOwner, ))
class DisciplineSummariesViewSet(viewsets.ModelViewSet):
  queryset = Summary.objects.all()
  serializer_class = SummarySerializer

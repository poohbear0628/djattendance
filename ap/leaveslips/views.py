import django_filters

from itertools import chain
from datetime import datetime, timedelta

from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib import messages
from django.db.models import Q

from rest_framework import viewsets, filters

from .models import LeaveSlip, IndividualSlip, GroupSlip
from .forms import IndividualSlipForm, GroupSlipForm
from .serializers import IndividualSlipSerializer, IndividualSlipFilter, GroupSlipSerializer, GroupSlipFilter
from accounts.models import Trainee, TrainingAssistant
from terms.models import Term
from rest_framework_bulk import BulkModelViewSet

from aputils.trainee_utils import trainee_from_user
from aputils.groups_required_decorator import group_required
from braces.views import GroupRequiredMixin

class IndividualSlipUpdate(GroupRequiredMixin, generic.UpdateView):
  model = IndividualSlip
  group_required = ['administration']
  template_name = 'leaveslips/individual_update.html'
  form_class = IndividualSlipForm
  context_object_name = 'leaveslip'

  def get_context_data(self, **kwargs):
    ctx = super(IndividualSlipUpdate, self).get_context_data(**kwargs)
    leaveslip = self.get_object()
    periods = leaveslip.periods
    if len(periods) > 0:
      start_date = Term.current_term().startdate_of_period(periods[0])
      end_date = Term.current_term().enddate_of_period(periods[-1])
      ctx['events'] = leaveslip.trainee.events_in_date_range(start_date, end_date)
      ctx['start_date'] = start_date
      ctx['end_date'] = end_date + timedelta(1)
    return ctx

class GroupSlipUpdate(GroupRequiredMixin, generic.UpdateView):
  model = GroupSlip
  group_required = ['administration']
  template_name = 'leaveslips/group_update.html'
  form_class = GroupSlipForm
  context_object_name = 'leaveslip'

  def get_context_data(self, **kwargs):
    ctx = super(GroupSlipUpdate, self).get_context_data(**kwargs)
    leaveslip = self.get_object()
    periods = leaveslip.periods
    if len(periods) > 0:
      start_date = Term.current_term().startdate_of_period(periods[0])
      end_date = Term.current_term().enddate_of_period(periods[-1])
      ctx['events'] = leaveslip.trainee.groupevents_in_week_range(periods[0]*2, (periods[-1]*2)+1)
      ctx['start_date'] = start_date
      ctx['end_date'] = end_date
      ctx['today'] = leaveslip.start
    return ctx

# viewing the leave slips
class LeaveSlipList(generic.ListView):
  model = IndividualSlip, GroupSlip
  template_name = 'leaveslips/list.html'

  def get_queryset(self):
   individual=IndividualSlip.objects.filter(trainee=self.request.user.id).order_by('status')
   group=GroupSlip.objects.filter(trainee=self.request.user.id).order_by('status')  # if trainee is in a group leaveslip submitted by another user
   queryset= chain(individual,group)  # combines two querysets
   return queryset

class TALeaveSlipList(GroupRequiredMixin, generic.TemplateView):
  model = IndividualSlip, GroupSlip
  group_required = ['administration']
  template_name = 'leaveslips/ta_list.html'

  def post(self, request, *args, **kwargs):
    context = self.get_context_data()
    return super(TALeaveSlipList, self).render_to_response(context)

  def get_context_data(self, **kwargs):
    ctx = super(TALeaveSlipList, self).get_context_data(**kwargs)

    individual=IndividualSlip.objects.filter(status__in=['P', 'F', 'S']).order_by('submitted')
    group=GroupSlip.objects.filter(status__in=['P', 'F', 'S']).order_by('submitted')  # if trainee is in a group leaveslip submitted by another user

    if self.request.method == 'POST':
      selected_ta = int(self.request.POST.get('leaveslip_ta_list'))
    else:
      selected_ta = self.request.user.id

    ta = None
    if selected_ta > 0:
      ta = TrainingAssistant.objects.filter(pk=selected_ta).first()
      individual = individual.filter(TA=ta)
      group = group.filter(TA=ta)

    ctx['TA_list'] = TrainingAssistant.objects.all()
    ctx['leaveslips'] = chain(individual,group)  # combines two querysets
    ctx['selected_ta'] = ta or self.request.user
    return ctx


@group_required(('administration',), raise_exception=True)
def modify_status(request, classname, status, id):
  if classname == "individual":
    leaveslip = get_object_or_404(IndividualSlip, pk=id)
  if classname == "group":
    leaveslip = get_object_or_404(GroupSlip, pk=id)
  leaveslip.status = status
  # If sister TA approves the leaveslip, tranfer to a TA brother.
  if status == 'S':
    ta = request.user.TA or TrainingAssistant.objects.filter(gender="B").first()
    leaveslip.TA = ta
  leaveslip.save()

  message =  "%s's %s leaveslip was marked %s" % (leaveslip.trainee, leaveslip.get_type_display().upper(), leaveslip.get_status_display())
  messages.add_message(request, messages.SUCCESS, message)

  return redirect('leaveslips:ta-leaveslip-list')

""" API Views """

class IndividualSlipViewSet(BulkModelViewSet):
  queryset = IndividualSlip.objects.all()
  serializer_class = IndividualSlipSerializer
  filter_backends = (filters.DjangoFilterBackend,)
  filter_class = IndividualSlipFilter
  def get_queryset(self):
    trainee = trainee_from_user(self.request.user)
    individualslip=IndividualSlip.objects.filter(trainee=trainee)
    return individualslip
  def allow_bulk_destroy(self, qs, filtered):
    return filtered

class GroupSlipViewSet(BulkModelViewSet):
  queryset = GroupSlip.objects.all()
  serializer_class = GroupSlipSerializer
  filter_backends = (filters.DjangoFilterBackend,)
  filter_class = GroupSlipFilter
  def get_queryset(self):
    trainee = trainee_from_user(self.request.user)
    groupslip = GroupSlip.objects.filter(Q(trainees=trainee) | Q(trainee=trainee)).distinct()
    return groupslip
  def allow_bulk_destroy(self, qs, filtered):
    return not all(x in filtered for x in qs)

class AllIndividualSlipViewSet(BulkModelViewSet):
  queryset = IndividualSlip.objects.all()
  serializer_class = IndividualSlipSerializer
  filter_backends = (filters.DjangoFilterBackend,)
  filter_class = IndividualSlipFilter
  def allow_bulk_destroy(self, qs, filtered):
    return not all(x in filtered for x in qs)

class AllGroupSlipViewSet(BulkModelViewSet):
  queryset = GroupSlip.objects.all()
  serializer_class = GroupSlipSerializer
  filter_backends = (filters.DjangoFilterBackend,)
  filter_class = GroupSlipFilter
  def allow_bulk_destroy(self, qs, filtered):
    return not all(x in filtered for x in qs)

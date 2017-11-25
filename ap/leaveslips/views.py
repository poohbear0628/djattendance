from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q

from rest_framework import filters
from rest_framework.renderers import JSONRenderer
from rest_framework_bulk import BulkModelViewSet
from braces.views import GroupRequiredMixin

from .models import IndividualSlip, GroupSlip
from .forms import IndividualSlipForm, GroupSlipForm
from .serializers import IndividualSlipSerializer, IndividualSlipFilter, GroupSlipSerializer, GroupSlipFilter
from accounts.models import TrainingAssistant
from terms.models import Term
from schedules.serializers import EventSerializer
from aputils.trainee_utils import trainee_from_user
from aputils.utils import modify_model_status
from aputils.decorators import group_required
from itertools import chain
from datetime import timedelta
import json



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
      attendance_record = leaveslip.trainee.get_attendance_record()

      for r in attendance_record:
        r['event'] = JSONRenderer().render(EventSerializer(r['event']).data)
      ctx['attendance_record'] = json.dumps(attendance_record)
      ctx['events'] = leaveslip.trainee.events_in_date_range(start_date, end_date)
      ctx['start_date'] = start_date
      ctx['end_date'] = end_date + timedelta(1)
      ctx['selected'] = leaveslip.events
      if (leaveslip.type == 'MEAL' or leaveslip.type == 'NIGHT'):
        last_leaveslip = IndividualSlip.objects.exclude(id=leaveslip.id).filter(trainee=leaveslip.trainee, type=leaveslip.type, status='A').first()
        if last_leaveslip is not None:
          ctx['type'] = leaveslip.type
          ctx['last_leaveslip_date'] = last_leaveslip.events[0].date
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
      events = leaveslip.trainee.groupevents_in_week_range(periods[0] * 2, (periods[-1] * 2) + 1)
      selected = []
      for e in events:
        if (leaveslip.start <= e.start_datetime <= leaveslip.end) or (leaveslip.start <= e.end_datetime <= leaveslip.end):
          selected.append(e)

      ctx['events'] = events
      ctx['selected'] = selected
      ctx['start_date'] = start_date
      ctx['end_date'] = end_date
      ctx['today'] = leaveslip.start
    return ctx


# viewing the leave slips
class LeaveSlipList(generic.ListView):
  model = IndividualSlip, GroupSlip
  template_name = 'leaveslips/list.html'

  def get_queryset(self):
   individual = IndividualSlip.objects.filter(trainee=self.request.user.id).order_by('status')
   group = GroupSlip.objects.filter(trainee=self.request.user.id).order_by('status')  # if trainee is in a group leaveslip submitted by another user
   queryset = chain(individual, group, )  # combines two querysets
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

    individual = IndividualSlip.objects.filter(status__in=['P', 'F', 'S']).order_by('submitted')
    group = GroupSlip.objects.filter(status__in=['P', 'F', 'S']).order_by('submitted')  # if trainee is in a group leaveslip submitted by another user

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
    ctx['leaveslips'] = chain(individual, group)  # combines two querysets
    ctx['selected_ta'] = ta or self.request.user
    return ctx


@group_required(('administration',), raise_exception=True)
def modify_status(request, classname, status, id):
  model = IndividualSlip
  if classname == "group":
    model = GroupSlip
  return modify_model_status(model, reverse_lazy('leaveslips:ta-leaveslip-list'))(request, status, id)


""" API Views """
class IndividualSlipViewSet(BulkModelViewSet):
  queryset = IndividualSlip.objects.all()
  serializer_class = IndividualSlipSerializer
  filter_backends = (filters.DjangoFilterBackend, )
  filter_class = IndividualSlipFilter

  def get_queryset(self):
    trainee = trainee_from_user(self.request.user)
    if not trainee.groups.filter(name='attendance_monitors').exists():
      individualslip = IndividualSlip.objects.filter(trainee=trainee)
    else:
      individualslip = IndividualSlip.objects.all()
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
  filter_backends = (filters.DjangoFilterBackend, )
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

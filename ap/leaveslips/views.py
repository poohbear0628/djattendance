from itertools import chain
import json

from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.shortcuts import redirect

from rest_framework import filters
from rest_framework_bulk import BulkModelViewSet
from rest_framework.renderers import JSONRenderer
from braces.views import GroupRequiredMixin

from .models import IndividualSlip, GroupSlip, LeaveSlip
from .forms import IndividualSlipForm, GroupSlipForm
from .serializers import IndividualSlipSerializer, IndividualSlipFilter, GroupSlipSerializer, GroupSlipFilter
from accounts.models import TrainingAssistant, Statistics
from attendance.views import react_attendance_context
from aputils.utils import modify_model_status
from aputils.decorators import group_required
from schedules.serializers import AttendanceEventWithDateSerializer


class LeaveSlipUpdate(GroupRequiredMixin, generic.UpdateView):
  def get_context_data(self, **kwargs):
    listJSONRenderer = JSONRenderer()
    ctx = super(LeaveSlipUpdate, self).get_context_data(**kwargs)
    trainee = self.get_object().get_trainee_requester()
    ctx.update(react_attendance_context(trainee))
    ctx['Today'] = self.get_object().get_date().strftime('%m/%d/%Y')
    ctx['SelectedEvents'] = listJSONRenderer.render(AttendanceEventWithDateSerializer(self.get_object().events, many=True).data)
    ctx['default_transfer_ta'] = self.request.user.TA or self.get_object().TA
    return ctx


class IndividualSlipUpdate(LeaveSlipUpdate):
  model = IndividualSlip
  group_required = ['training_assistant']
  template_name = 'leaveslips/individual_update.html'
  form_class = IndividualSlipForm
  context_object_name = 'leaveslip'

  def get_context_data(self, **kwargs):
    ctx = super(IndividualSlipUpdate, self).get_context_data(**kwargs)
    ctx['show'] = 'leaveslip'
    return ctx

  def post(self, request, **kwargs):
    events = json.loads(request.POST.get('events', '[]'))
    if events:
      IndividualSlipSerializer().update(self.get_object(), {'events': events})
    return super(IndividualSlipUpdate, self).post(request, **kwargs)


class GroupSlipUpdate(LeaveSlipUpdate):
  model = GroupSlip
  group_required = ['training_assistant']
  template_name = 'leaveslips/group_update.html'
  form_class = GroupSlipForm
  context_object_name = 'leaveslip'


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
  group_required = ['training_assistant']
  template_name = 'leaveslips/ta_list.html'

  def post(self, request, *args, **kwargs):
    context = self.get_context_data()
    return super(TALeaveSlipList, self).render_to_response(context)

  def get_context_data(self, **kwargs):
    ctx = super(TALeaveSlipList, self).get_context_data(**kwargs)

    individual = IndividualSlip.objects.all().order_by('status', 'submitted')
    group = GroupSlip.objects.all().order_by('status', 'submitted')  # if trainee is in a group leave slip submitted by another user

    s, _ = Statistics.objects.get_or_create(trainee=self.request.user)

    slip_setting = s.settings.get('leaveslip')
    selected_ta = slip_setting.get('selected_ta', self.request.user.id)
    status = slip_setting.get('selected_status', 'P')

    if self.request.method == 'POST':
      selected_ta = int(self.request.POST.get('leaveslip_ta_list'))
      status = self.request.POST.get('leaveslip_status')
    else:
      status = self.request.GET.get('status', status)
      selected_ta = self.request.GET.get('ta', selected_ta)

    s.settings['leaveslip']['selected_ta'] = selected_ta
    s.settings['leaveslip']['selected_status'] = status
    s.save()

    ta = None
    if selected_ta > 0:
      ta = TrainingAssistant.objects.filter(pk=selected_ta).first()
      individual = individual.filter(TA=ta)
      group = group.filter(TA=ta)

    if status != "-1":
      individual = individual.filter(status=status)
      group = group.filter(status=status)

    # Prefetch for performance
    individual.select_related('trainee', 'TA', 'TA_informed').prefetch_related('rolls')
    group.select_related('trainee', 'TA', 'TA_informed').prefetch_related('trainees')

    ctx['TA_list'] = TrainingAssistant.objects.filter(groups__name='training_assistant')
    ctx['leaveslips'] = chain(individual, group)  # combines two querysets
    ctx['selected_ta'] = ta
    ctx['status_list'] = LeaveSlip.LS_STATUS
    ctx['selected_status'] = status

    return ctx


@group_required(('training_assistant',), raise_exception=True)
def modify_status(request, classname, status, id):
  model = IndividualSlip
  if classname == "group":
    model = GroupSlip
  list_link = modify_model_status(model, reverse_lazy('leaveslips:ta-leaveslip-list'))(request, status, id)
  if "update" in request.META.get('HTTP_REFERER'):
    next_ls = IndividualSlip.objects.filter(status='P', TA=request.user).first()
    if next_ls:
      return redirect(reverse_lazy('leaveslips:individual-update', kwargs={'pk': next_ls.pk}))
    next_ls = GroupSlip.objects.filter(status='P', TA=request.user).first()
    if next_ls:
      return redirect(reverse_lazy('leaveslips:group-update', kwargs={'pk': next_ls.pk}))
  return list_link


# API Views
class IndividualSlipViewSet(BulkModelViewSet):
  queryset = IndividualSlip.objects.all()
  serializer_class = IndividualSlipSerializer
  filter_backends = (filters.DjangoFilterBackend, )
  filter_class = IndividualSlipFilter

  def get_queryset(self):
    user = self.request.user
    if not user.groups.filter(name='attendance_monitors').exists():
      individualslip = IndividualSlip.objects.filter(trainee=user)
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
    user = self.request.user
    if not user.groups.filter(name='attendance_monitors').exists():
      groupslip = GroupSlip.objects.filter(Q(trainees=user) | Q(trainee=user)).distinct()
    else:
      groupslip = GroupSlip.objects.all()
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

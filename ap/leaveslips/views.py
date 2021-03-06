import json
from datetime import datetime, timedelta
from itertools import chain

from accounts.models import Statistics, Trainee, TrainingAssistant
from aputils.decorators import group_required
from aputils.utils import modify_model_status
from attendance.views import react_attendance_context
from braces.views import GroupRequiredMixin
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy, reverse
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from rest_framework import filters
from rest_framework.renderers import JSONRenderer
from rest_framework_bulk import BulkModelViewSet
from schedules.serializers import AttendanceEventWithDateSerializer
from terms.models import Term

from .forms import (GroupSlipAdminForm, GroupSlipForm, IndividualSlipAdminForm,
                    IndividualSlipForm)
from .models import GroupSlip, IndividualSlip, LeaveSlip
from .serializers import (GroupSlipFilter, GroupSlipSerializer,
                          IndividualSlipFilter, IndividualSlipSerializer)
from .utils import find_next_leaveslip


class LeaveSlipUpdate(GroupRequiredMixin, generic.UpdateView):
  def get_context_data(self, **kwargs):
    listJSONRenderer = JSONRenderer()
    ctx = super(LeaveSlipUpdate, self).get_context_data(**kwargs)
    trainee = self.get_object().get_trainee_requester()
    kwargs['period'] = self.get_object().periods[0]
    ctx.update(react_attendance_context(trainee, request_params=kwargs))
    ctx['Today'] = self.get_object().get_date().strftime('%m/%d/%Y')
    ctx['SelectedEvents'] = listJSONRenderer.render(AttendanceEventWithDateSerializer(self.get_object().events, many=True).data)
    ctx['default_transfer_ta'] = trainee.TA_secondary if (trainee.gender == 'S') else trainee.TA
    ctx['assigned_TA'] = self.get_object().TA
    ctx['sister'] = self.request.user.gender == 'S'
    return ctx


class IndividualSlipUpdate(LeaveSlipUpdate):
  model = IndividualSlip
  group_required = ['training_assistant']
  template_name = 'leaveslips/individual_update.html'
  form_class = IndividualSlipForm
  context_object_name = 'leaveslip'

  def get_context_data(self, **kwargs):
    kwargs['leaveslip_type'] = 'individual'
    kwargs['object_id'] = self.object.id
    ctx = super(IndividualSlipUpdate, self).get_context_data(**kwargs)
    current_ls = self.get_object()
    if current_ls.type in ['MEAL', 'NIGHT']:
      IS_list = IndividualSlip.objects.filter(status='A', trainee=current_ls.get_trainee_requester(), type=current_ls.type).order_by('-submitted')
      most_recent_IS = IS_list.first()
      if most_recent_IS and most_recent_IS != current_ls:
        last_date = most_recent_IS.rolls.all().order_by('date').last().date
        ctx['last_date'] = last_date
        ctx['days_since'] = (current_ls.rolls.first().date - last_date).days
    ctx['show'] = 'leaveslip'
    try:
      ctx['next_ls_url'] = find_next_leaveslip(current_ls).get_ta_update_url()
    except AttributeError:
      ctx['next_ls_url'] = "%s?status=P&ta=%s" % (reverse('leaveslips:ta-leaveslip-list'), self.request.user.id)
    ctx['verbose_name'] = current_ls._meta.verbose_name
    current_ls.is_late = current_ls.late
    ctx['leaveslip'] = current_ls
    return ctx

  def post(self, request, **kwargs):
    update = request.POST.dict()
    if request.POST.get('events'):
      update['events'] = json.loads(request.POST.get('events'))
    # 'on' is the POSTed value for checked checkboxes, 'off' for unchecked
    if request.POST.get('ta_sister_approved'):
      update['ta_sister_approved'] = True if request.POST.get('ta_sister_approved') == 'on' else False
    if request.POST.get('texted'):
      update['texted'] = True if request.POST.get('texted') == 'on' else False

    IndividualSlipSerializer().update(self.get_object(), update)
    return HttpResponse('ok')


class GroupSlipUpdate(LeaveSlipUpdate):
  model = GroupSlip
  group_required = ['training_assistant']
  template_name = 'leaveslips/group_update.html'
  form_class = GroupSlipForm
  context_object_name = 'leaveslip'

  def get_context_data(self, **kwargs):
    kwargs['leaveslip_type'] = 'group'
    kwargs['object_id'] = self.object.id
    ctx = super(GroupSlipUpdate, self).get_context_data(**kwargs)
    ctx['show'] = 'groupslip'
    try:
      ctx['next_ls_url'] = find_next_leaveslip(self.get_object()).get_ta_update_url()
    except AttributeError:
      ctx['next_ls_url'] = "%s?status=P&ta=%s" % (reverse('leaveslips:ta-leaveslip-list'), self.request.user.id)
    current_ls = self.get_object()
    current_ls.is_late = current_ls.late
    ctx['leaveslip'] = current_ls
    return ctx

  def post(self, request, **kwargs):
    update = request.POST.dict()
    # 'on' is the POSTed value for checked checkboxes, 'off' for unchecked
    if request.POST.get('ta_sister_approved'):
      update['ta_sister_approved'] = True if request.POST.get('ta_sister_approved') == 'on' else False
    if request.POST.get('texted'):
      update['texted'] = True if request.POST.get('texted') == 'on' else False

    GroupSlipSerializer().update(self.get_object(), update)
    return HttpResponse('ok')


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

    i_slips = IndividualSlip.objects.all()
    g_slips = GroupSlip.objects.all()

    s, _ = Statistics.objects.get_or_create(trainee=self.request.user)

    slip_setting = s.settings.get('leaveslip')
    selected_ta = slip_setting.get('selected_ta', self.request.user.id)
    status = slip_setting.get('selected_status', 'P')
    selected_trainee = slip_setting.get('selected_trainee', Trainee.objects.first().id)

    if self.request.method == 'POST':
      selected_ta = int(self.request.POST.get('leaveslip_ta_list'))
      status = self.request.POST.get('leaveslip_status')
      selected_trainee = self.request.POST.get('leaveslip_trainee_list')
    else:
      status = self.request.GET.get('status', status)
      selected_ta = self.request.GET.get('ta', selected_ta)
      selected_trainee = self.request.GET.get('trainee')

    s.settings['leaveslip']['selected_ta'] = selected_ta
    s.settings['leaveslip']['selected_status'] = status
    s.settings['leaveslip']['selected_trainee'] = selected_trainee
    s.save()

    ta = None
    if int(selected_ta) > 0:
      ta = TrainingAssistant.objects.filter(pk=selected_ta).first()
      i_slips = i_slips.filter(TA=ta)
      g_slips = g_slips.filter(TA=ta)

    tr = None  # selected_trainee
    if selected_trainee and int(selected_trainee) > 0:
      tr = Trainee.objects.filter(pk=selected_trainee).first()
      i_slips = i_slips.filter(trainee=tr)
      g_slips = g_slips.filter(trainees__in=[tr])  # if trainee is in a group leave slip submitted by another user

    if status != "-1":
      si_slips = IndividualSlip.objects.none()
      sg_slips = GroupSlip.objects.none()
      i_slips = i_slips.filter(status=status) | si_slips
      g_slips = g_slips.filter(status=status) | sg_slips

    # Prefetch for performance
    i_slips = i_slips.select_related('trainee', 'TA', 'TA_informed').prefetch_related('rolls__event')
    g_slips = g_slips.select_related('trainee', 'TA', 'TA_informed').prefetch_related('trainees')

    slips = []
    for slip in i_slips:
      rolls = list(slip.rolls.all())
      rolls = sorted(rolls, key=lambda roll: roll.date)
      last_roll = rolls[-1]
      date = last_roll.date
      time = last_roll.event.end
      slip.is_late = slip.submitted > datetime.combine(date, time) + timedelta(hours=48)

      first_roll = rolls[0]
      slip.date = first_roll.date
      slip.period = Term.current_term().period_from_date(first_roll.date)
      slips.append(slip)

    for slip in g_slips:
      slip.is_late = slip.late
      slip.date = slip.start.date()
      slip.period = Term.current_term().period_from_date(slip.start.date())
      slips.append(slip)

    slips = sorted(slips, key=lambda slip: slip.date)

    ctx['TA_list'] = TrainingAssistant.objects.filter(groups__name='regular_training_assistant')
    ctx['leaveslips'] = slips
    ctx['selected_ta'] = ta
    ctx['status_list'] = LeaveSlip.LS_STATUS  # Removes Sister Approved Choice
    ctx['selected_status'] = status
    ctx['selected_trainee'] = tr
    ctx['trainee_list'] = Trainee.objects.all()
    return ctx


@group_required(('training_assistant',), raise_exception=True)
def bulk_modify_status(request, status):
  individual = []
  group = []
  for key, value in request.POST.iteritems():
    if value == "individual":
      individual.append(key)
    else:
      group.append(key)

  if status in ["A", "D"]:
    if individual:
      IndividualSlip.objects.filter(pk__in=individual).update(status=status)
    if group:
      GroupSlip.objects.filter(pk__in=group).update(status=status)
    sample = IndividualSlip.objects.get(pk=individual[0]) if individual else GroupSlip.objects.get(pk=group[0])
    message = "%s %ss were %s" % (len(individual) + len(group), LeaveSlip._meta.verbose_name, sample.get_status_for_message())
    messages.add_message(request, messages.SUCCESS, message)

  if status in ["S", "T"]:
    if status == "S":
      IndividualSlip.objects.filter(pk__in=individual).update(ta_sister_approved=True)
    for pk in individual:
      i = IndividualSlip.objects.get(pk=pk)
      i.TA = i.trainee.TA_secondary
      i.save()
    for pk in group:
      g = GroupSlip.objects.get(pk=pk)
      g.TA = g.trainee.TA_secondary
      g.save()
    status_message = "approved and transferred" if status == "S" else "transferred"
    message = "%s %ss were %s" % (len(individual) + len(group), LeaveSlip._meta.verbose_name, status_message)
    messages.add_message(request, messages.SUCCESS, message)

  return redirect(reverse_lazy('leaveslips:ta-leaveslip-list'))


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


class IndividualSlipCRUDMixin(GroupRequiredMixin):
  model = IndividualSlip
  template_name = 'leaveslips/admin_form.html'
  form_class = IndividualSlipAdminForm
  group_required = [u'attendance_monitors', u'training_assistant']


class IndividualSlipAdminCreate(IndividualSlipCRUDMixin, generic.CreateView):
  def get_context_data(self, **kwargs):
    ctx = super(IndividualSlipAdminCreate, self).get_context_data(**kwargs)
    ctx['page_title'] = 'Create IndividualSlip'
    ctx['button_label'] = 'Create'
    return ctx


class IndividualSlipAdminUpdate(IndividualSlipCRUDMixin, generic.UpdateView):

  def get_context_data(self, **kwargs):
    ctx = super(IndividualSlipAdminUpdate, self).get_context_data(**kwargs)
    ctx['page_title'] = 'Update IndividualSlip'
    ctx['button_label'] = 'Update'
    ctx['delete_button'] = True
    return ctx

  def get_form_kwargs(self):
    kwargs = super(IndividualSlipAdminUpdate, self).get_form_kwargs()
    kwargs['trainee'] = self.get_object().trainee
    return kwargs


class IndividualSlipAdminDelete(IndividualSlipCRUDMixin, generic.DeleteView):
  success_url = reverse_lazy('leaveslips:admin-islip-create')


class GroupSlipCRUDMixin(GroupRequiredMixin):
  model = GroupSlip
  template_name = 'leaveslips/admin_form.html'
  form_class = GroupSlipAdminForm
  group_required = [u'attendance_monitors', u'training_assistant', u'service_schedulers']


class GroupSlipAdminCreate(GroupSlipCRUDMixin, generic.CreateView):
  def get_context_data(self, **kwargs):
    ctx = super(GroupSlipAdminCreate, self).get_context_data(**kwargs)
    ctx['page_title'] = 'Create GroupSlip'
    ctx['button_label'] = 'Create'
    return ctx


class GroupSlipAdminUpdate(GroupSlipCRUDMixin, generic.UpdateView):

  def get_success_url(self):
    return self.object.get_admin_url()

  def get_context_data(self, **kwargs):
      ctx = super(GroupSlipAdminUpdate, self).get_context_data(**kwargs)
      ctx['page_title'] = 'Update GroupSlip'
      ctx['button_label'] = 'Update'
      ctx['delete_button'] = True
      return ctx


class GroupSlipAdminDelete(GroupSlipCRUDMixin, generic.DeleteView):
  success_url = reverse_lazy('leaveslips:admin-gslip-create')

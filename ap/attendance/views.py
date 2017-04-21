import django_filters
from itertools import chain
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy, resolve
from django.db.models import Q
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters
from rest_framework.renderers import JSONRenderer
from datetime import date, datetime, time
from collections import OrderedDict
from .models import Roll
from .serializers import RollSerializer, RollFilter, AttendanceSerializer, AttendanceFilter
from schedules.models import Schedule, Event
from schedules.constants import WEEKDAYS
from leaveslips.models import IndividualSlip, GroupSlip
from terms.models import Term
from accounts.models import Trainee, TrainingAssistant
from leaveslips.forms import IndividualSlipForm
from seating.models import Chart, Seat, Partial
from rest_framework_bulk import (
    BulkModelViewSet
)
from rest_framework.renderers import JSONRenderer
from django.core import serializers

from accounts.serializers import TraineeSerializer, TrainingAssistantSerializer, TraineeRollSerializer, TraineeForAttendanceSerializer
from schedules.serializers import AttendanceEventWithDateSerializer, EventWithDateSerializer
from leaveslips.serializers import IndividualSlipSerializer, GroupSlipSerializer
from seating.serializers import ChartSerializer, SeatSerializer, PartialSerializer
from terms.serializers import TermSerializer

from aputils.trainee_utils import trainee_from_user
from aputils.utils import get_item, lookup
from aputils.eventutils import EventUtils
from aputils.groups_required_decorator import group_required
from copy import copy
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

class AttendancePersonal(TemplateView):
  template_name = 'attendance/attendance_react.html'
  context_object_name = 'context'

  def get_context_data(self, **kwargs):
    listJSONRenderer = JSONRenderer()
    ctx = super(AttendancePersonal, self).get_context_data(**kwargs)
    user = self.request.user
    trainee = trainee_from_user(user)
    trainees = Trainee.objects.filter(is_active=True).prefetch_related('terms_attended')
    ctx['events'] = trainee.events
    serialized_obj = serializers.serialize('json', ctx['events'])
    ctx['schedule'] = Schedule.objects.filter(trainees=trainee)
    ctx['events_bb'] = listJSONRenderer.render(AttendanceEventWithDateSerializer(ctx['events'], many=True).data)
    ctx['trainee'] = trainee
    ctx['trainee_bb'] = listJSONRenderer.render(TraineeForAttendanceSerializer(ctx['trainee']).data)
    ctx['trainees'] = trainees
    ctx['trainees_bb'] = listJSONRenderer.render(TraineeForAttendanceSerializer(ctx['trainees'], many=True).data)
    ctx['rolls'] = Roll.objects.filter(trainee=trainee)
    ctx['rolls_bb'] = listJSONRenderer.render(RollSerializer(ctx['rolls'], many=True).data)
    ctx['leaveslipform'] = IndividualSlipForm()
    ctx['individualslips'] = IndividualSlip.objects.filter(trainee=trainee)
    ctx['individualslips_bb'] = listJSONRenderer.render(IndividualSlipSerializer(ctx['individualslips'], many=True).data)
    ctx['groupslips'] = GroupSlip.objects.filter(Q(trainee=trainee) | Q(trainees=trainee)).distinct()
    ctx['groupslips_bb'] = listJSONRenderer.render(GroupSlipSerializer(ctx['groupslips'], many=True).data)
    ctx['TAs'] = TrainingAssistant.objects.all()
    ctx['TAs_bb'] = listJSONRenderer.render(TrainingAssistantSerializer(ctx['TAs'], many=True).data)
    ctx['term'] = Term.objects.filter(current=True)
    ctx['term_bb'] = listJSONRenderer.render(TermSerializer(ctx['term'], many=True).data)
    return ctx

# View for Class/Seat Chart Based Rolls
class RollsView(TemplateView):
  template_name = 'attendance/roll_class.html'
  context_object_name = 'context'

  def post(self, request, *args, **kwargs):
    context = self.get_context_data()
    return super(RollsView, self).render_to_response(context)

  def get_context_data(self, **kwargs):
    lJRender = JSONRenderer().render
    ctx = super(RollsView, self).get_context_data(**kwargs)
    user = self.request.user
    trainee = trainee_from_user(user)
    # TODO - insert check for current user type

    if self.request.method == 'POST':
      selected_week = self.request.POST.get('week')
      event_id = self.request.POST.get('events')
      event = Event.objects.get(id=event_id)
      selected_date = event.date_for_week(int(selected_week))
    else:
      selected_date = date.today()
      selected_week = Event.week_from_date(selected_date)
      current_time = datetime.now()
      # try;
      events = trainee.immediate_upcoming_event(with_seating_chart=True)
      # TODO: - if trainee has no current event load other class that is occuring at the same time
      if len(events) > 0:
        event = events[0]
      else:
        event = None

    selected_week = int(selected_week)

    if event:
      chart = Chart.objects.filter(event=event).first()
      if chart:
        seats = Seat.objects.filter(chart=chart).select_related('trainee')
        partial = Partial.objects.filter(chart=chart).order_by('section_name')
        # Get roll with with for current event and today's date
        roll = Roll.objects.filter(event=event, date=selected_date)
        # TODO - Add group leaveslips
        individualslips = IndividualSlip.objects.filter(rolls=roll, status='A')
        trainees = Trainee.objects.filter(schedules__events=event)
        schedules = Schedule.get_all_schedules_in_weeks_for_trainees([selected_week,], trainees)

        w_tb = EventUtils.collapse_priority_event_trainee_table([selected_week,], schedules, trainees)

        t_set = EventUtils.get_trainees_attending_event_in_week(w_tb, event, selected_week)

        for s in seats:
          if s.trainee in t_set:
            s.attending = True
          else:
            s.attending = False

        start_datetime = datetime.combine(selected_date, event.start)
        end_datetime = datetime.combine(selected_date, event.end)
        group_slip = GroupSlip.objects.filter(end__gte=start_datetime, start__lte=end_datetime, status='A').prefetch_related('trainees')
        print group_slip, start_datetime, end_datetime
        trainee_groupslip = set()
        for gs in group_slip:
          trainee_groupslip = trainee_groupslip | set(gs.trainees.all())

        ctx['event'] = event
        ctx['event_bb'] = lJRender(EventWithDateSerializer(event).data)
        ctx['attendance_bb'] = lJRender(RollSerializer(roll, many=True).data)
        ctx['individualslips_bb'] = lJRender(IndividualSlipSerializer(individualslips, many=True).data)
        ctx['trainee_groupslip_bb'] = lJRender(TraineeRollSerializer(trainee_groupslip, many=True).data)
        ctx['trainees_bb'] = lJRender(TraineeRollSerializer(trainees, many=True).data)
        ctx['chart'] = chart
        ctx['chart_bb'] = lJRender(ChartSerializer(chart, many=False).data)
        ctx['seats'] = seats
        ctx['seats_bb'] = lJRender(SeatSerializer(seats, many=True).data)
        ctx['partial'] = partial
        ctx['partial_bb'] = lJRender(PartialSerializer(partial, many=True).data)

    ctx['weekdays'] = WEEKDAYS
    ctx['date'] = selected_date
    ctx['week'] = selected_week
    ctx['day'] = selected_date.weekday()
    current_url = resolve(self.request.path_info).url_name
    ctx['current_url'] = current_url

    # ctx['leaveslips'] = chain(list(IndividualSlip.objects.filter(trainee=self.request.user.trainee).filter(events__term=Term.current_term())), list(GroupSlip.objects.filter(trainee=self.request.user.trainee).filter(start__gte=Term.current_term().start).filter(end__lte=Term.current_term().end)))

    return ctx

class TableRollsView(TemplateView):
  template_name = 'attendance/roll_table.html'
  context_object_name = 'context'

  def post(self, request, *args, **kwargs):
    context = self.get_context_data()
    return super(TableRollsView, self).render_to_response(context)

  def get_context_data(self, **kwargs):
    ctx = super(TableRollsView, self).get_context_data(**kwargs)

    current_term = Term.current_term()
    if self.request.method == 'POST':
      selected_week = int(self.request.POST.get('week'))
      selected_date = current_term.startdate_of_week(selected_week)
    else:
      selected_date = date.today()
    current_week = current_term.term_week_of_date(selected_date)
    start_date = current_term.startdate_of_week(current_week)
    end_date = current_term.enddate_of_week(current_week)
    start_datetime = datetime.combine(start_date, time())
    end_datetime = datetime.combine(end_date, time())

    trainees = kwargs['trainees']
    event_type = kwargs['type']
    event_list, trainee_evt_list = Schedule.get_roll_table_by_type_in_weeks(trainees, event_type, [current_week,])
    rolls = Roll.objects.filter(event__in=event_list, date__gte=start_date, date__lte=end_date).select_related('trainee','event')
    group_slip = GroupSlip.objects.filter(end__gte=start_datetime, start__lte=end_datetime, status='A').order_by('start', 'end').prefetch_related('trainees')
    group_slip_tbl = OrderedDict()
    event_groupslip_tbl = OrderedDict()
    for gs in group_slip:
      gs_start = group_slip_tbl.setdefault(gs.start, OrderedDict())
      gs_end = gs_start.setdefault(gs.end, set())
      gs_end.add(gs)
    for evt in event_list:
      for gs_start in group_slip_tbl:
        if gs_start > evt.start_datetime:
          break
        else:
          for gs_end in group_slip_tbl[gs_start]:
            if gs_end < evt.end_datetime:
              break
            else:
              for g in group_slip_tbl[gs_start][gs_end]:
                eg_set = event_groupslip_tbl.setdefault(evt, set(g.trainees.all()))
                event_groupslip_tbl[evt] = event_groupslip_tbl[evt] | set(g.trainees.all())

    # TODO - Add group leaveslips
    rolls_withslips = rolls.filter(leaveslips__isnull=False, leaveslips__status="A")

    # trainees: [events,]
    # event.roll = roll
    # {trainee: OrderedDict({
    #   (event, date): roll
    # }),}
    roll_dict = OrderedDict()

    # Populate roll_dict from roll object for look up for building roll table
    for roll in rolls:
      r = roll_dict.setdefault(roll.trainee, OrderedDict())
      if roll in rolls_withslips:
        roll.leaveslip = True
      r[(roll.event, roll.date)] = roll

    # print trainee_evt_list, roll_dict, trainees, event_type

    # Add roll to each event from roll table
    for trainee in roll_dict:
      # Only update if trainee predefined
      if trainee in trainee_evt_list:
        evt_list = trainee_evt_list[trainee]
        if len(evt_list) <= 0:
          # delete empty column if all blocked out
          del trainee_evt_list[trainee]
        else:
          for i in range(0, len(evt_list)):
            ev = copy(evt_list[i])
            d = ev.start_datetime.date()
            # Add roll if roll exists for trainee
            if trainee in roll_dict and (ev, d) in roll_dict[trainee]:
              ev.roll = roll_dict[trainee][(ev, d)]
            evt_list[i] = ev

    ctx['event_type'] = event_type
    ctx['start_date'] = start_date
    ctx['term_start_date'] = current_term.start.strftime('%Y%m%d')
    ctx['current_week'] = current_week
    ctx['trainees'] = trainees
    ctx['trainees_event_list'] = trainee_evt_list
    ctx['event_list'] = event_list
    current_url = resolve(self.request.path_info).url_name
    ctx['current_url'] = current_url
    ctx['event_groupslip_tbl'] = event_groupslip_tbl
    return ctx

# Meal Rolls
class MealRollsView(TableRollsView):
  def get_context_data(self, **kwargs):
    # We get all 1st year trainees and 2nd year that are under audit
    kwargs['trainees'] = Trainee.objects.filter(Q(self_attendance=False,current_term__gt=2)|Q(current_term__lte=2))
    kwargs['type'] = 'M'
    ctx = super(MealRollsView, self).get_context_data(**kwargs)
    ctx['title'] = "meal rolls"
    return ctx

# House Rolls
class HouseRollsView(TableRollsView):
  def get_context_data(self, **kwargs):
    user = self.request.user
    trainee = trainee_from_user(user)
    kwargs['trainees'] = Trainee.objects.filter(house=trainee.house).filter(Q(self_attendance=False,current_term__gt=2)|Q(current_term__lte=2))
    kwargs['type'] = 'H'
    ctx = super(HouseRollsView, self).get_context_data(**kwargs)
    ctx['title'] = "house rolls"
    return ctx

class RFIDRollsView(TableRollsView):
  def get_context_data(self, **kwargs):
    user = self.request.user
    trainee = trainee_from_user(user)
    kwargs['trainees'] = Trainee.objects.all()
    kwargs['type'] = 'RF'
    ctx = super(RFIDRollsView, self).get_context_data(**kwargs)
    ctx['title'] = "RFID rolls"
    return ctx

# Team Rolls
class TeamRollsView(TableRollsView):
  def get_context_data(self, **kwargs):
    user = self.request.user
    trainee = trainee_from_user(user)
    kwargs['trainees'] = Trainee.objects.filter(team=trainee.team).filter(Q(self_attendance=False,current_term__gt=2)|Q(current_term__lte=2))
    kwargs['type'] = 'T'
    ctx = super(TeamRollsView, self).get_context_data(**kwargs)
    ctx['title'] = "team rolls"
    return ctx

# YPC Rolls
class YPCRollsView(TableRollsView):
  def get_context_data(self, **kwargs):
    kwargs['trainees'] = Trainee.objects.filter(Q(self_attendance=False,current_term__gt=2)|Q(current_term__lte=2))
    kwargs['type'] = 'Y'
    ctx = super(YPCRollsView, self).get_context_data(**kwargs)
    ctx['title'] = "YPC rolls"
    return ctx

class RollViewSet(BulkModelViewSet):
  queryset = Roll.objects.all()
  serializer_class = RollSerializer
  filter_backends = (filters.DjangoFilterBackend,)
  filter_class = RollFilter
  def get_queryset(self):
    user = self.request.user
    trainee = trainee_from_user(user)
    roll = trainee.current_rolls
    return roll
  def allow_bulk_destroy(self, qs, filtered):
    return filtered

    # failsafe- to only delete if qs is filtered.
    # return not all(x in filtered for x in qs)

class AttendanceViewSet(BulkModelViewSet):
  queryset = Trainee.objects.filter(is_active=True)
  serializer_class = AttendanceSerializer
  filter_backends = (filters.DjangoFilterBackend,)
  # filter_class = AttendanceFilter
  def get_queryset(self):
    user = self.request.user
    trainee = trainee_from_user(user)
    return trainee
  def allow_bulk_destroy(self, qs, filtered):
    return not all(x in filtered for x in qs)

class AllRollViewSet(BulkModelViewSet):
  queryset = Roll.objects.all()
  serializer_class = RollSerializer
  filter_backends = (filters.DjangoFilterBackend,)
  filter_class = RollFilter
  def allow_bulk_destroy(self, qs, filtered):
    return not all(x in filtered for x in qs)

class AllAttendanceViewSet(BulkModelViewSet):
  queryset = Trainee.objects.filter(is_active=True)
  serializer_class = AttendanceSerializer
  filter_backends = (filters.DjangoFilterBackend,)
  # filter_class = AttendanceFilter
  def allow_bulk_destroy(self, qs, filtered):
    return not all(x in filtered for x in qs)

@group_required(('attendance_monitors',))
def rfid_signin(request, trainee_id):
  trainee = get_object_or_404(Trainee, rfid_tag=trainee_id)
  events = filter(lambda x: x.monitor == 'RF', trainee.immediate_upcoming_event())
  if not events:
    return HttpResponse('No event found')
  now = datetime.now().time()
  if (event.start.hour * 60 + event.start.minute) - (now.hour * 60 + now.minute) > 15:
    status = 'T'
  else:
    status = 'P'
  roll = Roll(event=events[0], trainee=trainee, status=status, submitted_by=trainee, date=datetime.now())
  roll.save()

  return HttpResponse('Roll entered')

@group_required(('attendance_monitors',))
def rfid_finalize(request, event_id, event_date):
  event = get_object_or_404(Event, pk=event_id)
  date = datetime.strptime(event_date, "%Y-%m-%d").date()
  if not event.monitor == 'RF':
    return HttpResponse('No event found')

  # mark trainees without a roll for this event absent
  rolls = event.roll_set.filter(date=date)
  trainees_with_roll = set([roll.trainee for roll in rolls])
  schedules = event.schedules.all()
  for schedule in schedules:
    trainees = schedule.trainees.all()
    for trainee in trainees:
      if trainee not in trainees_with_roll:
        roll = Roll(event=event, trainee=trainee, status='A', submitted_by=trainee, date=date, finalized=True)
        roll.save()

  # mark existing rolls as finalized
  for roll in rolls:
    roll.finalized = True
    roll.save()

  # don't keep a record of present to save space
  rolls.filter(status='P', leaveslips__isnull=True).delete()

  return HttpResponse('Roll finalized')

@group_required(('attendance_monitors',))
def rfid_tardy(request, event_id, event_date):
  event = get_object_or_404(Event, pk=event_id)
  date = datetime.strptime(event_date, "%Y-%m-%d").date()
  if not event.monitor == 'RF':
    return HttpResponse('No event found')
  event.roll_set.filter(date=date, status='T', leaveslips__isnull=True).delete()
  return HttpResponse('Roll tardies removed')

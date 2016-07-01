import django_filters
from itertools import chain
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters
from rest_framework.renderers import JSONRenderer
from datetime import date, datetime
from .models import Roll
from .serializers import RollSerializer, RollFilter, AttendanceSerializer, AttendanceFilter
from schedules.models import Schedule, Event
from schedules.constants import WEEKDAYS
from leaveslips.models import IndividualSlip, GroupSlip
from terms.models import Term
from accounts.models import Trainee, TrainingAssistant
from leaveslips.models import IndividualSlip
from leaveslips.forms import IndividualSlipForm
from seating.models import Chart, Seat, Partial
from rest_framework_bulk import (
    BulkModelViewSet
)
from rest_framework.renderers import JSONRenderer
from django.core import serializers

from schedules.serializers import AttendanceEventWithDateSerializer, EventWithDateSerializer
from accounts.serializers import TraineeSerializer, TrainingAssistantSerializer, TraineeRollSerializer
from leaveslips.serializers import IndividualSlipSerializer
from seating.serializers import ChartSerializer, SeatSerializer, PartialSerializer

from aputils.utils import trainee_from_user

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

class AttendancePersonal(TemplateView):
    template_name = 'attendance/attendance_react.html'
    context_object_name = 'context'


    def get_context_data(self, **kwargs):
        listJSONRenderer = JSONRenderer()
        ctx = super(AttendancePersonal, self).get_context_data(**kwargs)
        user = self.request.user
        trainee = trainee_from_user(user)
        ctx['events'] = trainee.events
        ctx['events_bb'] = listJSONRenderer.render(AttendanceEventWithDateSerializer(ctx['events'], many=True).data)
        ctx['trainee'] = [trainee]
        ctx['trainee_bb'] = listJSONRenderer.render(TraineeSerializer(ctx['trainee'], many=True).data)
        ctx['rolls'] = Roll.objects.filter(trainee=trainee)
        ctx['rolls_bb'] = listJSONRenderer.render(RollSerializer(ctx['rolls'], many=True).data)
        ctx['leaveslipform'] = IndividualSlipForm()
        ctx['individualslips'] = IndividualSlip.objects.filter(trainee=trainee)
        ctx['individualslips_bb'] = listJSONRenderer.render(IndividualSlipSerializer(ctx['individualslips'], many=True).data)
        ctx['TAs'] = TrainingAssistant.objects.all()
        ctx['TAs_bb'] = listJSONRenderer.render(TrainingAssistantSerializer(ctx['TAs'], many=True).data)
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
            selected_week = Event.static_week_from_date(selected_date)
            current_time = datetime.now()
            # try;
            events = trainee.immediate_upcoming_event(True)
            # TODO: - if trainee has no current event load other class that is occuring at the same time
            if len(events) > 0:
                event = events[0]
            else:
                event = None

        if event:
            schedule = Schedule.objects.filter(events=event)
            try:
                chart = Chart.objects.get(event=event)
            except Chart.DoesNotExist:
                chart = None
            seats = Seat.objects.filter(chart=chart)
            partial = Partial.objects.filter(chart=chart).order_by('section_name')
            # Get roll with with for current event and today's date
            roll = Roll.objects.filter(event=event, date=selected_date)

            trainees = Trainee.objects.filter(schedules__events=event)

            t_set = []

            for t in trainees:
                t_set.append(t)

            for s in seats:
                if s.trainee in t_set:
                    s.attending = True
                else:
                    s.attending = False

            trainees = Trainee.objects.filter(chart=chart)
            
            ctx['event'] = event
            ctx['event_bb'] = lJRender(EventWithDateSerializer(event).data)
            ctx['attendance'] = roll
            ctx['attendance_bb'] = lJRender(RollSerializer(roll, many=True).data)
            ctx['trainees'] = trainees
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

        # ctx['leaveslips'] = chain(list(IndividualSlip.objects.filter(trainee=self.request.user.trainee).filter(events__term=Term.current_term())), list(GroupSlip.objects.filter(trainee=self.request.user.trainee).filter(start__gte=Term.current_term().start).filter(end__lte=Term.current_term().end)))

        return ctx

# Meal Rolls
class MealRollsView(TemplateView):
    template_name = 'attendance/roll_meal.html'
    context_object_name = 'context'
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        return super(MealRollsView, self).render_to_response(context)

    def get_context_data(self, **kwargs):   
        lJRender = JSONRenderer().render
        ctx = super(MealRollsView, self).get_context_data(**kwargs)
        user = self.request.user
        trainee = trainee_from_user(user)
        # TODO - insert check for current user type
        current_term = Term.current_term()

        # selected_date = date.today()
        # current_week = current_term.term_week_of_date(selected_date)
        # start_date = current_term.start.strftime('%Y%m%d')
        # events = Schedule.get_all_events_by_type_in_week('M', current_week)
        
        # trainees = Trainee.objects.filter(schedules__events__in=events).distinct()
        # evt_trainee_tbl = Schedule.get_event_trainee_mapping(trainees, events)
        # roll = Roll.objects.filter(event=event, date=selected_date)

        # schedules = Schedule.objects.filter(events__type='M')
        

        # ctx['start_date'] = start_date
        # ctx['trainees'] = trainees
        # ctx['trainees_bb'] = lJRender(TraineeRollSerializer(trainees, many=True).data)
        # ctx['event'] = event
        # ctx['event_bb'] = lJRender(EventWithDateSerializer(event).data)
        # ctx['events'] = evt_trainee_tbl
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

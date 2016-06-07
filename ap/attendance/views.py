import django_filters
from itertools import chain
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters
from rest_framework.renderers import JSONRenderer
from datetime import date
from .models import Roll
from .serializers import RollSerializer, RollFilter, AttendanceSerializer, AttendanceFilter
from schedules.models import Schedule, Event
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
from accounts.serializers import TraineeSerializer, TrainingAssistantSerializer
from schedules.serializers import AttendanceEventWithDateSerializer
from leaveslips.serializers import IndividualSlipSerializer
from accounts.serializers import TraineeRollSerializer
from seating.serializers import ChartSerializer, SeatSerializer, PartialSerializer

from aputils.utils import trainee_from_user

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

class RollsView(TemplateView):
    template_name = 'attendance/roll_class.html'
    context_object_name = 'context'

    # Logic
    # 1. Get current event (TODO)
    # 2. Based on event load the correct seating chart and trainees with assigned seats
    # 3. Pull leaveslips for absent trainees (TODO)
    # 
    def get_context_data(self, **kwargs):   
        listJSONRenderer = JSONRenderer()
        ctx = super(RollsView, self).get_context_data(**kwargs)
        user = self.request.user
        trainee = trainee_from_user(user)
        # TODO - insert check for current user type
        
        # Current event
        event = Event.objects.filter(pk=2)
        chart = Chart.objects.filter(event=event)
        seats = Seat.objects.filter(chart=chart)
        partial = Partial.objects.filter(chart=chart).order_by('section_name')
        # Get roll with with for current event and today's date
        roll = Roll.objects.filter(event=event, date="2016-06-04")
        trainees = Trainee.objects.filter(id__in=chart.values_list('trainees'))

        ctx['event'] = event
        ctx['event_bb'] = listJSONRenderer.render(EventWithDateSerializer(event, many=True).data)
        ctx['attendance'] = roll
        ctx['attendance_bb'] = listJSONRenderer.render(RollSerializer(roll, many=True).data)
        ctx['trainees'] = trainees
        ctx['trainees_bb'] = listJSONRenderer.render(TraineeRollSerializer(trainees, many=True).data)
        ctx['chart'] = chart
        ctx['chart_bb'] = listJSONRenderer.render(ChartSerializer(chart, many=True).data)
        ctx['chart_id'] = chart.first().id
        ctx['seats'] = seats
        ctx['seats_bb'] = listJSONRenderer.render(SeatSerializer(seats, many=True).data)
        ctx['partial'] = partial
        ctx['partial_bb'] = listJSONRenderer.render(PartialSerializer(partial, many=True).data)
        # ctx['leaveslips'] = chain(list(IndividualSlip.objects.filter(trainee=self.request.user.trainee).filter(events__term=Term.current_term())), list(GroupSlip.objects.filter(trainee=self.request.user.trainee).filter(start__gte=Term.current_term().start).filter(end__lte=Term.current_term().end)))

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

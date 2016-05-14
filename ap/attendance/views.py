import django_filters
from itertools import chain
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters
from .models import Roll
from .serializers import RollSerializer, RollFilter, AttendanceSerializer, AttendanceFilter
from schedules.models import Schedule, Event
from leaveslips.models import IndividualSlip, GroupSlip
from terms.models import Term
from accounts.models import User, Trainee
from leaveslips.models import IndividualSlip
from leaveslips.forms import IndividualSlipForm
from rest_framework_bulk import (
    BulkModelViewSet
)
from rest_framework.renderers import JSONRenderer
from schedules.serializers import EventSerializer
from django.core import serializers

class AttendancePersonal(TemplateView):
    template_name = 'attendance/attendance_detail.html'
    context_object_name = 'context'

    def get_context_data(self, **kwargs):   
        listJSONRenderer = JSONRenderer()
        context = super(AttendancePersonal, self).get_context_data(**kwargs)

        context['events'] = self.request.user.trainee.events
        
        serialized_obj = serializers.serialize('json',  context['events'] )
        print 'LOOKHERE'
        # print serialized_obj
        context['schedule'] = Schedule.objects.all()
        context['events_bb'] = listJSONRenderer.render(EventSerializer(context['events'], many=True).data)
        # context['events_list'] = listJSONRenderer.render(self.request.user.trainee.events)
        # print context['events_bb']
        context['trainee'] = self.request.user.trainee
        # context['schedule'] = Schedule.objects.get(trainee=self.request.user.trainee)
        # context['attendance'] = Roll.objects.filter(trainee=self.request.user.trainee)
        context['leaveslipform'] = IndividualSlipForm()
        # context['leaveslips'] = chain(list(IndividualSlip.objects.filter(trainee=self.request.user.trainee).filter(events__term=Term.current_term())), list(GroupSlip.objects.filter(trainee=self.request.user.trainee).filter(start__gte=Term.current_term().start).filter(end__lte=Term.current_term().end)))
        return context

class RollViewSet(BulkModelViewSet):
    queryset = Roll.objects.all()
    serializer_class = RollSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = RollFilter
    def get_queryset(self):
        user = self.request.user
        roll = Roll.objects.filter(trainee=user.trainee)
        return roll
    def allow_bulk_destroy(self, qs, filtered):
        return filtered
        #return not all(x in filtered for x in qs)

class AttendanceViewSet(BulkModelViewSet):
    queryset = Trainee.objects.all()
    serializer_class = AttendanceSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = AttendanceFilter
    def get_queryset(self):
        user = self.request.user
        trainee = Trainee.objects.filter(account=user)
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
    queryset = Trainee.objects.all()
    serializer_class = AttendanceSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = AttendanceFilter
    def allow_bulk_destroy(self, qs, filtered):
        return not all(x in filtered for x in qs)
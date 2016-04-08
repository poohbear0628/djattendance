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

class AttendancePersonal(TemplateView):
    template_name = 'attendance/attendance_detail.html'
    context_object_name = 'context'

    def get_context_data(self, **kwargs):
        context = super(AttendancePersonal, self).get_context_data(**kwargs)
        context['events'] = Event.objects.filter(term=Term.current_term())
        context['trainee'] = self.request.user.trainee
        context['schedule'] = Schedule.objects.filter(term=Term.current_term()).get(trainee=self.request.user.trainee)
        context['attendance'] = Roll.objects.filter(trainee=self.request.user.trainee).filter(event__term=Term.current_term())
        context['leaveslipform'] = IndividualSlipForm()
        context['leaveslips'] = chain(list(IndividualSlip.objects.filter(trainee=self.request.user.trainee).filter(events__term=Term.current_term())), list(GroupSlip.objects.filter(trainee=self.request.user.trainee).filter(start__gte=Term.current_term().start).filter(end__lte=Term.current_term().end)))
        return context

class RollViewSet(BulkModelViewSet):
    queryset = Roll.objects.all()
    serializer_class = RollSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = RollFilter
    def get_queryset(self):
        user = self.request.user
        roll = Roll.objects.filter(trainee=user.trainee).filter(event__term=Term.current_term())
        return roll
    def allow_bulk_destroy(self, qs, filtered):
        return not all(x in filtered for x in qs)

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

    #Attempt at implementing OR.
    def get_queryset(self):
        queryset = Roll.objects.all()
        data = self.request.get_full_path()
        if ('_' not in data):
            return queryset
        data = data.split('_',1)[1]
        data = data.split('&and_')
        or_params = {}
        and_params = {}
        for key in data:
            if '&or_' in key:
                firstFilter=True
                splitdata = key.split('&or_')
                for splitdata2 in splitdata:
                    or_data = splitdata2.split('=')
                    if (or_data[1]=='True'):
                        or_data[1] = True
                    elif (or_data[1]=='False'):
                        or_data[1] = False
                    or_params[or_data[0]] = or_data[1]
                    if firstFilter:
                        queryset = queryset.filter(**or_params)
                        firstFilter=False
                    else:
                        queryset = queryset | Roll.objects.filter(**or_params)
                    or_params={}
            else:
                splitdata=key.split('=')
                if (splitdata[1]=='True'):
                    splitdata[1] = True
                elif (splitdata[1]=='False'):
                    splitdata[1] = False
                and_params[splitdata[0]] = splitdata[1]
                queryset = queryset.filter(**and_params)
                and_params={}
        return queryset
    def allow_bulk_destroy(self, qs, filtered):
        return not all(x in filtered for x in qs)

class AllAttendanceViewSet(BulkModelViewSet):
    queryset = Trainee.objects.all()
    serializer_class = AttendanceSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = AttendanceFilter
    def allow_bulk_destroy(self, qs, filtered):
        return not all(x in filtered for x in qs)
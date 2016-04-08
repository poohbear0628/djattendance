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
    template_name = 'attendance/attendance_react.html'
    context_object_name = 'context'

    def get_context_data(self, **kwargs):
        #jsx.transform('static/js/react/attendance/calendar.jsx', 'static/js/react/attendance/calendar.js')

        listJSONRenderer = JSONRenderer()

        context = super(AttendancePersonal, self).get_context_data(**kwargs)
        context['events'] = Event.objects.filter(term=Term.current_term())
        context['trainee'] = self.request.user.trainee
        context['trainee_bb'] = listJSONRenderer.render(TraineeSerializer(context['trainee']).data)

        print 'current term', Term.current_term()
        context['schedule'] = Schedule.objects.filter(term=Term.current_term()).get(trainee=self.request.user.trainee)
        context['events_bb'] = listJSONRenderer.render(EventSerializer(context['schedule'].events.all(), many=True).data)
        context['attendance'] = Roll.objects.filter(trainee=self.request.user.trainee).filter(event__term=Term.current_term())
        context['attendance_bb'] = listJSONRenderer.render(RollSerializer(context['attendance'], many=True).data)
        context['leaveslipform'] = IndividualSlipForm()
        print 'trainee', self.request.user.trainee, IndividualSlip.objects.filter(trainee=self.request.user.trainee), IndividualSlip.objects.filter(trainee=self.request.user.trainee).filter(events__term=Term.current_term())
        context['leaveslips'] = IndividualSlip.objects.filter(trainee=self.request.user.trainee).filter(events__term=Term.current_term())
        context['groupslips'] = GroupSlip.objects.filter(trainee=self.request.user.trainee).filter(start__gte=Term.current_term().start).filter(end__lte=Term.current_term().end)
        print 'slips', context['leaveslips']
        context['leaveslips_bb'] = listJSONRenderer.render(IndividualSlipSerializer(context['leaveslips'], many=True).data)
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

<<<<<<< HEAD
class RollViewSet(mixins.BulkCreateModelMixin, mixins.BulkUpdateModelMixin, viewsets.ModelViewSet):
    queryset = Roll.objects.all()
    model = Roll
    # serializer_class = RollSerializer
=======
class AllRollViewSet(BulkModelViewSet):
    queryset = Roll.objects.all()
    serializer_class = RollSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = RollFilter
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
>>>>>>> a47295ef47d7251adb6836514b2f8ac9be85a7d2

from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.template import RequestContext
from django.forms.models import modelform_factory
from django.contrib.admin.widgets import AdminDateWidget
from django.db.models import Q
from rest_framework import viewsets, filters

from accounts.models import Trainee
from .models import Schedule, Event
from .serializers import EventSerializer, ScheduleSerializer, EventFilter, ScheduleFilter, AttendanceEventWithDateSerializer
from ap.forms import TraineeSelectForm
from terms.models import Term
from rest_framework_bulk import BulkModelViewSet

from aputils.trainee_utils import trainee_from_user

###  API-ONLY VIEWS  ###

class EventViewSet(viewsets.ModelViewSet):
  queryset = Event.objects.all()
  serializer_class = AttendanceEventWithDateSerializer
  def get_queryset(self):
    user = self.request.user
    if 'trainee' in self.request.GET:
      trainee = Trainee.objects.get(pk=self.request.GET.get('trainee'))
    else:
      trainee = trainee_from_user(user)
    return trainee.events
  def allow_bulk_destroy(self, qs, filtered):
    return not all(x in filtered for x in qs)

class ScheduleViewSet(viewsets.ModelViewSet):
  queryset = Schedule.objects.all()
  serializer_class = ScheduleSerializer
  filter_backends = (filters.DjangoFilterBackend,)
  filter_class = ScheduleFilter
  def get_queryset(self):
    trainee = trainee_from_user(self.request.user)
    schedule=Schedule.objects.filter(trainees=trainee)
    return schedule
  def allow_bulk_destroy(self, qs, filtered):
    return not all(x in filtered for x in qs)

class AllEventViewSet(BulkModelViewSet):
  queryset = Event.objects.all()
  serializer_class = EventSerializer
  filter_backends = (filters.DjangoFilterBackend,)
  filter_class = EventFilter
  def get_queryset(self):
    try:
      week = int(self.request.GET.get('week',''))
      day = int(self.request.GET.get('weekday', ''))
      date = Term.current_term().get_date(week, day)
      return Event.objects.filter(chart__isnull=False).filter(Q(weekday=day, day__isnull=True) | Q(day=date))
    except ValueError as e:
      print '%s (%s)' % (e.message, type(e))
      return Event.objects.all()

  def allow_bulk_destroy(self, qs, filtered):
    return not all(x in filtered for x in qs)

class AllScheduleViewSet(viewsets.ModelViewSet):
  queryset = Schedule.objects.all()
  serializer_class = ScheduleSerializer
  filter_backends = (filters.DjangoFilterBackend,)
  filter_class = ScheduleFilter
  def allow_bulk_destroy(self, qs, filtered):
    return not all(x in filtered for x in qs)

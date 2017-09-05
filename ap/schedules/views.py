from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.template import RequestContext
from django.forms.models import modelform_factory
from django.contrib.admin.widgets import AdminDateWidget
from django.db.models import Q
from rest_framework import viewsets, filters

from .models import Schedule, Event
from .serializers import EventSerializer, ScheduleSerializer, EventFilter, ScheduleFilter
from ap.forms import TraineeSelectForm
from terms.models import Term, FIRST_WEEK, LAST_WEEK
from rest_framework_bulk import BulkModelViewSet

from aputils.trainee_utils import trainee_from_user

class EventDetail(generic.DetailView):
  model = Event
  context_object_name = "event"


class EventDelete(generic.DeleteView):
  model = Event
  success_url = reverse_lazy('schedules:event-create')


class TermEvents(generic.ListView):
  model = Event
  template_name = 'schedules/term_events.html'
  context_object_name = 'events'

  def get_queryset(self, **kwargs):
    return Event.objects.filter(term=Term.decode(self.kwargs['term']))

  def get_context_data(self, **kwargs):
    context = super(TermEvents, self).get_context_data(**kwargs)
    context['term'] = Term.decode(self.kwargs['term'])
    return context

###  API-ONLY VIEWS  ###

class EventViewSet(viewsets.ModelViewSet):
  queryset = Event.objects.all()
  serializer_class = EventSerializer
  filter_backends = (filters.DjangoFilterBackend,)
  filter_class = EventFilter
  def get_queryset(self):
    user = self.request.user
    trainee = trainee_from_user(user)
    events = Event.objects.filter(schedules = trainee.schedules.all())
    return events
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

class AllEventViewSet(viewsets.ModelViewSet):
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

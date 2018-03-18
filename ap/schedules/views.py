from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import Q
from rest_framework import viewsets, filters

from .models import Schedule, Event
from .serializers import EventWithDateSerializer, EventSerializer, ScheduleSerializer, EventFilter, ScheduleFilter
from accounts.models import Trainee
from terms.models import Term

from aputils.trainee_utils import trainee_from_user


def assign_trainees_to_schedules(request):
  for s in Schedule.objects.all():
    s.assign_trainees()
  messages.success(request, 'Assigned trainees to schedules')
  return redirect('home')


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


#  API-ONLY VIEWS  #
class EventViewSet(viewsets.ModelViewSet):
  queryset = Event.objects.all()
  serializer_class = EventWithDateSerializer

  def get_queryset(self):
    if 'trainee' in self.request.GET:
      trainee = Trainee.objects.get(pk=self.request.GET.get('trainee'))
    else:
      user = self.request.user
      trainee = trainee_from_user(user)
    events = trainee.events
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
    schedule = Schedule.objects.filter(trainees=trainee)
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
      week = int(self.request.GET.get('week', ''))
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

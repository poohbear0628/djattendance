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
from terms.models import Term, FIRST_WEEK, LAST_WEEK
from rest_framework_bulk import BulkModelViewSet

from aputils.trainee_utils import trainee_from_user

class SchedulePersonal(generic.TemplateView):
  template_name = 'schedules/schedule_detail.html'
  context_object_name = 'schedule'

  def get_context_data(self, **kwargs):
    context = super(SchedulePersonal, self).get_context_data(**kwargs)
    c_term = Term.current_term()
    start_date = c_term.startdate_of_week(FIRST_WEEK)
    end_date = c_term.enddate_of_week(LAST_WEEK)
    trainee = trainee_from_user(self.request.user)
    # context['schedule'] = Schedule.objects.filter(trainees=trainee)
    context['events'] = trainee.events_in_date_range(start_date, end_date)
    context['start_date'] = start_date
    context['end_date'] = end_date
    return context

class ScheduleDetail(generic.DetailView):
  template_name = 'schedules/schedule_detail.html'
  context_object_name = 'schedule'

  def get_queryset(self):
    trainee = trainee_from_user(self.request.user)
    return Schedule.objects.filter(trainee=trainee).filter(term=Term.current_term())


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

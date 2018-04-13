from django.views.generic import TemplateView
from attendance.models import Roll
from leaveslips.models import IndividualSlip
from schedules.models import Event, Schedule
from ap.base_datatable_view import BaseDatatableView
from django.core.urlresolvers import reverse_lazy
import json


class LeaveSlipsJSON(BaseDatatableView):
  model = IndividualSlip
  columns = ['id', 'trainee', 'rolls', 'status', 'TA']
  order_columns = ['id', 'trainee', 'rolls', 'status', 'TA']
  max_display_length = 120

  def filter_queryset(self, qs):
    search = self.request.GET.get(u'search[value]', None)
    if search:
      qs = qs.filter(trainee__firstname__istartswith=search) | qs.filter(trainee__lastname__istartswith=search)
      if search.isdigit():
        qs = qs | qs.filter(id=int(search))  # | qs.filter(rolls__in=[int(search)])
    return qs


class RollsJSON(BaseDatatableView):
  model = Roll
  columns = ['id', 'trainee', 'event', 'status', 'submitted_by']
  order_columns = ['id', 'trainee', 'event', 'status', 'submitted_by']
  max_display_length = 120

  def filter_queryset(self, qs):
    # use parameters passed in GET request to filter queryset

    # simple example:
    search = self.request.GET.get(u'search[value]', None)
    if search:
      qs = qs.filter(trainee__firstname__istartswith=search) | qs.filter(trainee__lastname__istartswith=search)
    return qs


class EventsJSON(BaseDatatableView):
  model = Event
  columns = ['id', 'name', 'weekday']
  order_columns = ['id', 'name', 'weekday']
  max_display_length = 120

  def filter_queryset(self, qs):
    # use parameters passed in GET request to filter queryset

    # simple example:
    search = self.request.GET.get(u'search[value]', None)
    if search:
      qs = qs.filter(name__istartswith=search)
      if search.isdigit():
        qs = qs | qs.filter(id=int(search))
    return qs


class Viewer(TemplateView):
  template_name = 'data/viewer.html'
  viewer_name = ''
  targets = []
  header = []

  def get_context_data(self, **kwargs):
    ctx = super(Viewer, self).get_context_data(**kwargs)
    ctx['page_title'] = self.viewer_name + ' Viewer'
    ctx['source_url'] = reverse_lazy("attendance:" + self.viewer_name + "-json")
    ctx['targets_list'] = json.dumps(self.targets)
    ctx['header'] = self.header
    return ctx


class LeaveSlipViewer(Viewer):
  viewer_name = 'leaveslips'
  targets = [0, 1, 2, 3, 4]
  header = ['ID', 'Trainee', 'Rolls', 'Status', 'TA']

  def get_context_data(self, **kwargs):
    ctx = super(LeaveSlipViewer, self).get_context_data(**kwargs)
    ctx['page_title'] = 'Individual Leave Slip Viewer'
    return ctx


class RollsViewer(Viewer):
  viewer_name = 'rolls'
  targets = [0, 1, 2, 3, 4]
  header = ['ID', 'Trainee', 'Event', 'Status', 'Submitted By']

  def get_context_data(self, **kwargs):
    ctx = super(RollsViewer, self).get_context_data(**kwargs)
    ctx['page_title'] = 'Rolls Viewer'
    return ctx


class EventsViewer(Viewer):
  viewer_name = 'events'
  targets = [0, 1, 2]
  header = ['ID', 'Name', 'Weekday']

  def get_context_data(self, **kwargs):
    ctx = super(EventsViewer, self).get_context_data(**kwargs)
    ctx['page_title'] = 'Events Viewer'
    return ctx


# class SchedulesViewer(TemplateView):
#   pass

from django.views.generic import TemplateView
from django.db.models import Q
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
    ret = qs.none()
    if search:
      filters = []
      filters.append(Q(trainee__firstname__istartswith=search))
      filters.append(Q(trainee__lastname__istartswith=search))
      filters.append(Q(id=search))
      filters.append(Q(rolls__in=[search]))
      for f in filters:
        try:
          ret = ret | qs.filter(f)
        except ValueError:
          continue
      return ret
    else:
      return qs


class RollsJSON(BaseDatatableView):
  model = Roll
  columns = ['id', 'trainee', 'event', 'status', 'submitted_by']
  order_columns = ['id', 'trainee', 'event', 'status', 'submitted_by']
  max_display_length = 120

  def filter_queryset(self, qs):
    search = self.request.GET.get(u'search[value]', None)
    ret = qs.none()
    if search:
      filters = []
      filters.append(Q(trainee__firstname__istartswith=search))
      filters.append(Q(trainee__lastname__istartswith=search))
      filters.append(Q(id=search))
      for f in filters:
        try:
          ret = ret | qs.filter(f)
        except ValueError:
          continue
      return ret
    else:
      return qs


class EventsJSON(BaseDatatableView):
  model = Event
  columns = ['id', 'name', 'weekday']
  order_columns = ['id', 'name', 'weekday']
  max_display_length = 120

  def filter_queryset(self, qs):
    search = self.request.GET.get(u'search[value]', None)
    ret = qs.none()
    if search:
      filters = []
      filters.append(Q(name__istartswith=search))
      filters.append(Q(id=search))
      for f in filters:
        try:
          ret = ret | qs.filter(f)
        except ValueError:
          continue
      return ret
    else:
      return qs


class SchedulesJSON(BaseDatatableView):
  model = Schedule
  columns = ['id', 'name', 'events', 'weeks', 'team_roll']
  order_columns = ['id', 'name', 'weekday', '', 'team_roll']
  max_display_length = 120

  def filter_queryset(self, qs):
    search = self.request.GET.get(u'search[value]', None)
    ret = qs.none()
    if search:
      filters = []
      filters.append(Q(name__istartswith=search))
      filters.append(Q(id=search))
      for f in filters:
        try:
          ret = ret | qs.filter(f)
        except ValueError:
          continue
      return ret
    else:
      return qs


class Viewer(TemplateView):
  template_name = 'data/viewer.html'
  viewer_name = ''
  header = []

  def get_context_data(self, **kwargs):
    ctx = super(Viewer, self).get_context_data(**kwargs)
    ctx['page_title'] = self.viewer_name + ' Viewer'
    ctx['source_url'] = reverse_lazy("attendance:" + self.viewer_name + "-json")
    ctx['header'] = self.header
    ctx['targets_list'] = json.dumps([i for i, v in enumerate(self.header)])
    return ctx


class LeaveSlipViewer(Viewer):
  viewer_name = 'leaveslips'
  header = ['ID', 'Trainee', 'Rolls', 'Status', 'TA']

  def get_context_data(self, **kwargs):
    ctx = super(LeaveSlipViewer, self).get_context_data(**kwargs)
    ctx['page_title'] = 'Individual Leave Slip Viewer'
    return ctx


class RollsViewer(Viewer):
  viewer_name = 'rolls'
  header = ['ID', 'Trainee', 'Event', 'Status', 'Submitted By']

  def get_context_data(self, **kwargs):
    ctx = super(RollsViewer, self).get_context_data(**kwargs)
    ctx['page_title'] = 'Rolls Viewer'
    return ctx


class EventsViewer(Viewer):
  viewer_name = 'events'
  header = ['ID', 'Name', 'Weekday']

  def get_context_data(self, **kwargs):
    ctx = super(EventsViewer, self).get_context_data(**kwargs)
    ctx['page_title'] = 'Events Viewer'
    return ctx


class SchedulesViewer(Viewer):
  viewer_name = 'schedules'
  header = ['ID', 'Name', 'Weekday', 'Weeks', 'Team Roll']

  def get_context_data(self, **kwargs):
    ctx = super(SchedulesViewer, self).get_context_data(**kwargs)
    ctx['page_title'] = 'Schedules Viewer'
    return ctx

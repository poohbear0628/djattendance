from django.views.generic import TemplateView
from django.db.models import Q
from attendance.models import Roll
from leaveslips.models import IndividualSlip, GroupSlip
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


class GroupSlipsJSON(BaseDatatableView):
  model = GroupSlip
  columns = ['id', 'trainees', 'description', 'status', 'service_assignment']
  order_columns = ['id', '', 'description', 'status', 'service_assignment']
  max_display_length = 120
  use_admin_url = True

  def filter_queryset(self, qs):
    search = self.request.GET.get(u'search[value]', None)
    ret = qs.none()
    if search:
      filters = []
      filters.append(Q(trainees__in=[search]))
      filters.append(Q(trainees__in=[search]))
      filters.append(Q(trainee__in=[search]))
      filters.append(Q(service_assignment__service__name__icontains=search))
      filters.append(Q(id=search))
      filters.append(Q(description__icontains=search))
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
      filters.append(Q(name__icontains=search))
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
      filters.append(Q(name__icontains=search))
      filters.append(Q(team_roll__name__icontains=search))
      filters.append(Q(id=search))
      for f in filters:
        try:
          ret = ret | qs.filter(f)
        except ValueError:
          continue
      return ret
    else:
      return qs


class DataTableViewer(TemplateView):
  template_name = 'data/viewer.html'
  DataTableView = None
  source_url = ''

  def get_context_data(self, **kwargs):
    ctx = super(DataTableViewer, self).get_context_data(**kwargs)
    ctx['source_url'] = self.source_url
    header = self.DataTableView().get_header()
    ctx['header'] = header
    ctx['targets_list'] = json.dumps([i for i, v in enumerate(header)])
    return ctx


class GroupSlipViewer(DataTableViewer):
  DataTableView = GroupSlipsJSON
  source_url = reverse_lazy('attendance:groupslip-json')

  def get_context_data(self, **kwargs):
    ctx = super(GroupSlipViewer, self).get_context_data(**kwargs)
    ctx['page_title'] = 'Group Leave Slip Viewer'
    return ctx


class LeaveSlipViewer(DataTableViewer):
  DataTableView = LeaveSlipsJSON
  source_url = reverse_lazy('attendance:leaveslips-json')

  def get_context_data(self, **kwargs):
    ctx = super(LeaveSlipViewer, self).get_context_data(**kwargs)
    ctx['page_title'] = 'Individual Leave Slip Viewer'
    return ctx


class RollsViewer(DataTableViewer):
  DataTableView = RollsJSON
  source_url = reverse_lazy('attendance:rolls-json')

  def get_context_data(self, **kwargs):
    ctx = super(RollsViewer, self).get_context_data(**kwargs)
    ctx['page_title'] = 'Rolls Viewer'
    return ctx


class EventsViewer(DataTableViewer):
  DataTableView = EventsJSON
  source_url = reverse_lazy('attendance:events-json')

  def get_context_data(self, **kwargs):
    ctx = super(EventsViewer, self).get_context_data(**kwargs)
    ctx['page_title'] = 'Events Viewer'
    return ctx


class SchedulesViewer(DataTableViewer):
  DataTableView = SchedulesJSON
  source_url = reverse_lazy('attendance:schedules-json')

  def get_context_data(self, **kwargs):
    ctx = super(SchedulesViewer, self).get_context_data(**kwargs)
    ctx['page_title'] = 'Schedules Viewer'
    return ctx

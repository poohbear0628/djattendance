from django.views.generic import TemplateView
from django.db.models import Q
from attendance.models import Roll
from leaveslips.models import IndividualSlip, GroupSlip
from schedules.models import Event, Schedule
from ap.base_datatable_view import BaseDatatableView
from django.core.urlresolvers import reverse_lazy
import json
from accounts.models import Trainee

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

class RollsJSON(BaseDatatableView):
  model = Roll
  fields = ['id', 'trainee', 'event', 'event.id', 'date', 'status', 'finalized', 'submitted_by']
  columns = fields
  order_columns = fields
  max_display_length = 200

  def filter_queryset(self, qs):
    search = self.request.GET.get(u'search[value]', None)
    qs_params = Q()
    ret = qs.none()
    if search:
      for exp in search.split():
        try:
          q = Q(trainee__firstname__contains=exp)|Q(trainee__lastname__contains=exp)|Q(id__contains=exp)|Q(event__id__contains=exp)|Q(event__name__contains=exp)|Q(date__contains=exp)|Q(satus__contains=exp)
          qs_params = qs_params & q if q else qs_params

        except ValueError:
          continue
        
      ret = ret | qs.filter(qs_params)
      return ret
    else:
      return qs

class RollsViewer(DataTableViewer):
  DataTableView = RollsJSON
  source_url = reverse_lazy('attendance:rolls-json')

  def get_context_data(self, **kwargs):
    ctx = super(RollsViewer, self).get_context_data(**kwargs)
    ctx['page_title'] = 'Rolls Viewer'
    return ctx


class LeaveSlipsJSON(BaseDatatableView):
  model = IndividualSlip
  fields = ['id', 'trainee', 'rolls', 'status', 'TA', 'type']
  columns = fields
  order_columns = fields
  max_display_length = 200

  def filter_queryset(self, qs):
    search = self.request.GET.get(u'search[value]', None)
    qs_params = Q()
    ret = qs.none()
    if search:
      for exp in search.split():
        try:
          q = Q(trainee__firstname__contains=exp)|Q(trainee__lastname__contains=exp)|Q(id__contains=exp)|Q(type__contains=exp)|Q(rolls__event__name__contains=exp)|Q(rolls__event__id__contains=exp)|Q(rolls__id__contains=exp)
          qs_params = qs_params & q if q else qs_params

        except ValueError:
          continue

      ret = ret | qs.filter(qs_params)
      return ret
    else:
      return qs

class LeaveSlipViewer(DataTableViewer):
  DataTableView = LeaveSlipsJSON
  source_url = reverse_lazy('attendance:leaveslips-json')

  def get_context_data(self, **kwargs):
    ctx = super(LeaveSlipViewer, self).get_context_data(**kwargs)
    ctx['page_title'] = 'Individual Leave Slip Viewer'
    return ctx


class GroupSlipsJSON(BaseDatatableView):
  model = GroupSlip
  columns = ['id', 'submitted', 'trainees', 'description', 'status', 'service_assignment']
  order_columns = ['id', 'submitted', '', 'description', 'status', 'service_assignment']
  max_display_length = 200
  use_admin_url = True

  def filter_queryset(self, qs):
    search = self.request.GET.get(u'search[value]', None)
    ret = qs.none()
    if search:
      filters = []
      filters.append(Q(trainee__in=[search]))
      filters.append(Q(service_assignment__service__name__icontains=search))
      filters.append(Q(id=search))
      filters.append(Q(description__icontains=search))

      # ManyToMany
      ls = list(Trainee.objects.filter(firstname__icontains=search).values_list('id', flat=True))
      filters.append(Q(trainees__in=ls))
      ls = list(Trainee.objects.filter(lastname__icontains=search).values_list('id', flat=True))
      filters.append(Q(trainees__in=ls))

      for f in filters:
        try:
          ret = ret | qs.filter(f)
        except ValueError:
          continue
      return ret
    else:
      return qs


class GroupSlipViewer(DataTableViewer):
  DataTableView = GroupSlipsJSON
  source_url = reverse_lazy('attendance:groupslips-json')

  def get_context_data(self, **kwargs):
    ctx = super(GroupSlipViewer, self).get_context_data(**kwargs)
    ctx['page_title'] = 'Group Leave Slip Viewer'
    return ctx


class EventsJSON(BaseDatatableView):
  model = Event
  fields = ['id', 'name', 'weekday', 'type', 'monitor', 'start', 'end', 'chart']
  columns = fields
  order_columns = fields
  max_display_length = 200

  def filter_queryset(self, qs):
    search = self.request.GET.get(u'search[value]', None)
    qs_params = Q()
    ret = qs.none()
    if search:
      for exp in search.split():
        try:
          q = Q(id__contains=exp)|Q(name__contains=exp)|Q(weekday__contains=exp)|Q(type__contains=exp)|Q(monitor__contains=exp)|Q(start__contains=exp)|Q(end__contains=exp)
          qs_params = qs_params & q if q else qs_params

        except ValueError:
          continue

      ret = ret | qs.filter(qs_params)
      return ret
    else:
      return qs


class EventsViewer(DataTableViewer):
  DataTableView = EventsJSON
  source_url = reverse_lazy('attendance:events-json')

  def get_context_data(self, **kwargs):
    ctx = super(EventsViewer, self).get_context_data(**kwargs)
    ctx['page_title'] = 'Events Viewer'
    return ctx


class SchedulesJSON(BaseDatatableView):
  model = Schedule
  columns = ['id', 'name', 'events', 'trainees', 'weeks', 'team_roll', 'priority']
  order_columns = ['id', 'name', 'events', 'trainees', 'weeks', 'team_roll', 'priority']
  max_display_length = 200

  # def filter_queryset(self, qs):
  #   search = self.request.GET.get(u'search[value]', None)
  #   qs_params = Q()
  #   ret = qs.none()
  #   if search:
  #     for exp in search.split():
  #       try:
  #         q = Q(id__contains=exp)|Q(name__contains=exp)|Q(weekday__contains=exp)|Q(type__contains=exp)|Q(monitor__contains=exp)|Q(start__contains=exp)|Q(end__contains=exp)
  #         qs_params = qs_params & q if q else qs_params

  #       except ValueError:
  #         continue

  #     ret = ret | qs.filter(qs_params)
  #     return ret
  #   else:
  #     return qs

class SchedulesViewer(DataTableViewer):
  DataTableView = SchedulesJSON
  source_url = reverse_lazy('attendance:schedules-json')

  def get_context_data(self, **kwargs):
    ctx = super(SchedulesViewer, self).get_context_data(**kwargs)
    ctx['page_title'] = 'Schedules Viewer'
    return ctx

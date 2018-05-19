from django.views.generic.base import TemplateView


class DataTableView(TemplateView):
  template_name = ""
  cols = []
  source_url = ""

  def get_context_data(self, **kwargs):
    ctx = super(DataTableView, self).get_context_data(**kwargs)
    ctx['source_url'] = self.source_url
    ctx['cols'] = self.cols


class EventsViewer(DataTableView):
  template_name = "data/viewer.html"
  source_url = "/api/allevents/"
  cols = ['id', 'name', 'weekday', 'type', 'monitor', 'start', 'end', 'chart']

  def get_context_data(self, **kwargs):
    ctx = super(EventsViewer, self).get_context_data(**kwargs)
    ctx['page_title'] = 'Events Viewer'
    return ctx


class SchedulesViewer(DataTableView):
  template_name = "data/viewer.html"
  source_url = "/api/allschedules/"
  cols = ['id', 'name', 'events', 'weeks', 'team_roll', 'priority']

  def get_context_data(self, **kwargs):
    ctx = super(SchedulesViewer, self).get_context_data(**kwargs)
    ctx['page_title'] = 'Schedules Viewer'
    return ctx


class GroupSlipViewer(DataTableView):
  template_name = "data/viewer.html"
  source_url = "/api/allgroupslips/"
  cols = ['id', 'trainee', 'submitted', 'description', 'status', 'service_assignment', 'start', 'end']

  def get_context_data(self, **kwargs):
    ctx = super(GroupSlipViewer, self).get_context_data(**kwargs)
    ctx['page_title'] = 'Group Leave Slip Viewer'
    return ctx


class LeaveSlipViewer(DataTableView):
  template_name = "data/viewer.html"
  source_url = "/api/allindividualleaveslips/"
  cols = ['id', 'trainee', 'rolls', 'status', 'TA', 'type']

  def get_context_data(self, **kwargs):
    ctx = super(LeaveSlipViewer, self).get_context_data(**kwargs)
    ctx['page_title'] = 'Individual Leave Slip Viewer'
    return ctx


class RollsViewer(TemplateView):
  template_name = "data/viewer.html"
  source_url = "/api/allrolls/"
  cols = ['id', 'trainee', 'event', 'event.id', 'date', 'status', 'finalized', 'submitted_by']

  def get_context_data(self, **kwargs):
    ctx = super(RollsViewer, self).get_context_data(**kwargs)
    ctx['page_title'] = 'Rolls Viewer'
    return ctx

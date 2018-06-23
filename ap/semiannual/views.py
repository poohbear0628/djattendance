import json
from copy import copy, deepcopy
from collections import OrderedDict
from datetime import date, datetime, time, timedelta

import dateutil.parser
from accounts.models import Trainee, TrainingAssistant
from accounts.serializers import (TraineeForAttendanceSerializer,
                                  TraineeRollSerializer,
                                  TrainingAssistantSerializer)
from ap.forms import TraineeSelectForm
from aputils.decorators import group_required
from aputils.eventutils import EventUtils
from aputils.trainee_utils import is_trainee, trainee_from_user
from braces.views import GroupRequiredMixin
from django.core.urlresolvers import resolve, reverse_lazy
from django.db.models import Q
from django.forms.forms import NON_FIELD_ERRORS
from django.forms.utils import ErrorList
from django.http import (HttpResponse, HttpResponseBadRequest,
                         HttpResponseServerError, JsonResponse)
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from houses.models import House
from leaveslips.models import GroupSlip, IndividualSlip
from leaveslips.serializers import (GroupSlipSerializer,
                                    GroupSlipTADetailSerializer,
                                    IndividualSlipSerializer,
                                    IndividualSlipTADetailSerializer)
from rest_framework import filters, status
from rest_framework.renderers import JSONRenderer
from rest_framework_bulk import BulkModelViewSet
from rest_framework.response import Response
from schedules.constants import WEEKDAYS
from schedules.models import Event, Schedule
from schedules.serializers import (AttendanceEventWithDateSerializer,
                                   EventWithDateSerializer)
from seating.models import Chart, Partial, Seat
from seating.serializers import (ChartSerializer, PartialSerializer,
                                 SeatSerializer)
from teams.models import Team
from terms.models import Term
from terms.serializers import TermSerializer

from attendance.views import TableRollsView
from attendance.forms import RollAdminForm
from attendance.models import Roll
from attendance.serializers import AttendanceSerializer, RollFilter, RollSerializer

# universal variable for this term
CURRENT_TERM = Term.current_term()

class SemiAnnualView(TableRollsView):
  def get_context_data(self, **kwargs):
    kwargs['selected_date'] = CURRENT_TERM.get_date(19, 3)
    kwargs['trainees'] = Trainee.objects.filter(pk=self.request.user.id)
    kwargs['event_type'] = 'S'
    kwargs['monitor'] = 'HC'
    ctx = super(SemiAnnualView, self).get_context_data(**kwargs)
    ctx['title'] = "Semi-annual Study Attendance"
    return ctx

class SemiAnnualStudyReport(ListView):
  model = Roll
  template_name = 'semiannual/semi-annual_study_attendance.html'

  def get_context_data(self, **kwargs):
    ctx = super(SemiAnnualStudyReport, self).get_context_data(**kwargs)
    ctx['title'] = 'Semi-annual Study Attendance Report'

    evs = Schedule.objects.get(weeks=19).events.filter(type='S')
    rolls = Roll.objects.filter(event__in=evs).order_by('trainee__lastname', 'trainee__firstname')

    ctx['headers'] = ['Name', 'Term', 'Location', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    roll_dict = []
    for t in Trainee.objects.filter(is_active=True):
      t_rolls = rolls.filter(trainee=t)
      t_dict = {
       'Name': t.full_name2,
       'Term': t.current_term,
       'Tue': ' ',
       'Wed': ' ',
       'Thu': ' ',
       'Fri': ' ',
       'Sat': ' ',
      }

      # TODO add location
      t_dict['Location'] = 'TC'

      for r in t_rolls:
        w_day = r.date.strftime("%a")
        t_dict[w_day] = r.status

      roll_dict.append(t_dict)

    ctx['rolls'] = roll_dict
    return ctx
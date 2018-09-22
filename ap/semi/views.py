# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from accounts.models import Trainee
from aputils.trainee_utils import is_trainee, trainee_from_user
from braces.views import GroupRequiredMixin
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.base import TemplateView
from django.views.generic import UpdateView
from semi.forms import AttendanceForm, LocationForm
from semi.models import SemiAnnual
from semi.utils import attendance_stats, ROLL_STATUS
from terms.models import Term
from copy import deepcopy

class SemiView(TemplateView):
  template_name = 'semi/semi_base.html'

  def get_object(self, queryset=None):
    ct = Term.current_term()
    if is_trainee(self.request.user):
      trainee = trainee_from_user(self.request.user)
    else:
      trainee = Trainee.objects.first()
    obj, created = SemiAnnual.objects.get_or_create(trainee=trainee, term=ct)
    return obj

  def get(self, request, *args, **kwargs):
    semiannual = self.get_object()
    context = self.get_context_data(**kwargs)
    location_form = LocationForm(instance=semiannual)
    context['location_form'] = location_form

    attendance_form = AttendanceForm(initial=semiannual.attendance)
    context['attendance_form'] = attendance_form
    return self.render_to_response(context)

  def get_context_data(self, **kwargs):
    context = super(SemiView, self).get_context_data(**kwargs)
    headers = [rs[1] for rs in ROLL_STATUS]
    headers.insert(0, '')
    context['headers'] = headers
    context['button_label'] = "Save"
    context['page_title'] = "Semi-Annaul Study Attendance"

    show_attendance = False
    ct = Term.current_term()
    start_date = ct.startdate_of_week(19)
    if datetime.date.today() + datetime.timedelta(days=3) >= start_date:
      show_attendance = True
    context['show_attendance'] = show_attendance
    context['term'] = ct
    return context

  def post(self, request, *args, **kwargs):
    semiannual = self.get_object()
    data = deepcopy(request.POST)
    if 'location_form' in data.keys():
      del data['location_form']
      form = LocationForm(data)
      if form.is_valid():
        data = form.cleaned_data
        for field, value in data.items():
          setattr(semiannual, field, value)
          semiannual.save()


    elif 'attendance_form' in data.keys():
      del data['attendance_form']
      form = AttendanceForm(data)
      if form.is_valid():
        data = form.cleaned_data
        for k, v in data.items():
          semiannual.attendance[k] = v
        semiannual.save()

    return redirect(reverse('semi:semi-base'))

class AttendanceReport(GroupRequiredMixin, TemplateView):
  template_name = 'semi/attendance_report.html'
  group_required = ['training_assistant']

  @staticmethod
  def get_report_context():
    term = Term.current_term()
    semis = SemiAnnual.objects.filter(term=term)
    data = []
    for t in Trainee.objects.all():
      d = {'name': t.full_name, 'term': t.current_term}
      if semis.filter(trainee=t).exists():
        semi = semis.get(trainee=t)
        if 'N' in semi.attendance.values():
          d['submitted'] = "No"
        else:
          d['submitted'] = "Yes"
          d['semi'] = semi
          d['stats'] = attendance_stats(semi)
      else:
        d['submitted'] = "No"
      data.append(d)
    return data

  def get_context_data(self, **kwargs):
    context = super(AttendanceReport, self).get_context_data(**kwargs)
    context['page_title'] = "Attendance Report"
    context['term'] = Term.current_term()
    context['data'] = self.get_report_context()
    return context


class LocationReport(GroupRequiredMixin, TemplateView):
  template_name = 'semi/location_report.html'
  group_required = ['training_assistant']

  @staticmethod
  def get_report_context():
    term = Term.current_term()
    semis = SemiAnnual.objects.filter(term=term)
    data = []
    for t in Trainee.objects.all():
      d = {'name': t.full_name, 'term': t.current_term, 'gender': t.gender}
      if semis.filter(trainee=t).exists():
        semi = semis.get(trainee=t)
        d['semi'] = semi
      data.append(d)
    return data

  def get_context_data(self, **kwargs):
    context = super(LocationReport, self).get_context_data(**kwargs)
    context['page_title'] = "Location Report"
    context['term'] = Term.current_term()
    context['data'] = self.get_report_context()
    return context

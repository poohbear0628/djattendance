# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic.edit import DeleteView
from django.views.generic import TemplateView
from django.http import HttpResponse

from .models import GospelStat, GospelPair
from terms.models import Term
from accounts.models import Trainee

from datetime import *

from braces.views import GroupRequiredMixin

#ctx[cols] = attributes
attributes = ['Tracts Distributed','Bibles Distributed','Contacted (>30 sec)','Led to Pray','Baptized','2nd Appointment','Regular Appointment','Minutes on the Gospel','Bible Study','Small Groups','District Meeting (New Student)','Conference']
_attributes = ['Tracts_Distributed','Bibles_Distributed','Contacted_(>30_sec)','Led_to_Pray','Baptized','2nd_Appointment','Regular_Appointment','Minutes_on_the_Gospel','Bible_Study','Small_Groups','District_Meeting_(New_Student)','Conference']
ctx = dict()
for i in _attributes:
  ctx[i]=0

def get_week():
  for i in range(0,21):
    if Term.current_term().startdate_of_week(i) <= date.today()\
    and Term.current_term().enddate_of_week(i) >= date.today():
      return i

#In Progress
class GospelStatisticsView(TemplateView):
  template_name = "gospel_statistics/gospel_statistics.html"

  def get_context_data(self, **kwargs):
    current_user = self.request.user
    context = super(GospelStatisticsView, self).get_context_data(**kwargs)
    context['page_title'] = 'Team Statistics'
    context['team'] = current_user.team
    context['gospel_pairs'] = GospelPair.objects.filter(team=current_user.team)
    context['cols'] = attributes
    context['week'] = get_week()
    return context

class NewGospelPairView(TemplateView):
  template_name = "gospel_statistics/new_pair.html"

  def post(self, request, *args, **kwargs):
    context = self.get_context_data()
    list_of_trainee_id = request.POST.getlist('inputs')
    #Check for duplicate
    list_of_trainees = []
    for each in list_of_trainee_id:
      list_of_trainees.extend(Trainee.objects.filter(id=each))
    gospelpair = GospelPair(team=context['team'], term=Term.current_term())
    gospelpair.save()
    for each in list_of_trainees:
      print each
      gospelpair.trainees.add(each)
    return redirect(reverse('gospel_statistics:gospel-statistics-view'))

  def get_context_data(self, **kwargs):
    current_user = self.request.user
    context = super(NewGospelPairView, self).get_context_data(**kwargs)
    context['page_title'] = 'New Gospel Pair'
    context['team'] = current_user.team
    context['members'] = Trainee.objects.filter(team=current_user.team)
    return context

#Delete
def weekly_statistics(request):
  current_week = get_week()
  current_team = request.user.team
  stats = GospelStat.objects.filter(week=current_week)
  weekly_stats = []
  gps = []
  #Get all existing gospel pairs
  for stat in stats:
    print stat.trainees
  return HttpResponse(json.dumps(weekly_stats))

#In Progress (change to class)
def TAGospelStatisticsView(request):
  context = {
    'page_title': 'TA Gospel Statistics',
  }
  return render(request, 'gospel_statistics/index.html', context=context)

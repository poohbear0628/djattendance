# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.shortcuts import render
from django.views.generic.edit import DeleteView
from django.views.generic import TemplateView
from django.http import HttpResponse

from .models import GospelStat
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
    if Term.current_term().startdate_of_week(i) <= date.today() and Term.current_term().enddate_of_week(i) >= date.today():
      return i

#In Progress
def GospelStatisticsView(request):
  current_user = request.user
  context = {
    'team' : current_user.team,
    'page_title' : 'Team Statistics',
    'gospel_partners' : current_user.firstname+' '+current_user.lastname,
    'cols' : attributes,
    'week' : get_week(),
  }

  '''
  stats = GospelStat.objects.filter(team=current_user.team)
  ctx = {'Tracts_Distributed': 0}
  for i in stats:
    ctx['Tracts_Distributed']+=i.tracts_distributed
  for i in ctx:
    context[i]=ctx[i]
  '''

  return render(request, 'gospel_statistics/gospel_statistics.html', context=context)

def GospelStatisticsSave(request):
  current_user = request.user
  context = {
    'team' : current_user.team,
    'page_title' : 'Team Statistics',
    'gospel_partners' : current_user.firstname+' '+current_user.lastname,
    'cols' : attributes,
    'week' : get_week(),
  }

  '''
  currentStat = GospelStat(team=current_user.team,week=context['week'],tracts_distributed=1)
  currentStat.save()
  for trainee in Trainee.objects.filter(firstname=current_user.firstname,lastname=current_user.lastname):
    print trainee
    currentStat.trainees.add(trainee)

  stats = GospelStat.objects.filter(team=current_user.team)
  ctx = {'Tracts_Distributed': 0}
  for i in stats:
    ctx['Tracts_Distributed']+=i.tracts_distributed
  for i in ctx:
    context[i]=ctx[i]
  '''

  return render(request, 'gospel_statistics/gospel_statistics.html', context=context)

def new_pair(request):
  context =  {
    'page_title': 'New Gospel Pair'
  }
  return render(request, 'gospel_statistics/new_pair.html',context=context)

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

#In Progress
def TAGospelStatisticsView(request):
  context = {
    'page_title': 'TA Gospel Statistics',
  }
  return render(request, 'gospel_statistics/index.html', context=context)

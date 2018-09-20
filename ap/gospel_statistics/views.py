# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.edit import DeleteView
from django.views.generic import TemplateView

from .models import GospelStat
from terms.models import Term

from datetime import *

from braces.views import GroupRequiredMixin

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
    'cols' : ['Tracts Distributed'],
    'week' : get_week(),
  }
  return render(request, 'gospel_statistics/gospel_statistics.html', context=context)

def GospelStatisticsSave(request):
  current_user = request.user
  context = {
    'team' : current_user.team,
    'page_title' : 'Team Statistics',
    'gospel_partners' : current_user.firstname+' '+current_user.lastname,
    'cols' : ['Tracts Distributed'],
    'week' : 15,
  }
  return render(request, 'gospel_statistics/gospel_statistics.html', context=context)

#In Progress
def TAGospelStatisticsView(request):
  context = {
    'page_title': 'TA Gospel Statistics',
  }
  return render(request, 'gospel_statistics/index.html', context=context)

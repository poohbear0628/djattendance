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
attributes = ['Tracts Distributed','Bibles Distributed','Contacted (30 sec)','Led to Pray','Baptized','2nd Appointment','Regular Appointment','Minutes on the Gospel','Minutes in Appointment','Bible Study','Small Groups','District Meeting (New Student)','Conference']
_attributes = ['tracts_distributed','bibles_distributed','contacted_30_sec','led_to_pray','baptized','2nd_appointment','regular_appointment','minutes_on_the_gospel','minutes_in_appointment', 'bible_study','small_groups','district_meeting_new_student','conference']
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

  @staticmethod
  def get_stats_dict(gospel_pairs, gospel_statistics):
    data = []
    entry = dict()
    num = 0
    for p in gospel_pairs:
      entry = dict()
      entry['gospel_pair'] = p
      stat = gospel_statistics.filter(gospelpair=p, week=get_week())
      for i in range(len(_attributes)):
        entry[_attributes[i]]=num
      data.append(entry)
    return data

  def post(self, request, *args, **kwargs):
    #Do we need this?
    context = self.get_context_data()
    #Retreive the updated stat values
    list_of_pairs = request.POST.getlist('pairs')
    list_of_stats = request.POST.getlist('inputs')
    current_week = get_week()
    for i in range(len(list_of_pairs)):
      index = i*13
      pair = GospelPair.objects.filter(id=list_of_pairs[index])
      stat = GospelStat.objects.filter(gospelpair=pair, week=current_week)[0]
      stat.tracts_distributed = list_of_stats[index]
      stat.bibles_distributed = list_of_stats[index+1]
      stat.contacted_30_sec = list_of_stats[index+2]
      stat.led_to_pray = list_of_stats[index+3]
      stat.baptized = list_of_stats[index+4]
      stat.second_appointment = list_of_stats[index+5]
      stat.regular_appointment = list_of_stats[index+6]
      stat.minutes_on_gospel = list_of_stats[index+7]
      stat.minutes_in_appointment = list_of_stats[index+8]
      stat.bible_study = list_of_stats[index+9]
      stat.small_group = list_of_stats[index+10]
      stat.district_meeting = list_of_stats[index+11]
      stat.conference = list_of_stats[index+12]
      stat.save()
    return redirect(reverse('gospel_statistics:gospel-statistics-view'))
    

  def get_context_data(self, **kwargs):
    current_user = self.request.user
    context = super(GospelStatisticsView, self).get_context_data(**kwargs)
    context['page_title'] = 'Team Statistics'
    context['team'] = current_user.team
    context['gospel_pairs'] = GospelPair.objects.filter(team=current_user.team, term=Term.current_term())
    context['cols'] = attributes
    context['week'] = get_week()
    context['current'] = []
    context['atts'] = _attributes
    #Current week stat
    context['current'] = self.get_stats_dict(context['gospel_pairs'],GospelStat.objects.filter(gospelpair__in=context['gospel_pairs']))
    return context

class NewGospelPairView(TemplateView):
  template_name = "gospel_statistics/new_pair.html"

  def post(self, request, *args, **kwargs):
    #Do we need this?
    context = self.get_context_data()
    #Retrieve the selected trainees
    list_of_trainee_id = request.POST.getlist('inputs')
    list_of_trainees = []
    for each in list_of_trainee_id:
      list_of_trainees.extend(Trainee.objects.filter(id=each))
    #Create a new empty gospel pair
    gospelpair = GospelPair(team=context['team'], term=Term.current_term())
    gospelpair.save()
    #Add the trainees
    for each in list_of_trainees:
      gospelpair.trainees.add(each)
    #Check for duplicate
    for each in GospelPair.objects.filter(team=context['team'], term=Term.current_term()):
      ##Need to add an alert
      if each.id is not gospelpair.id and set(each.trainees.all()) == set(gospelpair.trainees.all()):
        gospelpair.delete()
        return redirect(reverse('gospel_statistics:gospel-statistics-view'))
    #Create 20 week GospelStats for the new gospelpair
    for week in range(0,21):
      GospelStat(gospelpair=gospelpair, week=week).save()
    return redirect(reverse('gospel_statistics:gospel-statistics-view'))

  def get_context_data(self, **kwargs):
    current_user = self.request.user
    context = super(NewGospelPairView, self).get_context_data(**kwargs)
    context['page_title'] = 'New Gospel Pair'
    context['team'] = current_user.team
    context['members'] = Trainee.objects.filter(team=current_user.team)
    return context

def weekly_statistics(request):
  current_week = get_week()
  current_team = request.user.team
  stats = GospelStat.objects.filter(week=current_week)
  weekly_stats = []
  gps = []
  #Get all existing gospel pairs
  return HttpResponse(json.dumps(weekly_stats))

#In Progress (change to class)
def TAGospelStatisticsView(request):
  context = {
    'page_title': 'TA Gospel Statistics',
  }
  return render(request, 'gospel_statistics/index.html', context=context)

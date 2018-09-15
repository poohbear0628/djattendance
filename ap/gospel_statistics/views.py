# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView

from braces.views import GroupRequiredMixin

#In Progress
class GospelStatisticsView(TemplateView):
  template_name = 'gospel_statistics/gospel_statistics.html'

  def get_context_data(self, **kwargs):
    ctx = super(GospelStatisticsView, self).get_context_data(**kwargs)
    ctx['team'] = 'University of California Riverside'
    ctx['page_title'] = 'Team Statistics'
    ctx['gospel_partners'] = 'You'
    ctx['cols'] = ['Tracts Distributed','Bibles Distributed','Contacted (>30 sec)','Led to Pray','Baptized','2nd Appointment','Regular Appointment','Minutes on the Gospel','Bible Study','Small Groups','District Meeting (New Student)','Conference']
    ctx['week'] = 15
    return ctx

  def post(self, request, **kwargs):
    update = {}
    if request.POST.get('tracts_distributed'):
      update['tracts_distributed'] = json.loads(request.POST.get('events'))

    super(GoseplStatisticsView, self).post(request, **kwargs)
    return HttpResponse('ok')

#In Progress
def TAGospelStatisticsView(request):
  context = {
    'page_title': 'TA Gospel Statistics',
  }
  return render(request, 'gospel_statistics/index.html', context=context)

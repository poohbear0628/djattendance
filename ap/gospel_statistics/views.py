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
    ctx['page_title'] = 'Gospel Statistics'
    return ctx

#In Progress
def TAGospelStatisticsView(request):
  context = {
    'page_title': 'TA Gospel Statistics',
  }
  return render(request, 'gospel_statistics/index.html', context=context)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
  context = {
    'page_title': 'Gospel Statistics',
  }
  return render(request, 'gospel_statistics/index.html', context=context)

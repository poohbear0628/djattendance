from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .utils import av_dir
from .models import AVFile
from terms.models import Term

class AVHome(generic.ListView):
  model = AVFile
  def dispatch(self, request, *args, **kwargs):
    week = self.kwargs.get('week', None)
    if not week:
      week = Term.current_term().term_week_of_date(date.today())
    self.week = week
    return super(AVHome, self).dispatch(request, *args, **kwargs)

  def get_queryset(self):
    return AVFile.filter_by_week(self.week)

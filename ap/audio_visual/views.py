from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .utils import av_dir
from .models import AVFile
from terms.models import Term

class AVHome(generic.ListView):
  model = AVFile
  template_name = 'audio_visual/avfile_list.html'

  def dispatch(self, request, week=None, *args, **kwargs):
    if not week:
      week = Term.current_term().term_week_of_date(date.today())
    self.week = int(week)
    return super(AVHome, self).dispatch(request, *args, **kwargs)

  def get_queryset(self):
    return AVFile.objects.filter_week(self.week)

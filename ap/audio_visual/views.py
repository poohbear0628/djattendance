from datetime import date
import json
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
    term = Term.current_term()
    current_week = term.term_week_of_date(date.today())
    if not week:
      week = current_week
    self.week = int(week)
    date_format = '%m/%d/%Y'
    self.weeks = json.dumps(map(
                        lambda w: {
                          'id': w,
                          'text': 'Week {0}: {1} - {2}'.format(w,
                              term.startdate_of_week(w).strftime(date_format),
                              term.enddate_of_week(w).strftime(date_format))},
                        range(current_week + 1)))
    return super(AVHome, self).dispatch(request, *args, **kwargs)

  def get_queryset(self):
    return AVFile.objects.filter_week(self.week)

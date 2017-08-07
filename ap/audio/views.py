from datetime import date
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from rest_framework_bulk import (
  BulkModelViewSet,
)

from .models import AudioFile, AudioRequest
from .serializers import AudioRequestSerializer
from .forms import AudioRequestForm
from terms.models import Term

class AudioHome(generic.ListView):
  model = AudioFile
  template_name = 'audio/audiofile_list.html'

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
    return super(AudioHome, self).dispatch(request, *args, **kwargs)

  def get_queryset(self):
    return AudioFile.objects.filter_week(self.week)

class AudioRequestCreate(generic.CreateView):
  model = AudioFile
  template_name = 'requests/request_form.html'
  form_class = AudioRequestForm

class AudioRequestViewSet(BulkModelViewSet):
  queryset = AudioRequest.objects.all()
  serializer_class = AudioRequestSerializer

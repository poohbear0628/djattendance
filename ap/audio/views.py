from datetime import date, datetime
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from rest_framework_bulk import (
  BulkModelViewSet,
)

from .models import AudioFile, AudioRequest
from .serializers import AudioRequestSerializer
from .forms import AudioRequestForm
from terms.models import Term
from aputils.trainee_utils import is_TA, trainee_from_user

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
          'text': 'Week {0}: {1} - {2}'.format(
              w,
              term.startdate_of_week(w).strftime(date_format),
              term.enddate_of_week(w).strftime(date_format)
          )
        }, range(current_week + 1)
    ))
    return super(AudioHome, self).dispatch(request, *args, **kwargs)

  def get_queryset(self):
    files = AudioFile.objects.filter_week(self.week)
    trainee = trainee_from_user(self.request.user)
    attendance_record = trainee.get_attendance_record()
    excused_events = filter(lambda r: r['attendance'] == 'E', attendance_record)
    for f in files:
      f.request = f.audio_requests.filter(trainee_author=trainee).first()
      f.has_leaveslip = False
      for record in excused_events:
        d = datetime.strptime(record['start'].split('T')[0], '%Y-%m-%d').date()
        if record['event'] == f.event and d == f.date:
          f.has_leaveslip = True
      f.can_download = f.has_leaveslip or f.request.status == 'A'
    return files

class AudioRequestCreate(generic.CreateView):
  model = AudioRequest
  template_name = 'requests/request_form.html'
  form_class = AudioRequestForm
  success_url = reverse_lazy('audio:audio-home')

  def form_valid(self, form):
    req = form.save(commit=False)
    req.trainee_author = trainee_from_user(self.request.user)
    req.save()
    return super(AudioRequestCreate, self).form_valid(form)

class AudioRequestUpdate(generic.UpdateView):
  model = AudioRequest
  template_name = 'requests/request_form.html'
  form_class = AudioRequestForm

class AudioRequestViewSet(BulkModelViewSet):
  queryset = AudioRequest.objects.all()
  serializer_class = AudioRequestSerializer

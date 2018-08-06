import json
import os
from datetime import date
from itertools import chain

from aputils.trainee_utils import trainee_from_user, is_trainee
from aputils.utils import modify_model_status
from braces.views import GroupRequiredMixin
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.forms import ValidationError
from django.http import HttpResponseBadRequest, JsonResponse
from django.views import generic
from rest_framework_bulk import BulkModelViewSet
from terms.models import Term

from .forms import AudioRequestForm, AudioRequestTACommentForm
from .models import AudioFile, AudioRequest, fs, valid_audiofile_name
from .serializers import AudioRequestSerializer


def import_audiofiles():
  term_folder = settings.AUDIO_FILES_ROOT
  if not os.path.exists(term_folder):
    return
  files = os.listdir(term_folder)
  imported = set([a.audio_file.name for a in AudioFile.objects.all()])
  for f in files:
    if fs.get_valid_name(f) in imported or not valid_audiofile_name(f):
      continue
    audio = AudioFile()
    try:
      audio.audio_file.name = fs.get_valid_name(f)
      audio.save()
    except ValidationError:
      pass


class AudioHome(generic.ListView):
  model = AudioFile
  template_name = 'audio/audiofile_list.html'

  def dispatch(self, request, week=None, *args, **kwargs):
    import_audiofiles()
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
    trainee = trainee_from_user(self.request.user)
    files = AudioFile.objects.filter_list(self.week, trainee)
    attendance_record = trainee.attendance_record
    for f in files:
      # replace methods with computed values because trainee can't be passed in template
      f.classnotes = f.classnotes(trainee)
      f.request = f.request(trainee)
      f.has_leaveslip = f.has_leaveslip(trainee, attendance_record)
      f.can_download = f.can_download(f.request, f.has_leaveslip)
    return files


class TAAudioHome(generic.ListView):
  model = AudioRequest
  template_name = 'audio/audio_request_list.html'

  def get_queryset(self):
    qs = AudioRequest.objects.filter_term(Term.current_term())
    qs = qs.filter(status='P') | qs.filter(status='F')
    return qs.order_by('date_requested')

  def get_context_data(self, **kwargs):
    context = super(TAAudioHome, self).get_context_data(**kwargs)
    audio_requests = AudioRequest.objects.none()
    reqs = AudioRequest.objects.filter_term(Term.current_term()).order_by('date_requested')
    for status in ['P', 'F', 'A', 'D']:
      audio_requests = chain(audio_requests, reqs.filter(status=status))
    context['audio_requests'] = audio_requests
    return context


class TAComment(GroupRequiredMixin, generic.UpdateView):
  model = AudioRequest
  template_name = 'requests/ta_comments.html'
  form_class = AudioRequestTACommentForm
  group_required = ['training_assistant']
  raise_exception = True
  success_url = reverse_lazy('audio:ta-audio-home')

  def get_context_data(self, **kwargs):
    context = super(TAComment, self).get_context_data(**kwargs)
    context['item_name'] = AudioRequest._meta.verbose_name
    context['request'] = self.get_object()
    return context


modify_status = modify_model_status(AudioRequest, reverse_lazy('audio:ta-audio-home'))


class AudioRequestCreate(generic.CreateView):
  model = AudioRequest
  template_name = 'requests/request_form.html'
  form_class = AudioRequestForm
  success_url = reverse_lazy('audio:audio-home')

  def get_form_kwargs(self):
    kwargs = super(AudioRequestCreate, self).get_form_kwargs()
    kwargs.update({'user': self.request.user})
    return kwargs

  def form_valid(self, form):
    req = form.save(commit=False)
    req.trainee_author = trainee_from_user(self.request.user)
    req.save()
    return super(AudioRequestCreate, self).form_valid(form)


class AudioCreate(generic.CreateView):
  template_name = 'audio/audiofile_upload.html'
  model = AudioFile
  fields = []

  def post(self, request):
    uploaded = request.FILES['file']
    audio_file = AudioFile(audio_file=uploaded)
    try:
      audio_file.save()
      return JsonResponse({'status': 'ok'})
    except ValidationError:
      return HttpResponseBadRequest('File name format incorrect.')


class AudioRequestUpdate(AudioRequestCreate, generic.UpdateView):
  def get_context_data(self, **kwargs):
    context = super(AudioRequestUpdate, self).get_context_data(**kwargs)
    if is_trainee(self.request.user):
      if context['form'].instance.status in ['D', 'A']:
        context['read_only'] = True
    return context


class AudioRequestViewSet(BulkModelViewSet):
  queryset = AudioRequest.objects.all()
  serializer_class = AudioRequestSerializer

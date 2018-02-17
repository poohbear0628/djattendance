from datetime import date
import json
import re
from django.http import JsonResponse, HttpResponseBadRequest
from django.views import generic
from django.core.urlresolvers import reverse_lazy

from braces.views import GroupRequiredMixin
from rest_framework_bulk import (
    BulkModelViewSet,
)

from .models import AudioFile, AudioRequest, AUDIO_FILE_FORMAT, PRETRAINING_FORMAT
from .serializers import AudioRequestSerializer
from .forms import AudioRequestForm, AudioRequestTACommentForm
from terms.models import Term
from aputils.trainee_utils import trainee_from_user
from aputils.utils import modify_model_status


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
    for f in files:
      # replace methods with computed values because trainee can't be passed in template
      f.classnotes = f.classnotes(trainee)
      f.request = f.request(trainee)
      f.can_download = f.can_download(trainee)
      f.has_leaveslip = f.has_leaveslip(trainee)
    return files


class TAAudioHome(generic.ListView):
  model = AudioRequest
  template_name = 'requests/request_list.html'

  def get_queryset(self):
    return AudioRequest.objects.filter_term(Term.current_term())


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
    fname = uploaded.name
    if re.match(AUDIO_FILE_FORMAT, fname) or re.match(PRETRAINING_FORMAT, fname):
      audio_file.save()
      return JsonResponse({'status': 'ok'})
    else:
      return HttpResponseBadRequest('File name format incorrect.')


class AudioRequestUpdate(AudioRequestCreate, generic.UpdateView):
  pass


class AudioRequestViewSet(BulkModelViewSet):
  queryset = AudioRequest.objects.all()
  serializer_class = AudioRequestSerializer

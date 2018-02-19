from django import forms

from aputils.trainee_utils import is_TA
from .models import AudioRequest


class AudioRequestForm(forms.ModelForm):
  class Meta:
    model = AudioRequest

    fields = (
        'trainee_comments',
        'audio_requested',
        'TA_comments'
    )

    labels = {
        'trainee_comments': 'Please describe the reason for your request in detail.',
    }

  def __init__(self, *args, **kwargs):
    self.user = kwargs.pop('user')
    super(AudioRequestForm, self).__init__(*args, **kwargs)
    self.fields['audio_requested'].label_from_instance = lambda obj: "%s" % obj.get_full_name()
    if not is_TA(self.user):
      self.fields['TA_comments'].disabled = True


class AudioRequestTACommentForm(forms.ModelForm):
  class Meta:
    model = AudioRequest
    fields = ['TA_comments']

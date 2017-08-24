from django import forms

from .models import AudioRequest

class AudioRequestForm(forms.ModelForm):
  class Meta:
    model = AudioRequest

    fields = (
      'trainee_comments',
      'audio_requested',
    )

    labels = {
      'trainee_comments': 'Please describe the reason for your request in detail.',
    }

  def __init__(self, *args, **kwargs):
    super(AudioRequestForm, self).__init__(*args, **kwargs)
    self.fields['audio_requested'].label_from_instance = lambda obj: "%s" % obj.get_full_name()

class AudioRequestTACommentForm(forms.ModelForm):
  class Meta:
    model = AudioRequest
    fields = ['TA_comments']

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

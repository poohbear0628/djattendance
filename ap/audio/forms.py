from django import forms

from .models import AudioRequest

class AudioRequestForm(forms.ModelForm):
  class Meta:
    model = AudioRequest
    fields = (
        'trainee_comments',
        'audio_requested',
    )

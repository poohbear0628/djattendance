from django import forms

from .models import MaintenanceRequest, FramingRequest


class MaintenanceRequestForm(forms.ModelForm):
  class Meta:
    model = MaintenanceRequest
    fields = ['house', 'request_type', 'description', 'room', 'urgent']
    labels = {
        'description': 'Please describe the problem in detail.',
    }


class FramingRequestForm(forms.ModelForm):
  class Meta:
    model = FramingRequest
    fields = ['house', 'location', 'frame', 'approved', 'frame_already_there']
    labels = {
        'location': 'Location: Please be descriptive, such as "in living room over fireplace" or "above right dresser in bedroom".',
        'frame_already_there': 'Is there a frame there already?',
        'frame': 'Desired quote to be in frame: Must be a verse, footnote, ministry quote, or hymn AND must have verbal approval from a TA brother. Or, if a frame is there already, what to fix.',
        'approved': 'TA brother approved'
    }

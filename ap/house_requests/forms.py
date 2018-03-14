from django import forms
from django.db.models import Q

from aputils.trainee_utils import is_TA

from houses.models import House
from .models import MaintenanceRequest, FramingRequest


class MaintenanceRequestForm(forms.ModelForm):
  class Meta:
    model = MaintenanceRequest
    fields = ['house', 'request_type', 'description', 'room', 'urgent']
    labels = {
        'description': 'Please describe the problem in detail.',
        'house': 'House/Location',
    }

  def __init__(self, user=None, *args, **kwargs):
    super(MaintenanceRequestForm, self).__init__(*args, **kwargs)
    if user.current_term > 2 and user.groups.filter(name='facility_maintenance').exists() or is_TA(user):
      self.fields['house'].queryset = House.objects.all()
    elif user and user.groups.filter(name='HC').exists():
      self.fields['house'].queryset = House.objects.filter(Q(pk=user.house.id) | Q(name__in=('MCC', 'TC')))
    else:
      self.fields['house'].queryset = House.objects.filter(name__in=('MCC', 'TC'))




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

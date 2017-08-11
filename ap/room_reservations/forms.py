from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import RoomReservation
from aputils.widgets import SelectTimeWidget, DatePicker

from datetime import datetime, timedelta

class RoomReservationForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(RoomReservationForm, self).__init__(*args, **kwargs)
    self.fields['start'].widget = SelectTimeWidget(twelve_hr=True, use_seconds=False, minute_step=30, required=True)
    self.fields['end'].widget = SelectTimeWidget(twelve_hr=True, use_seconds=False, minute_step=30, required=True)

    # These fields are required for clean to be called
    req_keys = ['group', 'date', 'start', 'end', 'room', 'group_size', 'frequency', 'reason']
    for key in req_keys:
    self.fields[key].required = True

  def clean(self):
    date = self.cleaned_data['date']
    start = self.cleaned_data['start']
    end = self.cleaned_data['end']

    #Only requests with 24 hour notice
    start_dt = datetime.combine(date, start)
    diff = start_dt - datetime.now()
    if diff.seconds > 83699:
    raise ValidationError(_('Request must be made 24 hours in advance'))

    #End must be after start
    if end <= start:
    raise ValidationError(_('End time must be after start time'))

    return self.cleaned_data

  class Meta:
    model = RoomReservation
    fields = ['group', 'date', 'start', 'end', 'room', 'group_size', 'frequency', 'reason']
    widgets = {
      'date': DatePicker(),
    }

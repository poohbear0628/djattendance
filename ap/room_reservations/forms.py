from django import forms
from django.forms.widgets import HiddenInput

from .models import RoomReservation
from aputils.widgets import DatePicker


class RoomReservationForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(RoomReservationForm, self).__init__(*args, **kwargs)

    # These fields are required for clean to be called
    req_keys = ['group', 'date', 'start', 'end', 'room', 'group_size', 'frequency', 'reason']
    for key in req_keys:
      self.fields[key].required = True

    hidden_keys = ['date', 'start', 'end', 'room']
    for key in hidden_keys:
      self.fields[key].widget = HiddenInput()

    self.fields['group'].widget.attrs['placeholder'] = 'Group making reservation (will be displayed on TV)'

  class Meta:
    model = RoomReservation
    fields = ['group', 'date', 'start', 'end', 'room', 'group_size', 'frequency', 'reason']
    widgets = {
        'date': DatePicker(),
    }

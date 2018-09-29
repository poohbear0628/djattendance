from django import forms

from .models import RoomReservation
from aputils.widgets import TimePicker, DatePicker
from aputils.trainee_utils import is_TA


class RoomReservationForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    user = kwargs.pop('user', None)
    super(RoomReservationForm, self).__init__(*args, **kwargs)

    # These fields are required for clean to be called
    req_keys = ['group', 'date', 'start', 'end', 'room', 'frequency', 'reason']
    for key in req_keys:
      self.fields[key].required = True

    if is_TA(user):
      self.fields['reason'].required = False;

    self.fields['group'].widget.attrs['placeholder'] = 'Group making reservation (will be displayed on TV)'
    self.fields['start'].widget = TimePicker()
    self.fields['end'].widget = TimePicker()
    self.fields['date'].widget = DatePicker()

  class Meta:
    model = RoomReservation
    fields = ['group', 'date', 'start', 'end', 'room', 'frequency', 'reason']

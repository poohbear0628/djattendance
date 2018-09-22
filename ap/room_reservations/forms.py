from django import forms
from django.core.serializers import serialize

from .models import RoomReservation
from aputils.widgets import TimePicker, DatePicker
import datetime
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

  def clean(self):
    cleaned_data = self.cleaned_data
    data_date = cleaned_data['date']
    data_start = cleaned_data['start']
    data_end = cleaned_data['end']
    data_room = cleaned_data['room']

    # pull Room Reservation data
    RoomReservations = RoomReservation.objects.filter(status='A')

    # if the cleaned (date, start, end, room) already exists inside RR data, raise something
    for r in RoomReservations:
      r_data = r.__dict__

      if data_start == data_end:
        raise forms.ValidationError("Start and end time shouldn't be the same.")

      if data_start > data_end: 
        raise forms.ValidationError("Start time should not be after the end time.")

      current_time = datetime.datetime.now().time()
      current_date = datetime.date.today()

      #No need to check end time b/c of the check above.
      if current_date >= data_date and current_time > data_start:
          raise forms.ValidationError("The given reservation is being made in the past.")

      if not r_data['room_id'] == data_room and r_data['date'] == data_date and (r_data['end'] >= data_start and r_data['start'] <= data_end):
        raise forms.ValidationError("Re-check the given start and end times. There is an overlap with an already approved room.")


    return cleaned_data
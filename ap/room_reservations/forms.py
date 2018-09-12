from django import forms
from django.core.serializers import serialize

from .models import RoomReservation
from aputils.widgets import TimePicker, DatePicker


class RoomReservationForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(RoomReservationForm, self).__init__(*args, **kwargs)

    # These fields are required for clean to be called
    req_keys = ['group', 'date', 'start', 'end', 'room', 'frequency', 'reason']
    for key in req_keys:
      self.fields[key].required = True

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
    print "hello!!"
    print data_date
    print data_start
    print data_end
    print data_room
    print "yellow!!"

    for r in RoomReservations:
      r_data = r.__dict__

      # input a check that ensures Trainee is not making a reservation for a given date before today.

      if r_data['start'] > r_data['end']:
        raise forms.ValidationError("Start time should not be after the end time.")

      if not r_data['room_id'] == data_room and (r_data['end'] >= data_start and r_data['start'] <= data_end):
        raise forms.ValidationError("Re-check the given start and end times. There is an overlap with given times.")


    return cleaned_data
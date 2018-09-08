from django import forms

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

    ## if the (date, start, end, room) already exists inside RR data, raise something
      # first check if it's the same date, o(1) check. should eliminate a subsequent checks
        # note to self, check that photo of the logic to check time




    return cleaned_data
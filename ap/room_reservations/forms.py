from django import forms
from django.core.serializers import serialize

import datetime
from .models import RoomReservation
from aputils.widgets import TimePicker, DatePicker
from terms.models import Term
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
    data_frequency = cleaned_data['frequency']

    # If the cleaned data (from django - the inputted data when a user tries to make a new room reservation)
    # is not valid then raise an error.
    if not Term.current_term().is_date_within_term(data_date):
      raise forms.ValidationError("Given date is not a valid date within the term.")

    if data_start == data_end:
      raise forms.ValidationError("Given start and end times should not be the same.")

    if data_start > data_end: 
      raise forms.ValidationError("Given start time should not be after the end time.")

    current_time = datetime.datetime.now().time()
    todays_date = datetime.date.today()
    if data_date <= todays_date and data_start < current_time:
        raise forms.ValidationError("The given reservation is being made in the past.")

   
    # In order to check if an approved room reservation (ARR) overlaps with the new room reservation (NRR):
    # If the ARR[room_id] == the NRR[room_id], and if the ARR's time overlaps with the NRR's time,
      # then compare the dates of the ARR and NRR. Making note to 'frequency' being 'once' or 'term'  
    # We can always assume that NRR is being made today or in the future because of a check above ensuring NRR is never in the past.

    # pull Approved Room Reservations data
    ApprovedRoomReservations = RoomReservation.objects.filter(status='A')

    for ARR in ApprovedRoomReservations:
      ARR = r.__dict__ # approved room reservations
      # need explicit str because ARR['room_id'] is <type 'unicode'>, data_room is <class 'rooms.models.Room'>
      if str(ARR['room_id']) == str(data_room) and ARR['end'] >= data_start and ARR['start'] <= data_end:
        # if the 'frequency' of the ARR is 'once', we consider if the ARR data is from the past, today, or future
        #   in the past, ignore it because that ARR data is irrelevant to a NRR.
        if str(ARR['frequency']) == 'once':
          if ARR['date'] < current_date:
            continue

          # else the AAR first occurence is today -
          elif ARR['date'] == current_date:
            # No need to check if NRR is 'once' or 'term'. Whether the NRR is once or term, because today overlaps, raise an error.
            raise forms.ValidationError("Re-check the date of the start and end times. There is an overlap with an already approved room reservation.")

          #therefore we are in the future
          elif ARR['date'] > current_date:
            if str(data_frequency) == 'once':
              continue
            #else it's NRR frequency is term, the new data inputted will conflict with the ARR
            raise forms.ValidationError("Re-check the date of the start and end times. There is an overlap with an already approved room reservation.")

        # else if the frequency of ARR is 'term', we still consider past, today, or future.
        # if they are on the same weekday in the past, then have already having known that the times overlap, raise an error
        elif str(ARR['frequency']) == 'term':
          if ARR['date'].weekday() == data_date.weekday():
           
            if ARR['date'] > current_date:
              continue
            raise forms.ValidationError("Re-check the date of the start and end times. There is an overlap with an already approved room reservation.")



          #   if ARR['date'] < current_date:
          #     raise forms.ValidationError("Re-check the date of the start and end times. There is an overlap with an already approved room reservation.")



          #   if ARR['date'].weekday() == data_date.weekday():
          #     raise forms.ValidationError("Re-check the date of the start and end times. There is an overlap with an already approved room reservation.")
          # elif ARR['date'] == current_date:
          #   raise an error b/c whether NRR is once or term, it always conflicts


          # elif ARR['date'] > current_date:
          #   if NRR is once, it ok

          #   else raise an errorrrrr cuz it'll conflict with the ARR eventually




          # else if str(data_frequency) == 'term':
          #   raise forms.ValidationError("Re-check the date of the start and end times. There is an overlap with an already approved room reservation.")


        # # if the frequency of ARR is 'term', compare the weekday
        # # if they are on the same weekday, then have already having known that the times overlap, raise an error
        # if str(ARR['frequency']) == 'term':
        #   if ARR['date'].weekday() == data_date.weekday():
        #     raise forms.ValidationError("Re-check the date of the start and end times. There is an overlap with an already approved room reservation.")

    return cleaned_data
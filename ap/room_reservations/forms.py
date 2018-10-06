from django import forms

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


    """
    In order to check if an approved room reservation (ARR) overlaps with the new room reservation (NRR):

    If the ARR[room_id] == the NRR[room_id], and if the ARR's time overlaps with the NRR's time,
    and if ARR.weekday() == data_date.weekday() ~note: this is needed for 'Term' checks because 'date' only gives first occurence of the RR~
      then compare the dates of the ARR and NRR. Making note with 'frequency' being 'Once' or 'Term'

    We can always assume that NRR is being made today or in the future because of a check above ensuring NRR is never in the past.

    Pseudo-logic for checking the Approved Room Reservations:

    if ARR['frequency'] == 'Once'
      if ARR['date'] < data_data, whether NRR is 'Once' or 'Term' having ARR['date'] there will never be an overlap.
      if ARR['date'] == data_date, raise an error regardless if NRR is 'Once' or 'Term' because they both overlap.
      if ARR['date'] > data_date, raise an error if NRR is 'Term' because NRR would eventually overlap. 'Once' would be ok.

    if ARR['frequency'] == 'Term'
      if ARR['date'] < data_data, raise an error regardless if NRR is 'Once' or 'Term' because ARR will eventually overlap
      if ARR['date'] == data_date, raise an error regardless if NRR is 'Once' or 'Term' because they both overlap
      if ARR['date'] > data_date, raise an error if NRR is 'Term' because NRR will eventually overlap. 'Once' would be ok.
    """

    ApprovedRoomReservations = RoomReservation.objects.filter(status='A', room=data_room) # pull Approved Room Reservations data
    for r in ApprovedRoomReservations:
      # ARR = r.__dict__
      # explicit str because ARR['room_id'] is <type 'unicode'>, data_room is <class 'rooms.models.Room'>
      #if str(ARR['room_id']) == str(data_room) and ARR['end'] > data_start and ARR['start'] < data_end and ARR['date'].weekday() == data_date.weekday():
      if r.end > data_start and r.start < data_end and r.date.weekday() == data_date.weekday(): 
        if r.frequency == 'Once' and r.date < data_date:
            continue
        if r.date > data_date and data_frequency == 'Once':
          continue
        raise forms.ValidationError("Re-check the date of the start and end times. There is an overlap with an already approved room reservation.")

    # # new code, review over it and test it.
    # # seems to not work functionally on some test cases - check github for example 1381/rr_doublebookfix
    # ApprovedRoomReservations = RoomReservation.objects.filter(status='A', room=data_room, date__lte=data_date) # pull Approved Room Reservations data
    # if ApprovedRoomReservations.exists():
    #   potential_reservation = [res for res in ApprovedRoomReservations.filter(frequency='Term') if res.date.weekday == data_date.weekday]
    #   potential_reservation += list(ApprovedRoomReservations.filter(frequency='Once'))
    #   if len(potential_reservation) > 0:
    #     for reservation in potential_reservation:
    #       if (reservation.start <= data_start <= reservation.end) or (data_start <= reservation.start <= data_end):
    #         raise forms.ValidationError("Re-check the date of the start and end times. There is an overlap with an already approved room reservation.")
    return cleaned_data
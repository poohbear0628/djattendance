from aputils.widgets import DatePicker, DatetimePicker
from django import forms
from .models import Destination


class OverseerForm(forms.Form):
  gospel_trip = None

  def __init__(self, *args, **kwargs):
    if 'gospel_trip__pk' in kwargs:
      self.gospel_trip = kwargs.pop('gospel_trip__pk')
    super(OverseerForm, self).__init__(*args, **kwargs)

  firstname = forms.ChoiceField()
  lastname = forms.ChoiceField()
  gender = forms.ChoiceField()
  locality = forms.ChoiceField()

  desination1 = forms.ModelChoiceField(
    queryset=Destination.objects.filter(gospel_trip=gospel_trip)
  )
  comments1 = forms.CharField()

  desination2 = forms.ModelChoiceField(
    queryset=Destination.objects.filter(gospel_trip=gospel_trip)
  )

  comments2 = forms.CharField()

  desination3 = forms.ModelChoiceField(
    queryset=Destination.objects.filter(gospel_trip=gospel_trip)
  )

  comments3 = forms.CharField()

  desination4 = forms.ModelChoiceField(
    queryset=Destination.objects.filter(gospel_trip=gospel_trip)
  )

  comments4 = forms.CharField()

  desination5 = forms.ModelChoiceField(
    queryset=Destination.objects.filter(gospel_trip=gospel_trip)
  )

  comments5 = forms.CharField()

  flight_comments = forms.CharField()

  general_comments = forms.CharField()


class PassportForm(forms.Form):
  def __init__(self, *args, **kwargs):
    super(PassportForm, self).__init__(*args, **kwargs)

  passport_firstname = forms.CharField()

  passport_middlename = forms.CharField()

  passport_lastname = forms.CharField()

  citizenship = forms.CharField()

  expiration_date = forms.DateField(widget=DatePicker())

  passport_number = forms.CharField()


class FlightForm(forms.Form):
  def __init__(self, *args, **kwargs):
    super(FlightForm, self).__init__(*args, **kwargs)

  number = forms.CharField()

  airline = forms.CharField()

  departure_airport = forms.CharField()

  departure_datetime = forms.DateTimeField(widget=DatetimePicker())

  arrival_airport = forms.CharField()

  arrival_datetime = forms.DateTimeField(widget=DatetimePicker())

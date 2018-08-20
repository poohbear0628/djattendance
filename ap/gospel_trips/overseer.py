from aputils.widgets import DatePicker, DatetimePicker
from django import forms
from .models import Destination


class OverseerForm(forms.Form):

  firstname = forms.CharField()
  lastname = forms.CharField()
  gender = forms.ChoiceField()
  locality = forms.CharField()

  desination1 = forms.ModelChoiceField(
    queryset=Destination.objects.none()
  )
  comments1 = forms.CharField()

  desination2 = forms.ModelChoiceField(
    queryset=Destination.objects.none()
  )

  comments2 = forms.CharField()

  desination3 = forms.ModelChoiceField(
    queryset=Destination.objects.none()
  )

  comments3 = forms.CharField()

  desination4 = forms.ModelChoiceField(
    queryset=Destination.objects.none()
  )

  comments4 = forms.CharField()

  desination5 = forms.ModelChoiceField(
    queryset=Destination.objects.none()
  )

  comments5 = forms.CharField()

  flight_comments = forms.CharField()

  general_comments = forms.CharField()

  def __init__(self, *args, **kwargs):
    if 'gospel_trip__pk' in kwargs:
      gospel_trip = kwargs.pop('gospel_trip__pk')
    super(OverseerForm, self).__init__(*args, **kwargs)
    qs = Destination.objects.filter(gospel_trip=gospel_trip)
    self.fields['desination1'].queryset = qs
    self.fields['desination2'].queryset = qs
    self.fields['desination3'].queryset = qs
    self.fields['desination4'].queryset = qs
    self.fields['desination5'].queryset = qs


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

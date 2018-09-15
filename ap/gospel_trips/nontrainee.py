from aputils.widgets import DatePicker, DatetimePicker
from django import forms
from django.forms import formset_factory

from .models import Destination


class ApplicationForm(forms.Form):

  destination1 = forms.ModelChoiceField(
    queryset=Destination.objects.none()
  )
  comments1 = forms.CharField(required=False)

  destination2 = forms.ModelChoiceField(
    queryset=Destination.objects.none()
  )

  comments2 = forms.CharField(required=False)

  destination3 = forms.ModelChoiceField(
    queryset=Destination.objects.none()
  )

  comments3 = forms.CharField(required=False)

  flight_comments = forms.CharField(required=False)

  general_comments = forms.CharField(required=False)

  def __init__(self, *args, **kwargs):
    if 'gospel_trip__pk' in kwargs:
      gospel_trip = kwargs.pop('gospel_trip__pk')
    super(ApplicationForm, self).__init__(*args, **kwargs)
    qs = Destination.objects.filter(gospel_trip=gospel_trip)
    self.fields['destination1'].queryset = qs
    self.fields['destination2'].queryset = qs
    self.fields['destination3'].queryset = qs


class PassportForm(forms.Form):
  def __init__(self, *args, **kwargs):
    super(PassportForm, self).__init__(*args, **kwargs)

  passport_firstname = forms.CharField(required=False)

  passport_middlename = forms.CharField(required=False)

  passport_lastname = forms.CharField(required=False)

  citizenship = forms.CharField(required=False)

  expiration_date = forms.DateField(widget=DatePicker(), required=False)

  passport_number = forms.CharField(required=False)


class FlightForm(forms.Form):
  def __init__(self, *args, **kwargs):
    super(FlightForm, self).__init__(*args, **kwargs)

  choices = [('INO', 'International Outbound'),
             ('INR', 'International Return'),
             ('IMO', 'Intermediate Outbound'),
             (('IMR', 'Intermediate Return'))]

  flight_type = forms.ChoiceField(choices=choices)

  number = forms.CharField(required=False)

  airline = forms.CharField(required=False)

  departure_airport = forms.CharField(required=False)

  departure_datetime = forms.DateTimeField(widget=DatetimePicker(), required=False)

  arrival_airport = forms.CharField(required=False)

  arrival_datetime = forms.DateTimeField(widget=DatetimePicker(), required=False)


FlightFormSet = formset_factory(FlightForm)

from django import forms
from bootstrap3_datetime.widgets import DateTimePicker
from django_select2 import *

from .models import Event, Schedule
from accounts.models import Trainee
from schedules.constants import WEEKDAYS


class EventForm(forms.ModelForm):
  active_trainees = Trainee.objects.select_related().filter(is_active=True)
  trainees = ModelSelect2MultipleField(queryset=active_trainees, required=False, search_fields=['^first_name', '^last_name'])

  class Meta:
    model = Event
    fields = ('type', 'name', 'code', 'description', 'monitor', 'start', 'end', 'day', 'weekday')
    widgets = { 'start': DateTimePicker(options={'format': 'MM/DD/YYYY HH:mm'}),
          'end': DateTimePicker(options={'format': 'MM/DD/YYYY HH:mm'}) }

  repeat = forms.MultipleChoiceField(choices=WEEKDAYS, help_text="Which days this event repeats on")
  duration = forms.IntegerField(help_text="How many weeks this event repeats for")
  active_trainees = Trainee.objects.filter(is_active=True)
  trainees = ModelSelect2MultipleField(queryset=active_trainees, required=False, search_fields=['^first_name', '^last_name'])

  class Meta:
    model = Event
    fields = ('type', 'name', 'code', 'description', 'monitor', 'start', 'end', 'day', 'weekday')
    help_texts = {
      'start': 'Set the date to the first occurrence of the event',
      'end': 'Set the date to the first occurrence of the event',
    }
    widgets = { 'start': DateTimePicker(options={'format': 'MM/DD/YYYY HH:mm'}),
          'end': DateTimePicker(options={'format': 'MM/DD/YYYY HH:mm'}) }

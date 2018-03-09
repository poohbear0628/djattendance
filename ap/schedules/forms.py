from django import forms

from django.contrib.admin.widgets import FilteredSelectMultiple
from django_select2.forms import ModelSelect2MultipleWidget
from aputils.custom_fields import CSIMultipleChoiceField

from terms.models import Term
from accounts.widgets import TraineeSelect2MultipleInput
from accounts.models import Trainee

from .models import Event, Schedule


class EventForm(forms.ModelForm):
  schedules = forms.ModelMultipleChoiceField(
    label='Schedules',
    queryset=Schedule.objects.all(),
    required=False,
    widget=FilteredSelectMultiple("schedules", is_stacked=False))

  class Meta:
    model = Event
    exclude = []
    widgets = {
      'schedules': FilteredSelectMultiple("schedules", is_stacked=False),
    }


class ScheduleForm(forms.ModelForm):
  events = forms.ModelMultipleChoiceField(
    label='Events',
    queryset=Event.objects.all(),
    required=False,
    widget=FilteredSelectMultiple(
      "events", is_stacked=False))

  weeks = CSIMultipleChoiceField(
    initial='0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19',
    choices=Term.all_weeks_choices(),
    required=False,
    label='Weeks')

  trainees = forms.ModelMultipleChoiceField(
    queryset=Trainee.objects.all(),
    label='Participating Trainees',
    required=False,
    widget=TraineeSelect2MultipleInput,
  )

  def save(self, commit=True):
    instance = super(ScheduleForm, self).save(commit=False)
    weeks = self.cleaned_data['weeks'].split(',') # etc
    if len(weeks) > 1:
      weeks.sort(key=int)
    instance.weeks = ','.join(weeks)
    if commit:
        instance.save()
    return instance

  def __init__(self, *args, **kwargs):
    super(ScheduleForm, self).__init__(*args, **kwargs)
    self.fields['trainees'].widget.attrs = {'style':'width:100%'}

  class Meta:
    model = Schedule
    exclude = []

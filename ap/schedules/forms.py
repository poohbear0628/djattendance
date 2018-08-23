from accounts.models import Trainee
from accounts.widgets import TraineeSelect2MultipleInput
from aputils.custom_fields import CSIMultipleChoiceField
from django import forms
from django.utils.translation import ugettext as _
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.shortcuts import redirect

from terms.models import Term
from attendance.models import Roll

from .models import Event, Schedule
from .utils import validate_rolls


class EventForm(forms.ModelForm):
  schedules = forms.ModelMultipleChoiceField(
    label='Schedules',
    queryset=Schedule.objects.all(),
    required=False,
    widget=FilteredSelectMultiple("schedules", is_stacked=False))

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    self.fields['type'].widget.attrs['class'] = 'select-fk'
    self.fields['class_type'].widget.attrs['class'] = 'select-fk'
    self.fields['monitor'].widget.attrs['class'] = 'select-fk'
    self.fields['weekday'].widget.attrs['class'] = 'select-fk'
    self.fields['chart'].widget.attrs['class'] = 'select-fk'

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

  # trainees, events, priority and weeks will provide query parameters for rolls that needs to be reconciled
  # prior to allowing this schedule change to take place
  def clean(self):
    obj_id = self.instance.id
    data = self.cleaned_data
    weeks = set([int(i) for i in data['weeks'].split(',')])
    trainees = data['trainees']
    priority = data['priority']
    total_invalid_rolls = []
    print 'called clean'

    for t in trainees:
      check_schedules = []
      potential_schedules = t.active_schedules.filter(priority__lte=priority)
      if obj_id:
        potential_schedules = potential_schedules.exclude(id=obj_id)
      for s in potential_schedules:
        if len(weeks.intersection(set([int(i) for i in s.weeks.split(',')]))) > 0:
          check_schedules.append(s)

        # print 'checking schedules'
        # print check_schedules
      check_schedules.append(self.instance)
      check_schedules = sorted(check_schedules, key=lambda sch: sch.priority)
      rolls = validate_rolls(t, weeks, check_schedules)

      total_invalid_rolls.extend(rolls)

    error_rolls = []
    for i in total_invalid_rolls:
      roll = Roll.objects.get(pk=i)
      error_rolls.append(roll)

    if len(total_invalid_rolls) > 0:
      raise ValidationError(error_rolls)

    else:
      return self.cleaned_data


  def save(self, commit=True):
    trainees_cleaned = self.cleaned_data['trainees']
    events_cleaned = self.cleaned_data['events']
    weeks = self.cleaned_data['weeks'].split(',')  # etc

    instance = super(ScheduleForm, self).save(commit=False)

    if len(weeks) > 1:
      weeks.sort(key=int)
    instance.weeks = ','.join(weeks)

    if commit:
      instance.save()  # save before M2M can be used
      instance.trainees.set(trainees_cleaned)
      instance.events.set(events_cleaned)

    return instance

  def __init__(self, *args, **kwargs):
    super(ScheduleForm, self).__init__(*args, **kwargs)
    self.fields['trainees'].widget.attrs['class'] = 'select-fk'
    self.fields['parent_schedule'].widget.attrs['class'] = 'select-fk'
    self.fields['term'].widget.attrs['class'] = 'select-fk'
    self.fields['query_filter'].widget.attrs['class'] = 'select-fk'

  class Meta:
    model = Schedule
    exclude = []

class AfternoonClassForm(forms.Form):

  afternoon_classes = list(Event.objects.filter(class_type='AFTN', weekday=3, monitor='AM').values_list('code', 'name').order_by('name'))
  afternoon_classes.insert(0, ('', '---'))

  trainees = forms.ModelMultipleChoiceField(
    queryset=Trainee.objects.all(),
    label='Trainees',
    required=True,
    widget=TraineeSelect2MultipleInput,
  )

  event = forms.ChoiceField(
    choices=afternoon_classes,
    required=True,
    label='transfer to'
  )

  week = forms.IntegerField(
    max_value=18,
    min_value=1,
    required=True,
    label='starting from week'
  )

  def __init__(self, *args, **kwargs):
    super(AfternoonClassForm, self).__init__(*args, **kwargs)
    self.fields['trainees'].widget.attrs['class'] = 'select-fk'
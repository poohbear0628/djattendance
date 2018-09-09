from accounts.models import Trainee
from accounts.widgets import TraineeSelect2MultipleInput
from aputils.custom_fields import CSIMultipleChoiceField

from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.core.exceptions import ValidationError

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

#   # trainees, events, priority and weeks will provide query parameters for rolls that needs to be reconciled
#   # prior to allowing this schedule change to take place
#   def clean(self):
#     obj_id = self.instance.id
#     data = self.cleaned_data
#     weeks = set([int(i) for i in data['weeks'].split(',')])
#     trainees = data['trainees']
#     priority = data['priority']
#     total_invalid_rolls = []
#     print 'called clean'

#     for t in trainees:
#       check_schedules = []
#       potential_schedules = t.active_schedules.filter(priority__lte=priority)
#       if obj_id:
#         potential_schedules = potential_schedules.exclude(id=obj_id)
#       for s in potential_schedules:
#         if len(weeks.intersection(set([int(i) for i in s.weeks.split(',')]))) > 0:
#           check_schedules.append(s)

#         # print 'checking schedules'
#         # print check_schedules
#       check_schedules.append(self.instance)
#       check_schedules = sorted(check_schedules, key=lambda sch: sch.priority)
#       rolls = validate_rolls(t, weeks, check_schedules)

#       total_invalid_rolls.extend(rolls)

#     error_rolls = []
#     for i in total_invalid_rolls:
#       roll = Roll.objects.get(pk=i)
#       error_rolls.append(roll)

#     if len(total_invalid_rolls) > 0:
#       raise ValidationError(error_rolls)

#     else:
#       return self.cleaned_data


class BaseScheduleForm(forms.ModelForm):
  events = forms.ModelMultipleChoiceField(
    label='Events',
    queryset=Event.objects.all(),
    required=False,
    widget=FilteredSelectMultiple(
      "events", is_stacked=False)
  )

  weeks = CSIMultipleChoiceField(
    initial='1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18',
    choices=Term.all_weeks_choices(),
    required=False,
    label='Weeks'
  )

  trainees = forms.ModelMultipleChoiceField(
    queryset=Trainee.objects.all(),
    label='Participating Trainees',
    required=False,
    widget=TraineeSelect2MultipleInput,
  )


  def __init__(self, *args, **kwargs):
    super(BaseScheduleForm, self).__init__(*args, **kwargs)
    self.fields['trainees'].widget.attrs['class'] = 'select-fk'
    self.fields['parent_schedule'].widget.attrs['class'] = 'select-fk'
    self.fields['term'].widget.attrs['class'] = 'select-fk'
    self.fields['term'].initial = Term.objects.get(current=True)
    self.fields['query_filter'].widget.attrs['class'] = 'select-fk'

  def save(self, *args, **kwargs):
    self.clean()
    return super(BaseScheduleForm, self).save(*args, **kwargs)

  class Meta:
    model = Schedule
    exclude = []

class CreateScheduleForm(BaseScheduleForm):

  def clean(self):
    data = self.cleaned_data
    trainees = data['trainees']
    interested_schedules = Schedule.objects.filter(trainees__in=trainees).exclude(priority__gt=int(data['priority'])).exclude(trainee_select='GP').distinct()
    interested_eventsList = list(interested_schedules.values('events__id', 'events__start', 'events__end', 'events__weekday'))
    events = data['events']
    events_weekday = set(events.values_list('weekday', flat=True))
    event_ids = []

    for ev in interested_eventsList:
      if ev['events__weekday'] in events_weekday:
        for event in events:
          if event.start <= ev['events__start'] <= event.end or event.start <= ev['events__end'] <= event.end:
            event_ids.append(ev['events__id'])
            break

    weeks = data['weeks']
    weeks = weeks.split(',')
    current_term = Term.objects.get(current=True)
    start_date = current_term.startdate_of_week(int(weeks[0]))
    end_date = current_term.enddate_of_week(int(weeks[-1]))
    rolls = Roll.objects.filter(trainee__in=trainees, event__id__in=event_ids, date__range=[start_date, end_date]).values_list('id', flat=True)
    if rolls.exists():
      raise ValidationError('%(rolls)s', code='invalidRolls', params={'rolls': list(rolls)})

    return self.cleaned_data

class UpdateScheduleForm(BaseScheduleForm):

  def clean(self):
    data = self.cleaned_data


    return self.cleaned_data

class AfternoonClassForm(forms.Form):

  trainees = forms.ModelMultipleChoiceField(
    queryset=Trainee.objects.all(),
    label='Trainees',
    required=True,
    widget=TraineeSelect2MultipleInput,
  )

  event = forms.ChoiceField(
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
    event_choices = kwargs.pop('event_choices')
    super(AfternoonClassForm, self).__init__(*args, **kwargs)
    self.fields['event'].choices = event_choices
    self.fields['trainees'].widget.attrs['class'] = 'select-fk'
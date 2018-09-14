from accounts.models import Trainee
from accounts.widgets import TraineeSelect2MultipleInput
from aputils.custom_fields import CSIMultipleChoiceField
from aputils.eventutils import EventUtils

from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.core.exceptions import ValidationError
from copy import deepcopy

from terms.models import Term
from attendance.models import Roll

from .models import Event, Schedule
from .utils import validate_rolls, schedule_rolls


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
          if event.start <= ev['events__start'] <= ev['events__end'] <= event.end:
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

# small hack for delete, we're giving two buttons to the same form and instead of using DeleteView
# we'll be using the same framework for rendering rolls deletion for both update and delete
class UpdateScheduleForm(BaseScheduleForm):

  def clean(self):
    rolls = Roll.objects.none()

    if 'update' in self.data:
      data = self.cleaned_data
      roll_ids = []

      if 'weeks' in self.changed_data:
        changed_weeks = data['weeks'].split(',')
        initial_weeks = self.initial['weeks']
        min_val = min(changed_weeks[0], initial_weeks[0])
        max_val = max(changed_weeks[-1], initial_weeks[-1]) + 1
        weeks = range(min_val, max_val)
      else:
        weeks = range(0, 20)

      t_set = set(data['trainees'])
      if 'trainees' in self.changed_data:
        t_set = set(self.initial['trainees']) | t_set

      schedules = Schedule.get_all_schedules_in_weeks_for_trainees(weeks, t_set)
      schedules = list(schedules.exclude(id=self.instance.id))

      new_schedule_instance = deepcopy(self.instance)
      new_schedule_instance.trainees = data['trainees']
      new_schedule_instance.events = data['events']
      new_schedule_instance.priority = data['priority']
      new_schedule_instance.weeks = data['weeks']
      schedules.append(new_schedule_instance)
      w_tb = EventUtils.collapse_priority_event_trainee_table(weeks, schedules, t_set)

      events = set(data['events'])
      if 'events' in self.changed_data:
        events = set(self.initial['events']) | events

      events_to_check = set()
      for ev in events:
        potential_conflicts = Event.objects.filter(weekday=ev.weekday)
        for pc in potential_conflicts:
          if pc.start <= ev.start <= ev.end <= pc.end:
            events_to_check.update([pc])

      events = events | events_to_check
      trainee_rolls = Roll.objects.filter(trainee__in=t_set, event__in=events)

      for r in trainee_rolls:
        key = Term.objects.get(current=True).reverse_date(r.date)
        evs = w_tb[key]
        if r.event not in evs or (r.event in evs and r.trainee not in evs[r.event] ):
          roll_ids.append(r.id)

      rolls = Roll.objects.filter(id__in=roll_ids).values_list('id', flat=True)

    elif 'delete' in self.data:
      schedule_id = self.instance.id
      schedule = Schedule.objects.get(pk=schedule_id)
      rolls = schedule_rolls(schedule)
      rolls = rolls.values_list('id', flat=True)

    if rolls.exists():
      raise ValidationError('%(rolls)s', code='invalidRolls', params={'rolls': list(rolls)})

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
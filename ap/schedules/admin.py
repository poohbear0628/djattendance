from django import forms
from django.contrib import admin
from schedules.models import *
from .models import Event, Schedule

from django.contrib.admin.widgets import FilteredSelectMultiple
from django_select2.forms import ModelSelect2MultipleWidget

from aputils.admin_utils import FilteredSelectMixin
from aputils.custom_fields import CSIMultipleChoiceField

from terms.models import Term

class EventForm(forms.ModelForm):
  schedules = forms.ModelMultipleChoiceField(
    label='Schedules',
    queryset=Schedule.objects.all(),
    required=False,
    widget=admin.widgets.FilteredSelectMultiple(
      "schedules", is_stacked=False))

  class Meta:
    model = Event
    exclude = []
    widgets = {
    'schedules': admin.widgets.FilteredSelectMultiple(
      "schedules", is_stacked=False),
    }


class EventAdmin(FilteredSelectMixin, admin.ModelAdmin):
  form = EventForm
  registered_filtered_select = [('schedules', Schedule), ]
  save_as = True
  list_display = ("name", "code", "description", "type", "start", "end", "day", "weekday", "chart")




class ScheduleForm(forms.ModelForm):
  trainees = ModelSelect2MultipleWidget(
    label='Participating Trainees',
    queryset=Trainee.objects.all().only('firstname', 'lastname', 'email'),
    required=False)

  events = forms.ModelMultipleChoiceField(
    label='Events',
    queryset=Event.objects.all(),
    required=False,
    widget=admin.widgets.FilteredSelectMultiple(
      "events", is_stacked=False))

  weeks = CSIMultipleChoiceField(initial='0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19', choices=Term.all_weeks_choices(), required=False, label='Weeks')

  def save(self, commit=True):
    instance = super(ScheduleForm, self).save(commit=False)
    weeks = self.cleaned_data['weeks'].split(',') # etc
    if len(weeks) > 1:
      weeks.sort(key=int)
    instance.weeks = ','.join(weeks)
    if commit:
        instance.save()
    return instance

  class Meta:
    model = Schedule
    exclude = []
    widgets = {
    'trainees': admin.widgets.FilteredSelectMultiple(
      "trainees", is_stacked=False),
    }


# Works without mixin b/c relationship is explicitly defined
class ScheduleAdmin(admin.ModelAdmin):
  form = ScheduleForm
  save_as = True
  list_display = ("name", "comments", "priority", "term", "season", "weeks", "is_deleted")
  registered_filtered_select = [('trainees', Trainee), ('events', Event)]
  # filter_horizontal = ("weeks",)

admin.site.register(Event, EventAdmin)
admin.site.register(Schedule, ScheduleAdmin)

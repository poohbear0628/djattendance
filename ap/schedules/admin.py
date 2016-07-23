from django import forms
from django.contrib import admin
from schedules.models import *
from .models import Event, Schedule, Class

class ClassAdmin(admin.ModelAdmin):
  exclude = ['type']

  # Automatically type class event objects saved.
  def save_model(self, request, obj, form, change):
      obj.type = 'C'
      obj.save()


class EventAdmin(admin.ModelAdmin):
  save_as = True
  list_display = ("name", "code", "description", "type", "start", "end", "day", "weekday", "chart")


class ScheduleForm(forms.ModelForm):
  trainees = forms.ModelMultipleChoiceField(
    label='Participating Trainees',
    queryset=Trainee.objects.all().only('firstname', 'lastname', 'email'),
    required=False,
    widget=admin.widgets.FilteredSelectMultiple(
      "trainees", is_stacked=False))

  events = forms.ModelMultipleChoiceField(
    label='Events',
    queryset=Event.objects.all(),
    required=False,
    widget=admin.widgets.FilteredSelectMultiple(
      "events", is_stacked=False))

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


admin.site.register(Event, EventAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Class, ClassAdmin)
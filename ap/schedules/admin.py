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
    list_display = ("name", "description", "type", "start", "end", "day", "weekday", "chart")

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ("name", "comments", "priority", "term", "season", "weeks", "is_deleted")

admin.site.register(Event, EventAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Class, ClassAdmin)
from django.contrib import admin
from schedules.models import *
from .models import Event, Schedule, Class

admin.site.register(Event)
admin.site.register(Schedule)
admin.site.register(Class)
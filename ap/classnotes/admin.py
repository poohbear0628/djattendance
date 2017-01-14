from django.contrib import admin
from .models import Classnotes, Classnotes_Tracker

class ClassnotesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'trainee','classname','classdate')

class Classnotes_TrackerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'trainee','classnotes_owed','absence_counts')

# Register your models here.
admin.site.register(Classnotes, ClassnotesAdmin)
admin.site.register(Classnotes_Tracker, Classnotes_TrackerAdmin)

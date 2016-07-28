from django import forms
from django.contrib import admin
from .models import Class
from schedules.models import Schedule

from aputils.admin_utils import FilteredSelectMixin


class ClassForm(forms.ModelForm):
  schedules = forms.ModelMultipleChoiceField(
    label='Schedules',
    queryset=Schedule.objects.all(),
    required=False,
    widget=admin.widgets.FilteredSelectMultiple(
      "schedules", is_stacked=False))

  class Meta:
    model = Class
    exclude = []
    widgets = {
    'schedules': admin.widgets.FilteredSelectMultiple(
      "schedules", is_stacked=False),
    }


class ClassAdmin(FilteredSelectMixin, admin.ModelAdmin):
  exclude = ['type']
  form = ClassForm
  registered_filtered_select = [('schedules', Schedule), ]
  save_as = True
  list_display = ("name", "code", "description", "type", "start", "end", "day", "weekday", "chart")

  # Automatically type class event objects saved.
  def save_model(self, request, obj, form, change):
      obj.type = 'C'
      obj.save()

# class ClassAdmin(admin.ModelAdmin):
#     exclude = ['type']

#     # Automatically type class event objects saved.
#     def save_model(self, request, obj, form, change):
#         obj.type = 'C'
#         obj.save()

#admin.site.register(Class)
admin.site.register(Class, ClassAdmin)
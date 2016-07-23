from django import forms
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse

from accounts.models import Trainee
from houses.models import House, Room, Bunk
from aputils.models import Address
from aputils.admin_utils import FilteredSelectMixin


class HouseForm(forms.ModelForm):
  residents = forms.ModelMultipleChoiceField(
    label='Residents',
    queryset=Trainee.objects.all(),
    required=False,
    widget=admin.widgets.FilteredSelectMultiple(
      "trainees", is_stacked=False))

  class Meta:
    model = House
    fields = ['name', 'address', 'gender', 'used', ]
    widgets = {
    'trainees': admin.widgets.FilteredSelectMultiple(
      "trainees", is_stacked=False),
    }


class HouseAdmin(FilteredSelectMixin, ModelAdmin):
  form = HouseForm
  registered_filtered_select = [('residents', Trainee), ]

  list_display = ['name', 'address', 'gender', 'used', 'residents_list', ]
  ordering = ['name', ]




admin.site.register(House, HouseAdmin)
admin.site.register(Room)
admin.site.register(Bunk)

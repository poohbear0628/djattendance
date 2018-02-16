from django import forms
from django.contrib import admin

from django_select2.forms import ModelSelect2Widget

from .models import Roll, Trainee, Event


class RollAdminForm(forms.ModelForm):
  event = forms.ModelChoiceField(
      label="Event",
      queryset=Event.objects.all(),
      required=True,
      widget=ModelSelect2Widget(
          queryset=Event.objects.all(),
          required=True,
          search_fields=['name__icontains', 'weekday__icontains'],
      )
  )

  trainee = forms.ModelChoiceField(
      label="Trainee",
      queryset=Trainee.objects.all(),
      required=True,
      widget=ModelSelect2Widget(
          queryset=Trainee.objects.all(),
          required=True,
          search_fields=['firstname__icontains', 'lastname__icontains'],
      )
  )

  submitted_by = forms.ModelChoiceField(
      label="Submitted by",
      queryset=Trainee.objects.filter(is_active=True),
      required=True,
      widget=ModelSelect2Widget(
          queryset=Trainee.objects.filter(is_active=True),
          required=True,
          search_fields=['firstname__icontains', 'lastname__icontains'],
      )
  )

  def __init__(self, *args, **kwargs):
    self.user = kwargs.pop('user', None)
    super(RollAdminForm, self).__init__(*args, **kwargs)
    self.initial['Submitted by'] = self.user


class RollAdmin(admin.ModelAdmin):
  list_display = ('date', 'event', 'trainee', 'status', 'finalized')
  list_filter = ('date', 'event__name', 'status')
  ordering = ('date', 'event', 'trainee')
  search_fields = ('trainee__firstname', 'trainee__lastname', 'event__name', 'status', 'date')
  form = RollAdminForm


admin.site.register(Roll, RollAdmin)

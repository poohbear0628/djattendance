from django import forms
from django.contrib import admin
from django_select2.forms import ModelSelect2Widget, ModelSelect2MultipleWidget

from .models import Roll, Trainee, Event
from accounts.widgets import TraineeSelect2MultipleInput


class RollAdminForm(forms.ModelForm):
  class Meta:
    fields = ['event', 'trainee', 'status', 'finalized', 'date', 'notes', 'submitted_by']
    model = Roll

  event = forms.ModelMultipleChoiceField(
      label="Event",
      queryset=Event.objects.all(),
      required=True,
      widget=ModelSelect2MultipleWidget(
          queryset=Event.objects.all(),
          required=True,
          search_fields=['name__icontains', 'weekday__icontains'],
      )
  )

  trainee = forms.ModelMultipleChoiceField(
      queryset=Trainee.objects.all(),
      label='Trainee(s)',
      required=False,
      widget=TraineeSelect2MultipleInput(attrs={'id': 'id_trainees'}),
  )

  submitted_by = forms.ModelChoiceField(
      label="",
      queryset=Trainee.objects.filter(is_active=True),
      required=False,
      widget=forms.HiddenInput,
  )

  def save(self, commit=True):
    print(self.cleaned_data)
    return 


class RollAdmin(admin.ModelAdmin):
  list_display = ('date', 'event', 'status', 'finalized')
  list_filter = ('date', 'event__name', 'status')
  ordering = ('date', 'event')
  search_fields = ('trainee__firstname', 'trainee__lastname', 'event__name', 'event__weekday', 'status', 'date')
  form = RollAdminForm


admin.site.register(Roll, RollAdmin)

from django import forms
from django.contrib import admin
from schedules.models import *
from .models import Roll

from django.contrib.admin.widgets import FilteredSelectMultiple
from django_select2.forms import ModelSelect2MultipleWidget

from aputils.admin_utils import FilteredSelectMixin
from aputils.custom_fields import CSIMultipleChoiceField

from terms.models import Term
from accounts.widgets import TraineeSelect2MultipleInput, EventSelect2MultipleInput

class RollForm(forms.ModelForm):
  event = forms.ModelChoiceField(
    queryset=Event.objects.all(),
    label='Events',
    required=False,
    widget=EventSelect2MultipleInput,
    )

  trainee = forms.ModelChoiceField(
    queryset=Trainee.objects.all(),
    label='Participating Trainees',
    required=False,
    widget=TraineeSelect2MultipleInput,
    )

  def save(self, commit=True):
    instance = super(RollForm, self).save(commit=False)
    if commit:
        instance.save()
    return instance

  def __init__(self, *args, **kwargs):
    super(RollForm, self).__init__(*args, **kwargs)
    self.fields['trainee'].widget.attrs = {'style':'width:100%'}
    self.fields['event'].widget.attrs = {'style':'width:100%'}

  class Meta:
    model = Roll
    exclude = []

# Works without mixin b/c relationship is explicitly defined
class RollAdmin(admin.ModelAdmin):
  form = RollForm
  save_as = True
  list_display = ("status", "finalized", "notes", "submitted_by", "date")
  registered_filtered_select = [('trainee', Trainee), ('event', Event)]

admin.site.register(Roll, RollAdmin)

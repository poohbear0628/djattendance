from django import forms

from django.contrib.admin.widgets import FilteredSelectMultiple
from accounts.widgets import TraineeSelect2MultipleInput
from django_select2.forms import ModelSelect2MultipleWidget
from .models import IndividualSlip, GroupSlip
from accounts.models import Trainee
from services.models import Assignment
from suit.widgets import AutosizedTextarea

# TODO support events


class LeaveslipForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(LeaveslipForm, self).__init__(*args, **kwargs)
    self.fields['description'].widget.attrs['readonly'] = True
    self.fields['type'].label = 'Reason'
    self.fields['TA'].label = 'TA Assigned to this leave slip'

class IndividualSlipForm(LeaveslipForm):
  def __init__(self, *args, **kwargs):
    super(IndividualSlipForm, self).__init__(*args, **kwargs)
    self.fields['trainee'].widget.attrs['readonly'] = True

  class Meta:
    model = IndividualSlip
    fields = ['trainee', 'type', 'description', 'private_TA_comments', 'comments', 'TA']
    widgets = {
      'description': AutosizedTextarea,
      'comments': AutosizedTextarea,
      'private_TA_comments': AutosizedTextarea,
    }

class GroupSlipForm(forms.ModelForm):
  trainees = forms.ModelMultipleChoiceField(
      queryset=Trainee.objects.all(),
      required=True,
      widget=ModelSelect2MultipleWidget(model=Trainee),
  )

  def __init__(self, *args, **kwargs):
    super(GroupSlipForm, self).__init__(*args, **kwargs)
    self.fields['start'].widget.attrs['readonly'] = True
    self.fields['end'].widget.attrs['readonly'] = True

  class Meta:
    model = GroupSlip
    fields = ['trainees', 'type', 'description', 'private_TA_comments', 'comments', 'start', 'end']
    widgets = {
      'description': AutosizedTextarea,
      'comments': AutosizedTextarea,
      'private_TA_comments': AutosizedTextarea,
    }

class GroupSlipAdminForm(forms.ModelForm):

  trainees = forms.ModelMultipleChoiceField(
    queryset=Trainee.objects.all(),
    label='Trainees',
    required=False,
    widget=TraineeSelect2MultipleInput,
  )

  service_assignment = forms.ModelMultipleChoiceField(
    label='Service Assignment',
    queryset=Assignment.objects.all(),
    required=False,
    widget=FilteredSelectMultiple(
      "service_assignment", is_stacked=True)
  )

  def __init__(self, *args, **kwargs):
    super(GroupSlipAdminForm, self).__init__(*args, **kwargs)
    self.fields['service_assignment'].queryset = Assignment.objects.all().select_related('week_schedule', 'service') 

from django import forms

from django_select2.forms import ModelSelect2MultipleWidget
from .models import IndividualSlip, GroupSlip
from accounts.models import Trainee

# TODO support events


class LeaveslipForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(LeaveslipForm, self).__init__(*args, **kwargs)
    self.fields['type'].label = 'Reason'
    self.fields['TA'].label = 'TA Assigned to this leave slip'
    self.fields['TA_informed'].label = 'TA informed'


class IndividualSlipForm(LeaveslipForm):
  def __init__(self, *args, **kwargs):
    super(IndividualSlipForm, self).__init__(*args, **kwargs)

  class Meta:
    model = IndividualSlip
    fields = ['trainee', 'type', 'description', 'private_TA_comments', 'comments', 'TA_informed', 'TA']


class GroupSlipForm(LeaveslipForm):
  trainees = forms.ModelMultipleChoiceField(
      queryset=Trainee.objects.all(),
      required=True,
      widget=ModelSelect2MultipleWidget(model=Trainee),
  )

  def __init__(self, *args, **kwargs):
    super(GroupSlipForm, self).__init__(*args, **kwargs)

  class Meta:
    model = GroupSlip
    fields = ['trainees', 'type', 'description', 'private_TA_comments', 'comments', 'start', 'end', 'TA_informed', 'TA']

from django import forms

from django_select2.forms import ModelSelect2MultipleField
from .models import IndividualSlip, GroupSlip
from accounts.models import Trainee

# TODO support events


class LeaveslipForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(LeaveslipForm, self).__init__(*args, **kwargs)
    self.fields['description'].widget.attrs['readonly'] = True
    self.fields['informed'].widget.attrs['onclick'] = 'return false;'
    self.fields['texted'].widget.attrs['onclick'] = 'return false;'
    self.fields['TA'].label = 'TA informed'


class IndividualSlipForm(LeaveslipForm):
  def __init__(self, *args, **kwargs):
    super(IndividualSlipForm, self).__init__(*args, **kwargs)
    self.fields['trainee'].widget.attrs['readonly'] = True

  class Meta:
    model = IndividualSlip
    fields = ['trainee', 'type', 'description', 'private_TA_comments', 'comments', 'texted', 'informed', 'TA']


class GroupSlipForm(forms.ModelForm):
  trainees = forms.ModelChoiceField(
      queryset=Trainee.objects.all(),
      required=True,
      widget=Select2MultipleWidget,
  )

  def __init__(self, *args, **kwargs):
    super(GroupSlipForm, self).__init__(*args, **kwargs)
    self.fields['trainees'] = ModelSelect2MultipleField(queryset=Trainee.objects.all(), required=False, search_fields=['^first_name', '^last_name'])
    self.fields['start'].widget.attrs['readonly'] = True
    self.fields['end'].widget.attrs['readonly'] = True

  class Meta:
    model = GroupSlip
    fields = ['trainees', 'type', 'description', 'private_TA_comments', 'comments', 'texted', 'informed', 'start', 'end', 'TA']
    widgets = {
      'trainees': Select2MultipleWidget,
    }

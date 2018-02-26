from django import forms

from django_select2.forms import ModelSelect2MultipleWidget
from .models import IndividualSlip, GroupSlip
from accounts.models import Trainee
from suit.widgets import AutosizedTextarea

# TODO support events


class LeaveslipForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(LeaveslipForm, self).__init__(*args, **kwargs)
    self.fields['description'].widget.attrs['readonly'] = True
    # self.fields['informed'].widget.attrs['onclick'] = 'return false;'
    # self.fields['texted'].widget.attrs['onclick'] = 'return false;'
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


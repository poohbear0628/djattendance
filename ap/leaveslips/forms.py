from django import forms

from django_select2.forms import ModelSelect2Widget, Select2MultipleWidget
from .models import IndividualSlip, GroupSlip
from accounts.models import Trainee
from attendance.models import Roll

#TODO support events

class IndividualSlipForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(IndividualSlipForm, self).__init__(*args, **kwargs)
    self.fields['trainee'].widget.attrs['disabled'] = True
    self.fields['description'].widget.attrs['disabled'] = True

  class Meta:
    model = IndividualSlip
    fields = ['trainee', 'type', 'description', 'comments', 'texted', 'informed', 'TA']

class GroupSlipForm(forms.ModelForm):
  trainees = forms.ModelChoiceField(
    queryset = Trainee.objects.all(),
    required = True,
    widget = Select2MultipleWidget,
  )

  def __init__(self, *args, **kwargs):
    super(GroupSlipForm, self).__init__(*args, **kwargs)
    self.fields['description'].widget.attrs['disabled'] = True

  class Meta:
    model = GroupSlip
    fields = ('trainees', 'description', 'trainee', 'type', 'description', 'comments', 'texted', 'informed', 'TA')
    widgets = {
      'trainees': Select2MultipleWidget,
    }

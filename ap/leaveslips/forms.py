from django import forms

from django_select2 import ModelSelect2MultipleField
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
  class Media:
    css = {
      'all': [
        'bower_components/select2/select2.css',
        'bower_components/select2/select2-bootstrap.css',
      ]
    }
    js = [
      'js/select2-django.js'
    ]

  def __init__(self, *args, **kwargs):
    super(GroupSlipForm, self).__init__(*args, **kwargs)
    self.fields['description'].widget.attrs['disabled'] = True
    self.fields['trainees'] = ModelSelect2MultipleField(queryset=Trainee.objects.all(), required=False, search_fields=['^first_name', '^last_name'])

  class Meta:
    model = GroupSlip
    fields = ['trainees', 'type', 'description', 'comments', 'texted', 'informed', 'start', 'end', 'TA']

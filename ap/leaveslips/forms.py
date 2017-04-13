from django import forms

from django_select2 import ModelSelect2MultipleField
from .models import IndividualSlip, GroupSlip
from accounts.models import Trainee
from attendance.models import Roll

#TODO support events

class IndividualSlipForm(forms.ModelForm):

  class Meta:
    model = IndividualSlip
    fields = ['type', 'description', 'comments', 'texted', 'informed', 'TA']

class GroupSlipForm(forms.ModelForm):
  trainees = ModelSelect2MultipleField(queryset=Trainee.objects.all(), required=False, search_fields=['^first_name', '^last_name'])

  class Meta:
    model = GroupSlip
    fields = ['type', 'description', 'comments', 'texted', 'informed', 'TA', 'start', 'end']

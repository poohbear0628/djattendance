from django import forms

from django_select2.forms import ModelSelect2MultipleWidget
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
    js = [
      'js/select2-django.js'
    ]

  def __init__(self, *args, **kwargs):
    super(GroupSlipForm, self).__init__(*args, **kwargs)
    self.fields['description'].widget.attrs['disabled'] = True
    class Meta:
      model = GroupSlip
      fields = ('trainees', )
      widgets = {
        'trainees' : ModelSelect2MultipleWidget(queryset=Trainee.objects.all(), required=False, search_fields=['lastname__icontains','firstname__icontains'])
      }
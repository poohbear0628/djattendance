from django import forms

from django_select2 import ModelSelect2MultipleField
from .models import IndividualSlip, GroupSlip
from accounts.models import Trainee

#TODO support events

class IndividualSlipForm(forms.ModelForm):
    class Meta:
        model = IndividualSlip
        fields = ['type', 'description', 'texted', 'informed', 'rolls']

class TAIndividualSlipCommentsForm(forms.ModelForm):
    class Meta:
        model = IndividualSlip
        fields = ['comments']

class GroupSlipForm(forms.ModelForm):

    trainees = ModelSelect2MultipleField(queryset=Trainee.objects.all(), required=False, search_fields=['^first_name', '^last_name'])

    class Meta:
        model = GroupSlip
        fields = ['type', 'description', 'comments', 'texted', 'informed', 'start', 'end']

class TAGroupSlipCommentsForm(forms.ModelForm):
    class Meta:
        model = GroupSlip
        fields = ['comments']
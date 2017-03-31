from django import forms

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

    trainees = forms.ModelMultipleChoiceField(queryset=Trainee.objects.select_related().filter(is_active=True))

    class Meta:
        model = GroupSlip
        fields = ['type', 'trainees', 'description', 'comments', 'texted', 'informed', 'start', 'end']


class TAGroupSlipCommentsForm(forms.ModelForm):
    class Meta:
        model = GroupSlip
        fields = ['comments']
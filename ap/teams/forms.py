from django import forms
from django.contrib import admin

from accounts.models import Trainee
from .models import Team


class TeamAdminForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(TeamAdminForm, self).__init__(*args, **kwargs)

  class Meta:
    model = Team
    fields = ['members']
    widgets = {
        'members': admin.widgets.FilteredSelectMultiple("trainees", is_stacked=False),
    }

  members = forms.ModelMultipleChoiceField(
      label='Members',
      queryset=Trainee.objects.all(),
      required=False,
      widget=admin.widgets.FilteredSelectMultiple("trainees", is_stacked=False)
  )

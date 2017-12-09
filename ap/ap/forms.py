from django import forms

from django_select2.forms import Select2MultipleWidget

from accounts.models import User
from teams.models import Team
from houses.models import House
from localities.models import Locality


class TraineeSelectForm(forms.Form):
  TERM_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4')
  )

  term = forms.MultipleChoiceField(
    choices=TERM_CHOICES,
    widget=forms.CheckboxSelectMultiple,
    required=False,
  )
  gender = forms.ChoiceField(
    choices=User.GENDER,
    widget=forms.RadioSelect,
    required=False,
  )
  hc = forms.BooleanField(required=False, label="House coordinators")
  team_type = forms.MultipleChoiceField(
    choices=Team.TEAM_TYPES,
    widget=forms.CheckboxSelectMultiple,
    required=False,
  )
  team = forms.ModelChoiceField(
    queryset=Team.objects.all(),
    required=False,
    widget=Select2MultipleWidget,
  )
  house = forms.ModelChoiceField(
    queryset=House.objects.filter(used=True),
    required=False,
    widget=Select2MultipleWidget,
  )
  locality = forms.ModelChoiceField(
    queryset=Locality.objects.all(),
    required=False,
    widget=Select2MultipleWidget,
  )

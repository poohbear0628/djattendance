from django import forms
from accounts.models import Trainee
from fobi.base import BasePluginForm


class FormAccessForm(forms.Form, BasePluginForm):
  """ Hidden Name form. """

  plugin_data_fields = [
    ("name", "Access"),
    ("label", "Access"),
    ("initial", ""),
    ("help_text", "Ignore this field."),
    ("required", False)
  ]

  TRAINEE_CHOICES = ((-1, 'all'), )
  trainee_qs = Trainee.objects.all()
  for t in trainee_qs:
    TRAINEE_CHOICES += ((t.id, t.full_name), )

  name = forms.CharField(label="Name", required=True)
  label = forms.CharField(label="Label", required=True)
  initial = forms.CharField(
    label="Initial",
    required=False,
    widget=forms.SelectMultiple(choices=TRAINEE_CHOICES)
  )
  required = forms.BooleanField(label="Required", required=False)

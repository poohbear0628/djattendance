from django import forms
from fobi.base import BasePluginForm

from accounts.models import Trainee
from accounts.widgets import TraineeSelect2MultipleInput


class FormAccessForm(forms.Form, BasePluginForm):
  """ Hidden Name form. """

  plugin_data_fields = [
    ("name", "Access"),
    ("label", "Access"),
    ("initial", ""),
    ("help_text", "Ignore this field."),
    ("required", False)
  ]

  name = forms.CharField(label="Name", required=True)
  label = forms.CharField(label="Label", required=True)
  initial = forms.CharField(
    label="Initial",
    required=False,
    widget=TraineeSelect2MultipleInput,
  )
  required = forms.BooleanField(label="Required", required=False)

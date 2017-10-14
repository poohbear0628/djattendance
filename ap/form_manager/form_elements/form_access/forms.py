from django import forms
from fobi.base import BasePluginForm
from form_manager.utils import TRAINEE_CHOICES


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
    widget=forms.SelectMultiple(choices=TRAINEE_CHOICES)
  )
  required = forms.BooleanField(label="Required", required=False)

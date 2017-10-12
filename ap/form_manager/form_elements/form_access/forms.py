from django import forms
from fobi.base import BasePluginForm
from form_manager.utils import TRAINEE_CHOICES
from django.db import models


class FormAccessForm(forms.Form, BasePluginForm):
  """ Hidden Name form. """

  plugin_data_fields = [
    ("name", "Access"),
    ("label", "Access"),
    ("initial", ""),
    ("help_text", "Ignore this field."),
    ("required", True)
  ]

  name = forms.CharField(label="Name", required=True)
  label = forms.CharField(label="Label", required=True)
  initial = forms.CharField(label="Initial", required=False, widget=forms.Select(choices=TRAINEE_CHOICES))
  required = forms.BooleanField(label="Required", required=False)

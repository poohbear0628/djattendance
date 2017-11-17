from django import forms
from fobi.base import BasePluginForm


class NameInputForm(forms.Form, BasePluginForm):
  """ Name Input form. """
  plugin_data_fields = [
      ("name", "NAME"),
      ("label", "NAME"),
      ("initial", ""),
      ("required", True)
  ]

  name = forms.CharField(label="Name", required=True)
  label = forms.CharField(label="Label", required=True)
  initial = forms.CharField(label="Initial", required=False)
  required = forms.BooleanField(label="Required", required=False)

from django import forms
from fobi.base import BasePluginForm, get_theme
from accounts.widgets import TraineeSelect2MultipleInput
from django_select2.forms import Select2MultipleWidget
from accounts.models import Trainee

theme = get_theme(request=None, as_instance=True)

class FormAccessForm(forms.Form, BasePluginForm):
  """ Hidden Name form. """

  plugin_data_fields = [
    ("name", "Access"),
    ("label", "Access"),
    ("initial", ""),
    ("help_text", "Ignore this field."),
    ("required", False)
  ]
  # This important for trainee_select.js
  attrs = {
    'id':'id_trainees',
  }

  initial = forms.ModelMultipleChoiceField(
    queryset=Trainee.objects.all(),
    label="Initial",
    required=False,
    widget=TraineeSelect2MultipleInput(attrs=attrs),
  )

  name = forms.CharField(label="Name", required=False)
  label = forms.CharField(label="Label", required=False)
  help_text = forms.CharField(
    label="Help text",
    required=False,
  )
  required = forms.BooleanField(label="Required", required=False)

  def get_plugin_data(self, request=None, json_format=True):
      """Get plugin data.

      overwrites get_plugin_data()
      see fobi.base for more.
      
      """
      
      qs = self.cleaned_data.get('initial') # QuerySet of Trainees
      ids = []
      if qs:
        for q in qs:
          ids.append(q.id)
      else:
        ids.append[-1]
      self.cleaned_data['initial'] = ids
      self.cleaned_data['name'] = 'Access'
      self.cleaned_data['label'] = 'Access'
      self.cleaned_data['help_text'] = 'Ignore this field.'
      if self.plugin_data_fields:
          return self._get_plugin_data(self.plugin_data_fields,
                                       request=request,
                                       json_format=json_format)

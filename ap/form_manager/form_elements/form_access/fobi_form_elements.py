from django import forms
from accounts.models import Trainee
from fobi.base import FormFieldPlugin, form_element_plugin_registry, get_theme
from form_manager.form_elements.form_access.forms import FormAccessForm

theme = get_theme(request=None, as_instance=True)


class FormAccessPlugin(FormFieldPlugin):
  """Name Field plugin -- autofills with user name if marked as required."""
  uid = "form_access"
  name = "Form Access"
  form = FormAccessForm
  # Group to which the plugin belongs to
  group = "Custom"
  is_hidden = True

  TRAINEE_CHOICES = ((-1, 'all'), )
  trainee_qs = Trainee.objects.all()
  for t in trainee_qs:
    TRAINEE_CHOICES += ((t.id, t.full_name), )

  def get_form_field_instances(self, request=None, form_entry=None, form_element_entries=None, **kwargs):
    attrs = {
      'class': theme.form_element_html_class,
      'readonly': 'readonly',
    }
    kwargs = {
      'required': self.data.required,
      'label': self.data.label,
      'initial': self.data.initial,
      'widget': forms.SelectMultiple(choices=self.TRAINEE_CHOICES, attrs=attrs)
    }
    return [(self.data.name, forms.CharField, kwargs), ]


form_element_plugin_registry.register(FormAccessPlugin)

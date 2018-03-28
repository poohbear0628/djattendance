from django import forms

from accounts.widgets import TraineeSelect2MultipleInput
from graduation.models import *
from aputils.widgets import DatePicker


class GenericModelForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(GenericModelForm, self).__init__(*args, **kwargs)

  class Meta:
    exclude = ['trainee', 'due_date', 'show_status', 'grad_admin', ]


class TestimonyForm(GenericModelForm):

  class Meta(GenericModelForm.Meta):
    model = Testimony


class ConsiderationForm(GenericModelForm):

  class Meta(GenericModelForm.Meta):
    model = Consideration


class WebsiteForm(GenericModelForm):

  class Meta(GenericModelForm.Meta):
    model = Website


class OutlineForm(GenericModelForm):

  class Meta(GenericModelForm.Meta):
    model = Outline


class RemembranceForm(GenericModelForm):

  class Meta(GenericModelForm.Meta):
    model = Remembrance
    widgets = {
        'remembrance_text': forms.TextInput(attrs={'cols': 15, 'rows': 1, 'maxlength': 15}),
        'remembrance_reference': forms.TextInput(attrs={'cols': 10, 'rows': 1, 'maxlength': 5})
    }


class MiscForm(GenericModelForm):

  class Meta(GenericModelForm.Meta):
    model = Misc


class GradAdminForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(GradAdminForm, self).__init__(*args, **kwargs)

  class Meta:
    model = GradAdmin
    exclude = ['term', ]
    widgets = {
        'testimony_due_date': DatePicker(),
        'consideration_due_date': DatePicker(),
        'website_due_date': DatePicker(),
        'outline_due_date': DatePicker(),
        'remembrance_due_date': DatePicker(),
        'misc_due_date': DatePicker(),
        'speaking_trainees': TraineeSelect2MultipleInput(attrs={'id': 'id_trainees'}),
    }

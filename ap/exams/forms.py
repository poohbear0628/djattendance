from django.forms import Form, ModelForm, formset_factory
from django.forms import CharField, Textarea, TextInput
from django.forms.models import inlineformset_factory, BaseInlineFormSet
from django_select2 import ModelSelect2MultipleField

from .models import Exam, Section, Session
from accounts.models import Trainee


class ExamCreateForm(ModelForm):

  def __init__(self, *args, **kwargs):
    super(ExamCreateForm, self).__init__(*args, **kwargs)
    metadata_name_attr = {'name': 'exam_metadata'}
    self.fields['training_class'].widget.attrs = metadata_name_attr
    self.fields['term'].widget.attrs = metadata_name_attr
    self.fields['description'].widget.attrs = metadata_name_attr

  class Meta:
    model = Exam
    fields = ('training_class', 'description', 'is_open', 'duration', 'category', 'term')


class ExamReportForm(ModelForm):
  active_trainees = Trainee.objects.select_related().filter(is_active=True)
  label = 'Trainees whose exams to generate a report for'
  trainee = ModelSelect2MultipleField(queryset=active_trainees, required=False, search_fields=['^last_name', '^first_name'], label=label)

  def __init__(self, *args, **kwargs):
    super(ExamReportForm, self).__init__(*args, **kwargs)
    self.fields['trainee'].widget.attrs = {'class': 'hide-if-in-class', 'id': 'id_trainees'}

  class Meta:
    model = Session
    fields = ('trainee',)

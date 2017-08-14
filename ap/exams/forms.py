from django.forms import Form, ModelForm, formset_factory
from django.forms import CharField, Textarea, TextInput
from django.forms.models import inlineformset_factory, BaseInlineFormSet
from django_select2 import ModelSelect2MultipleField

from .models import Exam, Section, Session
from accounts.models import Trainee

class ExamCreateForm(ModelForm):
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

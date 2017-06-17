from django.forms import Form, ModelForm, formset_factory
from django.forms import CharField, Textarea, TextInput
from django.forms.models import inlineformset_factory, BaseInlineFormSet
from django_select2.forms import ModelSelect2MultipleWidget

from .models import Exam, Section, Session
from accounts.models import Trainee

class ExamCreateForm(ModelForm):
  class Meta:
    model = Exam
    fields = ('training_class', 'description', 'is_open', 'duration', 'category', 'term')

class ExamReportForm(ModelForm):
  def __init__(self, *args, **kwargs):
    super(ExamReportForm, self).__init__(*args, **kwargs)
    self.fields['trainee'].widget.attrs = {'class': 'hide-if-in-class', 'id': 'id_trainees'}

  class Meta:
    model = Session
    fields = ('trainee', )
    active_trainees = Trainee.objects.select_related().filter(is_active=True)
    label = 'Trainees whose exams to generate a report for'
    widgets = {
      'trainee' : ModelSelect2MultipleWidget(queryset=active_trainees, required=False, search_fields=['lastname__icontains', 'firstname__icontains'], label=label)
    }
from django.forms import ModelForm, MultipleChoiceField
from django.forms.models import ModelChoiceField, ModelMultipleChoiceField

from .models import Exam, Section, Session
from accounts.models import Trainee
from accounts.widgets import TraineeSelect2MultipleInput
from classes.models import Class


class ExamCreateForm(ModelForm):
  training_class = ModelChoiceField(Class.objects.all(), empty_label=None)
  class Meta:
    model = Exam
    fields = ('training_class', 'description', 'is_open', 'duration', 'category', 'term')


class ExamReportForm(ModelForm):
  exam = ModelChoiceField(queryset=Exam.objects.all(), required=False, label='Select an exam')
  label = 'Trainees whose exams to generate a report for'
  trainee = ModelMultipleChoiceField(
    widget=TraineeSelect2MultipleInput,
    queryset=Trainee.objects.all(),
    required=False,
    label=label
  )

  def __init__(self, *args, **kwargs):
    super(ExamReportForm, self).__init__(*args, **kwargs)
    self.fields['trainee'].widget.attrs = {'id': 'id_trainees'}

  class Meta:
    model = Session
    fields = ('exam', 'trainee',)

class ExamPeerForm(ModelForm):
  def __init__(self, *args, **kwargs):
    super(ExamPeerForm, self).__init__(*args, **kwargs)
    print "**********************************************************************"
    print str(kwargs)
    print "**********************************************************************"
    #trainees = Trainee.objects.all().order_by('lastname')
    #exam = Exam.objects.get(pk=kwargs['exam'])
    #if exam.training_class.class_type == '1YR':
    #  trainees = trainees.filter(current_term__lte=2)
    #elif exam.training_class.class_type == '2YR':
    #  trainees = trainees.filter(current_term__gte=3)
    #trainees= trainees.exclude(id=self._get_session().trainee.id)
    self.fields['trainee'] = kwargs['initial']['trainees']

  class Meta:
    model = Session
    fields = ('trainee',)


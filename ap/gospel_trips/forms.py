from django import forms

from .models import GospelTrip, Section, Instruction, Question, Answer


class GospelTripForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(GospelTripForm, self).__init__(*args, **kwargs)

    class Meta:
      model = GospelTrip
      fields = ['name', ]


class SectionForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(SectionForm, self).__init__(*args, **kwargs)

  class Meta:
    model = Section
    fields = ['name', ]


class InstructionForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(InstructionForm, self).__init__(*args, **kwargs)

  class Meta:
    model = Instruction
    fields = ['name', 'instruction', ]


class QuestionForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(QuestionForm, self).__init__(*args, **kwargs)

  class Meta:
    model = Question
    fields = ['instruction', 'answer_type', 'answer_choices', ]


class AnswerForm(forms.ModelForm):
  ''' seen by the trainee '''
  def __init__(self, *args, **kwargs):
    answer_type = kwargs.pop('answer_type')
    if answer_type == 'C':
      choices = kwargs.pop('choices')  # pass tuple of tuples
    super(AnswerForm, self).__init__(*args, **kwargs)
    if answer_type == 'C':
      response = forms.ChoiceField(choices=choices)
    if answer_type == 'T':
      response = forms.CharField(max_length=100, widget=forms.Textarea)

  class Meta:
    model = Answer
    fields = ['response', ]

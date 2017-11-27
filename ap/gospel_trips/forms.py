from django import forms

from .models import GospelTrip, Section, Instruction, Question, AnswerSelect, AnswerText


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


class AnswerSelectForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    choices = kwargs.pop('choices')  # pass tuple of tuples
    super(AnswerSelectForm, self).__init__(*args, **kwargs)
    response = forms.ChoiceField(choices=choices)

  class Meta:
    model = AnswerSelect
    fields = ['response', ]


class AnswerTextForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(AnswerTextForm, self).__init__(*args, **kwargs)

  class Meta:
    model = AnswerText
    fields = ['response', ]

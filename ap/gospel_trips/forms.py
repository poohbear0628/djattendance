from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import GospelTrip, Section, Instruction, Question, Answer


class GospelTripForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(GospelTripForm, self).__init__(*args, **kwargs)

  class Meta:
    model = GospelTrip
    fields = ['name', ]
    labels = {
      'name': _('Gospel Trip Name'),
    }


class SectionForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(SectionForm, self).__init__(*args, **kwargs)

  class Meta:
    model = Section
    fields = ['name', ]
    labels = {
      'name': _('Section Name'),
    }


class InstructionForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(InstructionForm, self).__init__(*args, **kwargs)
    self.fields['instruction'].widget.attrs.update({'class': 'mceEditor'})

  class Meta:
    model = Instruction
    fields = ['name', 'instruction', ]
    labels = {
      'name': _('Instruction Name'),
      'instruction': _('instructions'),
    }
    widgets = {
      'instruction': forms.Textarea()
    }


class QuestionForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(QuestionForm, self).__init__(*args, **kwargs)
    self.fields['instruction'].widget.attrs.update({'class': 'mceEditor'})

  class Meta:
    model = Question
    fields = ['instruction', 'answer_type', 'answer_choices', ]
    labels = {
      'instruction': _('Question instructions'),
    }


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


def form_from_object(obj):
  FORM_FROM_OBJECT = {
    'GospelTrip': GospelTripForm,
    'Section': SectionForm,
    'Instruction': InstructionForm,
    'Question': QuestionForm
  }
  return FORM_FROM_OBJECT[obj.__class__.__name__]


def build_form(obj, data={}, prefix=None):
  # prefix - a unique identifier for form data; also tracks order
  if data:
    return form_from_object(obj)(data, instance=obj, prefix=prefix)
  else:
    return form_from_object(obj)(instance=obj, prefix=prefix)


def gospel_trip_forms(gospel_trip, data={}):
  # returns a list of forms
  # gospel_trip - an existing GospelTrip object
  # data - a dictionary containing HTTP Request POST data

  new_s = False  # if data contains new section form data
  new_i = False  # if data contains new instruction form data
  new_q = False  # if data contains new question form data

  all_forms = [build_form(gospel_trip, data)]

  sections = Section.objects.filter(gospel_trip=gospel_trip)
  for s in sections:

    prefix = 's' + str(s.index)
    all_forms.append(build_form(s, data, prefix))

    instructions = Instruction.objects.filter(section=s)
    for i in instructions:
      prefix = 'i' + str(i.index)
      all_forms.append(build_form(i, data, prefix))

    else:
      if not new_i:
        prefix = 'i' + str(len(instructions) + 1)
        all_forms.append(InstructionForm(data, prefix=prefix))
        new_i = True

    if not data:
      if not new_i:
        prefix = 'i' + str(len(instructions) + 1)
        all_forms.append(InstructionForm(prefix=prefix, instance=Instruction()))
        new_i = True

    questions = Question.objects.filter(section=s)
    for q in questions:

      prefix = 'q' + str(q.index)
      all_forms.append(build_form(q, data, prefix))

    else:
      prefix = 'q' + str(len(questions) + 1)
      if not new_q:
        all_forms.append(QuestionForm(data, prefix=prefix))
        new_q = True
    if not data:
      if not new_q:
        prefix = 'q' + str(len(questions) + 1)
        all_forms.append(QuestionForm(prefix=prefix, instance=Question()))
        new_q = True
  else:
    if not new_s:
      prefix = 's' + str(len(sections) + 1)
      all_forms.append(SectionForm(data, prefix=prefix))
      new_s = True

  if not data:
    if not new_s:
      prefix = 's' + str(len(sections) + 1)
      all_forms.append(SectionForm(prefix=prefix, instance=Section()))
      new_s = True
  return all_forms

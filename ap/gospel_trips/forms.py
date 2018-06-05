from collections import OrderedDict

from aputils.widgets import DatetimePicker
from django import forms
from django.forms.models import BaseInlineFormSet, inlineformset_factory
from django.utils.translation import ugettext_lazy as _

from .models import Answer, GospelTrip, Instruction, Question, Section, Destination

InstructionFormSet = inlineformset_factory(Section, Instruction, fields=('name', 'instruction'), extra=1, can_order=True)
QuestionFormSet = inlineformset_factory(
    Section, Question, fields=('instruction', 'answer_type'),
    widgets={'answer_type': forms.TextInput()}, extra=1, can_order=True)


class GospelTripForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(GospelTripForm, self).__init__(*args, **kwargs)

  class Meta:
    model = GospelTrip
    fields = "__all__"
    labels = {
      'name': _('Gospel Trip Name'),
    }
    widgets = {
      'open_time': DatetimePicker(),
      'close_time': DatetimePicker()
    }


class AnswerForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    if 'gospel_trip__pk' in kwargs:
      gospel_trip = kwargs.pop('gospel_trip__pk')
    super(AnswerForm, self).__init__(*args, **kwargs)
    self.fields['response'] = forms.CharField(widget=forms.Textarea)
    if self.instance.question:
        answer_type = self.instance.question.answer_type['type']
        if answer_type == 'choice':
          choices = [(c, c) for c in self.instance.question.answer_type['choices']]
          self.fields['response'] = forms.ChoiceField(choices=choices)
        elif answer_type == 'destinations':
          self.fields['response'] = forms.ModelChoiceField(
            queryset=Destination.objects.filter(gospel_trip=gospel_trip),
            required=True,
          )

  class Meta:
    model = Answer
    fields = ['response', ]


class BaseSectionFormset(BaseInlineFormSet):
  def add_fields(self, form, index):
    super(BaseSectionFormset, self).add_fields(form, index)

    # save the formset in the 'nested' property
    form.nested = OrderedDict()
    form.nested['Instructions'] = InstructionFormSet(
        instance=form.instance,
        data=form.data if form.is_bound else None,
        files=form.files if form.is_bound else None,
        prefix='instruction-%s-%s' % (
            form.prefix,
            InstructionFormSet.get_default_prefix()),)

    form.nested['Questions'] = QuestionFormSet(
        instance=form.instance,
        data=form.data if form.is_bound else None,
        files=form.files if form.is_bound else None,
        prefix='question-%s-%s' % (
            form.prefix,
            QuestionFormSet.get_default_prefix()),)

  def is_valid(self):
    result = super(BaseSectionFormset, self).is_valid()

    if self.is_bound:
      for form in self.forms:
        if hasattr(form, 'nested'):
          for name, f in form.nested.items():
            result = result and f.is_valid()

    return result

  def save(self, commit=True):
    result = super(BaseSectionFormset, self).save(commit=commit)

    for form in self.forms:
      if hasattr(form, 'nested'):
        if not self._should_delete_form(form):
          for name, f in form.nested.items():
            f.save(commit=commit)

    return result


SectionFormSet = inlineformset_factory(GospelTrip, Section, formset=BaseSectionFormset, fields=('name', ), extra=1, can_order=True)

from collections import OrderedDict

from aputils.widgets import DatetimePicker
from django import forms
from django.forms.models import BaseInlineFormSet, inlineformset_factory
from django.utils.translation import ugettext_lazy as _

from .models import Answer, GospelTripAdmin, Instruction, Question, Section

InstructionFormSet = inlineformset_factory(Section, Instruction, fields=('name', 'instruction'), extra=1, can_order=True)
QuestionFormSet = inlineformset_factory(Section, Question, fields=('instruction', ), extra=1, can_order=True)
AnswerFormSet = inlineformset_factory(Question, Answer, fields=('response', ), extra=1)


class GospelTripAdminForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(GospelTripAdminForm, self).__init__(*args, **kwargs)

  class Meta:
    model = GospelTripAdmin
    fields = "__all__"
    labels = {
      'name': _('Gospel Trip Name'),
    }
    widgets = {
      'open_time': DatetimePicker(),
      'close_time': DatetimePicker()
    }


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
          print form.nested
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


SectionFormSet = inlineformset_factory(GospelTripAdmin, Section, formset=BaseSectionFormset, fields=('name', ), extra=1, can_order=True)

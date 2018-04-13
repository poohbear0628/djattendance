from django import forms
from classes.models import ClassFile


class ClassFileForm(forms.ModelForm):

  def __init__(self, *args, **kwargs):
    limit_choices = kwargs.pop('limit_choices')
    super(ClassFileForm, self).__init__(*args, **kwargs)
    if limit_choices:
      self.fields['for_class'].choices = limit_choices

  class Meta:
    model = ClassFile
    fields = ['label', 'for_class', 'file']

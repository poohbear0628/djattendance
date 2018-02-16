from django import forms
from classes.models import ClassFile


class ClassFileForm(forms.ModelForm):

  def __init__(self, *args, **kwargs):
    super(ClassFileForm, self).__init__(*args, **kwargs)

  class Meta:
    model = ClassFile
    fields = ['label', 'for_class', 'file']

from django import forms
from .models import Syllabus, ClassSession

class NewSyllabusForm(forms.ModelForm):

  class Meta:
    model = Syllabus
    fields = '__all__'
    #widgets = {
    #  'start': DatepickerWidget(),
    #  'end': DatepickerWidget()
    #}

  def save(self, commit=True):
    #data = self.cleaned_data
    syllabus = super(NewSyllabusForm, self).save(commit=False)
    #syllabus.season = data['season']
    #syllabus.name = data['season']
    #syllabus.code = syllabus.name[:2]
    #syllabus.start = data['start']
    #syllabus.end = data['end']

    #if syllabus.start.year == syllabus.end.year:
    #  syllabus.name += ' ' + str(syllabus.start.year)
    #  syllabus.code += str(syllabus.start.year)[2:]
##    else:
      # error
    ## check if term code has duplicate??

    if commit:
      syllabus.save()
    return syllabus

class NewSessionForm(forms.ModelForm):

  class Meta:
    model = ClassSession
    fields = '__all__'

  def save(self, commit=True):
    session = super(NewSessionForm, self).save(commit=False)
    if commit:
      session.save()
    return session

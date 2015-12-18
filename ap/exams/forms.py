from django.forms import Form, ModelForm
from django.forms import CharField, TextInput
# from django.forms.formsets import BaseInlineFormSet
# from django.forms.models import inlineformset_factory
from django_select2 import ModelSelect2MultipleField

from .models import Trainee, Exam, Section

class TraineeSelectForm(Form):
    trainees = ModelSelect2MultipleField(queryset=Trainee.objects, 
                                         required=False, 
                                         search_fields=['^first_name', '^last_name'])

class ExamCreateForm(ModelForm):
    class Meta:
        model = Exam
        fields = ('training_class', 'name', 'is_open', 'duration', 'category')

# class EssayQuestionForm(ModelForm):
#     question = CharField(max_length=200,
#                          widget=TextInput(attrs={
#                             'placeholder':'Question',
#                             }),
#                          required=True)

# class SectionForm(ModelForm):
#     class Meta:
#         model = Section
#         fields = ('description',)

# class BaseSectionFormSet(BaseInlineFormSet):

#     def add_fields(self, form, index):

#         super(BaseSectionFormSet, self).add_fields(form, index)

# SectionFormset = inlineformset_factory(Exam, 
#                                        Section, 
#                                        formset=BaseSectionFormset, 
#                                        extra=1)
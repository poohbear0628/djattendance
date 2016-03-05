from django.forms import Form, ModelForm, formset_factory
from django.forms import CharField, Textarea, TextInput
from django.forms.models import inlineformset_factory, BaseInlineFormSet
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

class EssayQuestionForm(ModelForm):
    question = CharField(max_length=200,
                         widget=TextInput(attrs={
                            'placeholder':'Question',
                            }),
                         required=True)

EssayQuestionFormset = formset_factory(EssayQuestionForm,
                                       extra=1,
                                       can_order=True,
                                       can_delete=True)

class SectionForm(ModelForm):
   class Meta:
        model = Section
        fields = ('description',)
        widgets = {
            'description': Textarea(
                attrs={'placeholder':'Type instructions for this section here',
                       'rows': '2',
                       'cols': '60'}
                )
        }

class BaseSectionFormSet(BaseInlineFormSet):
    model = Exam
    inline_model = Section
    def add_fields(self, form, index):
        super(BaseSectionFormSet, self).add_fields(form, index)

        # get the SectionForm that we are related to
        try:
            sectionform = self.get_queryset()[index]
        except IndexError:
            sectionform = None

        print "adding field"
        # create and store a essay question formset
        form.nested = [
            EssayQuestionFormset()]


SectionFormSet = inlineformset_factory(Exam, 
                                       Section, 
                                       form=SectionForm,
                                       formset=BaseSectionFormSet, 
                                       extra=1,
                                       can_order=True,
                                       can_delete=True)
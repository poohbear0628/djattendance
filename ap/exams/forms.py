from django.forms import Form, ModelForm, formset_factory
from django.forms import CharField, Textarea, TextInput
from django.forms.models import inlineformset_factory, BaseInlineFormSet
from django_select2 import ModelSelect2MultipleField

from .models import Trainee, Exam, Section

class ExamCreateForm(ModelForm):
    class Meta:
        model = Exam
        fields = ('training_class', 'description', 'is_open', 'duration', 'category', 'term')

from django import forms
from .models import Portion

class CreateForm(forms.ModelForm):
  class Meta:
    model = Portion
    exclude = ('submitted_by', 'approved', 'timestamp')

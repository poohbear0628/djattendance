from django.forms import ModelForm
from django.forms.formsets import formset_factory
from aputils.models import City

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name', 'state', 'country']

CityFormSet = formset_factory(CityForm, extra=2)
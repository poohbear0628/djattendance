from django import forms
from django.forms import modelformset_factory
from .models import Table, TraineeExclusion
from accounts.models import Trainee
from django.contrib.admin.widgets import FilteredSelectMultiple


TableFormSetBase = modelformset_factory(Table, fields=('name', 'capacity', 'gender', 'location',), can_delete=True)
TraineeExclusionFormSetBase = modelformset_factory(TraineeExclusion, fields=('trainee',))

class TableFormSet(TableFormSetBase):
  # this is where you can add additional fields to a ModelFormSet
  # this is also where you can change stuff about the auto generated form
  def add_fields(self, form, index):
    super(TableFormSet, self).add_fields(form, index)
    form.fields['is_deleted'] = forms.BooleanField(required=False)

class TraineeExclusionFormSet(TableFormSetBase):
  # this is where you can add additional fields to a ModelFormSet
  # this is also where you can change stuff about the auto generated form
  def add_fields(self, form, index):
    super(TraineeExclusionFormSet, self).add_fields(form, index)
    form.fields['is_deleted'] = forms.BooleanField(required=False)

class TraineeExclusionForm(forms.ModelForm):                                 
  trainees = forms.ModelMultipleChoiceField(                           
    queryset=Trainee.objects.all(),                                  
    widget=FilteredSelectMultiple("verbose name", is_stacked=False)     
  )                                                                       

  class Meta:                                                             
    model = Trainee                                                      
    fields = ('firstname', 'lastname' )

  class Media:
   css = {'all': ('/static/admin/css/widgets.css',),}
   js = ('/admin/jsi18n',)


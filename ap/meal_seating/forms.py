from django import forms
from django.forms import modelformset_factory
from .models import Table, TraineeExclude
from accounts.models import Trainee
from django.contrib.admin.widgets import FilteredSelectMultiple


TableFormSetBase = modelformset_factory(Table, fields=('name', 'capacity', 'gender', 'location',), can_delete=True, extra=1, max_num=1)
TraineeExcludeFormSetBase = modelformset_factory(TraineeExclude, fields=('trainee',))

class TableFormSet(TableFormSetBase):
  # this is where you can add additional fields to a ModelFormSet
  # this is also where you can change stuff about the auto generated form
  def add_fields(self, form, index):
    super(TableFormSet, self).add_fields(form, index)
    form.fields['is_deleted'] = forms.BooleanField(required=False)

class TraineeExcludeFormSet(TableFormSetBase):
  # this is where you can add additional fields to a ModelFormSet
  # this is also where you can change stuff about the auto generated form
  def add_fields(self, form, index):
    super(TraineeExcludeFormSet, self).add_fields(form, index)
    form.fields['is_deleted'] = forms.BooleanField(required=False)

class TraineeExcludeForm(forms.ModelForm):                                 
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


from django.contrib import admin
from .models import Roll, Trainee, Event
#from accounts.models import User
#from schedules.constants import WEEKDAYS

from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import Group

from django_select2.forms import ModelSelect2Widget

class RollAdminForm(forms.ModelForm):
  event = forms.ModelChoiceField(
  	label="Event",
  	queryset=Event.objects.all(),
  	required=True,
  	widget=ModelSelect2Widget(
  	  queryset=Event.objects.all(),
  	  required=True,
  	  search_fields=['name__icontains', 'weekday__icontains'],
  	)
  )

  trainee = forms.ModelChoiceField(
	label="Trainee",
	queryset=Trainee.objects.filter(is_active=True),
	required=True,
	widget=ModelSelect2Widget(
	  queryset=Trainee.objects.filter(is_active=True),
	  required=True,
	  search_fields=['firstname__icontains', 'lastname__icontains'],
	)
  )

  submitted_by = forms.ModelChoiceField(
	label="Submitted by",
	queryset=Trainee.objects.filter(is_active=True),
	required=True,
	widget=ModelSelect2Widget(
	  queryset=Trainee.objects.filter(is_active=True),
	  required=True,
	  search_fields=['firstname__icontains', 'lastname__icontains'],
	)
  )

  # class Meta:
  # 	model = Roll
  # 	fields = ['submitted_by']
  # 	widgets = {
  # 	  'submitted_by': ModelSelect2Widget(
	 #  	queryset=Trainee.objects.filter(is_active=True),
	 #  	required=True,
	 #  	search_fields=['firstname__icontains', 'lastname__icontains'],
	 #  )
  # 	}

  # def __init__(self, *args, **kwargs):
  # 	self.user = kwargs.pop('user', None)
  # 	super(RollAdminForm, self).__init__(*args, **kwargs)
  

class RollAdmin(admin.ModelAdmin):
  list_display = ('date', 'event', 'trainee', 'status', 'finalized')
  list_filter = ('date', 'event__name', 'status')
  ordering = ('date', 'event', 'trainee')
  search_fields = ('trainee__firstname', 'trainee__lastname', 'event__name', 'status', 'date')
  form = RollAdminForm
  # def get_form_kwargs(self):
  # 	kwargs = super(RollAdmin, self).get_form_kwargs()
  # 	kwargs['user'] = self.request.user
  # 	return kwargs

admin.site.register(Roll, RollAdmin)
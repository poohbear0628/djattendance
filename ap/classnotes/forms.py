from django import forms
from bootstrap3_datetime.widgets import DateTimePicker
from .models import Classnotes
from accounts.models import Trainee

class NewClassnotesForm(forms.ModelForm):

	READONLY_FIELDS = ('trainee', 'classname', 'classdate')

	class Meta:
		model = Classnotes
		exclude = ('status', 'date_submitted')
		widgets = {'minimum_words': forms.HiddenInput()}

	# def __init__(self, *args, **kwargs):
	# 	t = kwargs.pop('trainee', None)
	# 	super(NewClassnotesForm, self).__init__(*args, **kwargs)
	# 	widgets = {'minimum_words': forms.HiddenInput()}
	# 	for field in self.READONLY_FIELDS:
	# 		self.fields[field].widget.attrs['readonly'] = True

	# def save(self, commit=True):
	# 	classnotes = super(NewClassnotesForm, self).save(commit=False)
	# 	if commit:
	# 		classnotes.save()
	# 	return classnotes

class EditClassnotesForm(forms.ModelForm):

	class Meta:
		model = Classnotes
		exclude = ('status', 'comments', 'date', 'date_submitted', 'event', 'type', 'trainee')
		widgets = {'minimum_words': forms.HiddenInput()}

	def save(self, commit=True):
		classnotes = super(EditClassnotesForm, self).save(commit=False)
		if commit:
			classnotes.save()
		return classnotes	

class ApproveClassnotesForm(forms.ModelForm):

	class Meta:
		model = Classnotes
		#exclude = ('status', 'content', 'date', 'date_submitted', 'event', 'type', 'trainee')
		fields = ('comments',)

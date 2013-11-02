from django.forms.models import modelformset_factory
from django.shortcuts import render, render_to_response
from django.views.generic.edit import FormView
from absent_trainee_roster.forms import AbsentTraineeForm
from absent_trainee_roster.models import Entry
from django.core.context_processors import csrf
from django.template import RequestContext # For CSRF
from django.forms.formsets import formset_factory, BaseFormSet
from absent_trainee_roster.forms import AbsentTraineeForm, NewEntryFormSet


def absent_trainee_form(request):
	EntryFormSet = modelformset_factory(Entry, AbsentTraineeForm, formset=NewEntryFormSet, max_num=10, extra=2)
	if request.method == 'POST':
		formset = EntryFormSet(request.user, request.POST, request.FILES)
		if formset.is_valid():
			formset.save()
			# roster = roster for today's date
			# for form in formset.forms:
			# 	entry = form.save(commit=False)
			# 	entry.roster = roster
			# 	entry.save()
	else:
		formset = EntryFormSet(user=request.user)
	return render_to_response('absent_trainee_roster/absent_trainee_form.html', {'formset': formset, 'user':request.user})

from datetime import date

from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages

from absent_trainee_roster.models import Entry, Roster
from absent_trainee_roster.forms import AbsentTraineeForm, NewEntryFormSet

from absent_trainee_roster.utils import generate_pdf, send_absentee_report

# @user_passes_test(lambda u: u.groups.filter(name='house_coordinator').count() == 1, login_url = '/')
def absent_trainee_form(request):
	EntryFormSet = modelformset_factory(Entry, AbsentTraineeForm, formset=NewEntryFormSet, max_num=50, extra=1, can_delete=True)
	
	today = date.today()
	# get today's roster. create it if it doesn't exist.
	if Roster.objects.filter(date=today).exists():
		roster = Roster.objects.get(date=today)
	else:
		roster = Roster.objects.create_roster(date=today)

	if request.method == 'POST':
		formset = EntryFormSet(request.POST, request.FILES, user=request.user)
		if formset.is_valid():
			new_absentees = {}
			for i in xrange(int(request.POST['form-TOTAL_FORMS'])):
				if request.POST['form-' + str(i) + '-absentee']:
					absentee = int(request.POST['form-' + str(i) + '-absentee'])
					new_absentees[absentee] = i
			for form in formset.forms:
				if form.cleaned_data: # only save entry if it's not empty
					entry = form.save(commit=False)

					# check for overriding entry for absentee already in database
					# for existing_entry in roster.entry_set.filter(absentee__house=request.user.house):
					for existing_entry in roster.entry_set.all():
						if entry.absentee == existing_entry.absentee:
							existing_entry.delete()
						
					entry.roster = roster
					roster.unreported_houses.remove(entry.absentee.house)
					entry.save()
			
			# delete entries for absentees not in newly submitted form
			# entries = roster.entry_set.filter(absentee__house=request.user.house)
			entries = roster.entry_set.all()
			for entry in entries:
				if entry.absentee.id not in new_absentees.keys():
					entry.delete()
			# uncomment if this view is being used by HCs
			#roster.unreported_houses.remove(request.user.house)
			
			# return redirect('/')

			# Need to fix this so message displays without refresh
			# messages.add_message(request, messages.SUCCESS, 'Saved')
		roster_notes = request.POST.get('notes')
		if roster_notes:
			roster.notes = roster_notes
		else:
			roster.notes = ''
		roster.save()

	else:
		# shows existing entries from user's house, i.e. if form was already submitted and user revisits the page
		if request.user.is_hc:
			formset = EntryFormSet(user=request.user, queryset=roster.entry_set.filter(absentee__house=request.user.house))
		else:
			formset = EntryFormSet(user=request.user, queryset=roster.entry_set.all())

	bro_unreported = roster.unreported_houses.filter(gender='B')
	sis_unreported = roster.unreported_houses.filter(gender='S')

	c = {'formset': formset, 'user': request.user, 'bro_unreported': bro_unreported, 'sis_unreported': sis_unreported, 'roster': roster}
	c.update(csrf(request))

	return render_to_response('absent_trainee_roster/absent_trainee_form.html', c)

def pdf_report(request, year, month, day):
	return generate_pdf(year, month, day)

def email(request):
	today = date.today()
	send_absentee_report(today.year, today.month, today.day)
	return HttpResponse("Email was sent")
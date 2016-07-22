from datetime import date

from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from aputils.groups_required_decorator import group_required

from absent_trainee_roster.models import Entry, Roster
from absent_trainee_roster.forms import AbsentTraineeForm, NewEntryFormSet

from absent_trainee_roster.utils import generate_pdf, send_absentee_report

EntryFormSet = modelformset_factory(Entry, AbsentTraineeForm, formset=NewEntryFormSet, max_num=50, extra=1, can_delete=True)

# @user_passes_test(lambda u: u.groups.filter(name='house_coordinator').count() == 1, login_url = '/')
@group_required(('HC', 'absent_trainee_roster'))
def absent_trainee_form(request):
  today = date.today()
  user = request.user
  is_HC = user.HC_status()
  # get today's roster. create it if it doesn't exist.
  if Roster.objects.filter(date=today).exists():
    roster = Roster.objects.get(date=today)
  else:
    roster = Roster.objects.create_roster(date=today)

  if request.method == 'POST':
    # If HC submits any type of form, counts it as reported (empty form)
    if is_HC:
        roster.unreported_houses.remove(request.user.house)

    formset = EntryFormSet(request.POST, request.FILES, user=request.user)
    if formset.is_valid():
      print 'formset is valid'
      new_absentees = []
      # print formset.forms
      for form in formset.forms:
        print '!!!!!!!!!!!!!!!form', form.cleaned_data, form.is_valid()
        if form.cleaned_data: # only save entry if it's not empty
          print 'FORM! clean!~~~~~~~~~~~~~~~~~~'
          entry = form.save(commit=False)

          entry.roster = roster
          roster.unreported_houses.remove(entry.absentee.house)
          entry.save()

          new_absentees.append(entry.id)


      # delete entries for absentees not in newly submitted form
      # entries = roster.entry_set.filter(absentee__house=request.user.house)
      entries = roster.entry_set.exclude(id__in=new_absentees)
      print 'before entries', entries, new_absentees
      if not user.groups.filter(name='absent_trainee_roster').exists():
        entries = entries.filter(absentee__house=user.house)
        print 'isHC', entries

      formset.save(commit=False)

      # print 'deleted forms', formset.deleted_forms
      # print 'deleted object', formset.deleted_objects

      for entry in entries:
        print 'delete', entry
        entry.delete()

      # Need to fix this so message displays without refresh
      # messages.add_message(request, messages.SUCCESS, 'Saved')
    roster_notes = request.POST.get('notes')
    if roster_notes:
      roster.notes = roster_notes
    else:
      roster.notes = ''
    roster.save()

    if request.user.groups.filter(name='absent_trainee_roster').exists():
      formset = EntryFormSet(user=request.user, queryset=roster.entry_set.all())
    else:
      formset = EntryFormSet(user=request.user, queryset=roster.entry_set.filter(absentee__house=request.user.house))


    # roster = Roster.objects.get(date=today)

  else:
    # shows existing entries from user's house, i.e. if form was already submitted and user revisits the page
    if request.user.groups.filter(name='absent_trainee_roster').exists():
      formset = EntryFormSet(user=request.user, queryset=roster.entry_set.all())
    else:
      formset = EntryFormSet(user=request.user, queryset=roster.entry_set.filter(absentee__house=request.user.house))

  bro_unreported = roster.unreported_houses.filter(gender='B')
  sis_unreported = roster.unreported_houses.filter(gender='S')

  c = {'formset': formset, 'user': request.user, 'bro_unreported': bro_unreported, 'sis_unreported': sis_unreported, 'roster': roster}
  c.update(csrf(request))

  return render_to_response('absent_trainee_roster/absent_trainee_form.html', c)

@group_required(('absent_trainee_roster'))
def pdf_report(request, year, month, day):
  return generate_pdf(year, month, day)

@group_required(('absent_trainee_roster'))
def email(request):
  today = date.today()
  send_absentee_report(today.year, today.month, today.day)
  return HttpResponse("Email was sent")


@group_required(('absent_trainee_roster'))
def email_on_date(request, year, month, day):
  send_absentee_report(year, month, day)
  return HttpResponse("Email was sent for %s-%s-%s" % (month, day, year))

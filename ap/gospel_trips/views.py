# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from gospel_trips.models import GospelTrip, Section, Instruction, Question, Answer
from gospel_trips.forms import GospelTripForm, SectionForm, InstructionForm, QuestionForm, AnswerForm


def gospel_trip_forms(gospel_trip, data={}):
  new_s = False
  new_i = False
  new_q = False

  if data:
    all_forms = [GospelTripForm(data, instance=gospel_trip)]
  else:
    all_forms = [GospelTripForm(instance=gospel_trip)]

  sections = Section.objects.filter(gospel_trip=gospel_trip)
  for s in sections:

    if data:
      all_forms.append(SectionForm(data, prefix='s' + str(s.index), instance=s))
    else:
      all_forms.append(SectionForm(prefix='s' + str(s.index), instance=s))

    instructions = Instruction.objects.filter(section=s)
    for i in instructions:
      if data:
        all_forms.append(InstructionForm(data, prefix='i' + str(i.index), instance=i))
      else:
        all_forms.append(InstructionForm(prefix='i' + str(i.index), instance=i))
    else:
      if not new_i:
        all_forms.append(InstructionForm(data, prefix='i' + str(len(instructions) + 1)))
        new_i = True

    if not data:
      if not new_i:
        all_forms.append(InstructionForm(prefix='i' + str(len(instructions) + 1), instance=Instruction()))
        new_i = True

    questions = Question.objects.filter(section=s)
    for q in questions:
      if data:
        all_forms.append(QuestionForm(data, prefix='q' + str(q.index), instance=q))
      else:
        all_forms.append(QuestionForm(prefix='q' + str(q.index), instance=q))
    else:
      if not new_q:
        all_forms.append(QuestionForm(data, prefix='q' + str(len(questions) + 1)))
        new_q = True
    if not data:
      if not new_q:
        all_forms.append(QuestionForm(prefix='q' + str(len(questions) + 1), instance=Question()))
        new_q = True

  else:
    if not new_s:
      all_forms.append(SectionForm(data, prefix='s' + str(len(sections) + 1)))
      new_s = True

  if not data:
    if not new_s:
      all_forms.append(SectionForm(prefix='s' + str(len(sections) + 1), instance=Section()))
      new_s = True
  return all_forms


# Create your views here.
def create_gospel_trip(request, pk):
  ctx = {}
  gt, created = GospelTrip.objects.get_or_create(id=1)

  if request.method == 'POST':
    data = request.POST
    print data

    all_forms = gospel_trip_forms(gt, data)

    print all_forms

    if all([form.is_valid() for form in all_forms]):

      for form in all_forms:

        if form.__class__.__name__ == 'GospelTripForm':
          obj = form.save(commit=False)
          if obj.name:
            form.save()

        elif form.__class__.__name__ == 'SectionForm':
          print form
          obj = form.save(commit=False)
          obj.gospel_trip = gt
          obj.index = int(form.prefix[1:])
          if obj.name:
            form.save()

        elif form.__class__.__name__ == 'InstructionForm':
          obj = form.save(commit=False)
          obj.index = int(form.prefix[1:])
          if obj.name or obj.instruction:
            obj.save()

        elif form.__class__.__name__ == 'QuestionForm':
          obj = form.save(commit=False)
          obj.index = int(form.prefix[1:])
          if obj.instruction:
            obj.save()

      print 'good!'

    return HttpResponseRedirect(gt.get_absolute_url())
  else:  # GET

    all_forms = gospel_trip_forms(gt)
    ctx['all_forms'] = all_forms
    print all_forms
    return render(request, 'gospel_trips/new_gospel_trip.html', ctx)

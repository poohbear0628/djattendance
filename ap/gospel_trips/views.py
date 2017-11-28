# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from gospel_trips.models import GospelTrip, Section, Instruction, Question, Answer
from gospel_trips.forms import GospelTripForm, SectionForm, InstructionForm, QuestionForm, AnswerForm


def gospel_trip_forms(gospel_trip, data={}):

  if data:
    all_forms = [GospelTripForm(data, instance=gospel_trip)]
  else:
    all_forms = [GospelTripForm(instance=gospel_trip)]

  sections = Section.objects.filter(gospel_trip=gospel_trip)
  for s in sections:

    if data:
      all_forms.append(SectionForm(data, prefix=s.index, instance=s))
    else:
      all_forms.append(SectionForm(prefix=s.index, instance=s))

    instructions = Instruction.objects.filter(section=s)
    for i in instructions:
      if data:
        all_forms.append(InstructionForm(data, prefix=i.index, instance=i))
      else:
        all_forms.append(InstructionForm(prefix=i.index, instance=i))
    if not data:
      all_forms.append(InstructionForm(prefix=len(instructions) + 1, instance=Instruction()))

    questions = Question.objects.filter(section=s)
    for q in questions:
      if data:
        all_forms.append(QuestionForm(data, prefix=q.index, instance=q))
      else:
        all_forms.append(QuestionForm(prefix=q.index, instance=q))
    if not data:
      all_forms.append(QuestionForm(prefix=len(questions) + 1, instance=Question()))

  if not data:
    all_forms.append(SectionForm(prefix=len(sections) + 1, instance=Section()))
  return all_forms


# Create your views here.
def create_gospel_trip(request, pk):
  ctx = {}
  gt, created = GospelTrip.objects.get_or_create(id=1)

  if request.method == 'POST':
    data = request.POST
    print data

    all_forms = gospel_trip_forms(gt, data)

    if all([form.is_valid() for form in all_forms]):
      section_counter = 1
      instrction_counter = 1

# figure out counter better
      for form in all_forms:
        if form.__name__ == 'SectionForm':
          section = form.save(commit=False)
          section.gospel_trip = gt
          if section == 0:
            section.index += section_counter
          section_counter += 1

        elif form.__name__ == 'InstructionForm':
          obj = form.save(commit=False)
          obj.index = instrction_counter
          instrction_counter += 1

        elif form.__name__ == 'QuestionForm':
          obj = form.save(commit=False)
          obj.index = question_counter
          instrction_counter += 1

      print 'good!'

    return HttpResponseRedirect(gt.get_absolute_url())
  else:  # GET

    all_forms = gospel_trip_forms(gt)
    ctx['all_forms'] = all_forms
    print all_forms
    return render(request, 'gospel_trips/new_gospel_trip.html', ctx)

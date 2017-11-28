# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from gospel_trips.models import GospelTrip, Section, Instruction, Question, Answer
from gospel_trips.forms import GospelTripForm, SectionForm, InstructionForm, QuestionForm, AnswerForm


# Create your views here.
def create_gospel_trip(request, pk):
  ctx = {}
  gt, created = GospelTrip.objects.get_or_create(id=1)
  sections = Section.objects.filter(gospel_trip=gt)
  instructions = Instruction.objects.filter(section__gospel_trip=gt)
  questions = Question.objects.filter(section__gospel_trip=gt)

  if request.method == 'POST':
    return HttpResponseRedirect(reverse('gospel-trip-create', {'pk': gt.id}))
  else:  # GET

    section_forms = []
    for s in sections:
      section_forms.append(
        SectionForm(prefix=s.index, instance=s)
      )
    next_section = len(sections) + 1
    section_forms.append(SectionForm(prefix=next_section, instance=Section()))

    instr_forms = []
    for i in instructions:
      instr_forms.append(
        InstructionForm(prefix=i.index, instance=i)
      )
    next_instruction = len(instructions) + 1
    instr_forms.append(InstructionForm(prefix=next_instruction, instance=Instruction()))

    question_forms = []
    for q in questions:
      question_forms.append(
        QuestionForm(prefix=q.index, instance=q)
      )
    next_question = len(questions) + 1
    question_forms.append(QuestionForm(prefix=next_question, instance=Question()))

    # organizer
    all_forms = [GospelTripForm(instance=gt)]
    for s in sections:

      all_forms.append(
        SectionForm(prefix=s.index, instance=s)
      )

      iss = Instruction.objects.filter(section=s)
      for i in iss:
        all_forms.append(
         InstructionForm(prefix=i.index, instance=i)
        )
      all_forms.append(InstructionForm(prefix=len(iss) + 1, instance=Instruction()))

      qs = Question.objects.filter(section=s)
      for q in qs:
        all_forms.append(
          QuestionForm(prefix=q.index, instance=q)
        )
      all_forms.append(QuestionForm(prefix=len(qs) + 1, instance=Question()))

    all_forms.append(SectionForm(prefix=len(sections) + 1, instance=Section()))

    ctx['gt_form'] = GospelTripForm(instance=gt)
    ctx['section_forms'] = section_forms
    ctx['instr_forms'] = instr_forms
    ctx['question_forms'] = question_forms
    ctx['all_forms'] = all_forms
    print all_forms
    return render(request, 'gospel_trips/new_gospel_trip.html', ctx)

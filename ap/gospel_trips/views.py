# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from gospel_trips.models import GospelTrip, Section, Instruction, Question, Answer
from gospel_trips.forms import GospelTripForm, SectionForm, InstructionForm, QuestionForm, AnswerForm


# Create your views here.
def create_survey(request):
  ctx = {}
  if request.method == 'POST':
    pass
  else:  # GET
    ctx['gt_form'] = GospelTripForm()
    ctx['section_form'] = SectionForm()
    ctx['inst_form'] = InstructionForm()
    ctx['question_form'] = QuestionForm()
  return render(request, 'template', ctx)

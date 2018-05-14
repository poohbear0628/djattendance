# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from braces.views import GroupRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView

from .forms import GospelTripForm, SectionFormSet, AnswerForm
from .models import GospelTrip, Question, Answer
from aputils.trainee_utils import trainee_from_user


# Create your views here.
class GospelTripView(GroupRequiredMixin, CreateView):
  model = GospelTrip
  template_name = 'gospel_trips/gospel_trips_admin.html'
  form_class = GospelTripForm
  group_required = ['training_assistant']

  def get_context_data(self, **kwargs):
    ctx = super(GospelTripView, self).get_context_data(**kwargs)
    ctx['gospel_trips'] = GospelTrip.objects.all()
    ctx['page_title'] = 'Gospel Trip Admin'
    return ctx


def gospel_trip_admin_update(request, pk):
  gt = get_object_or_404(GospelTrip, pk=pk)
  context = {'page_title': 'Gospel Trip Editor'}

  if request.method == "POST":
    form = GospelTripForm(request.POST, instance=gt)
    form_set = SectionFormSet(request.POST, instance=gt)
    if form.is_valid() and form_set.is_valid():
      form.save()
      form_set.save()
      return HttpResponseRedirect("")
    else:
      context['admin_form'] = form
      context['section_formset'] = form_set
      context['last_form_counter'] = len(form_set)
  else:
    section_formset = SectionFormSet(instance=gt)
    context['admin_form'] = GospelTripForm(instance=gt)
    context['section_formset'] = section_formset
    context['last_form_counter'] = len(section_formset)
  return render(request, 'gospel_trips/gospel_trips_admin_update.html', context=context)


def gospel_trip_trainee(request, pk):
  gt = get_object_or_404(GospelTrip, pk=pk)
  trainee = trainee_from_user(request.user)
  context = {'page_title': gt.name}
  context['gospel_trip'] = gt
  if request.method == "POST":
    answer_forms = [AnswerForm(request.POST, prefix=q['id']) for q in Question.objects.filter(section__gospel_trip=gt).values('id')]
    if all(f.is_valid() for f in answer_forms):
      for f in answer_forms:
        answer = f.save(commit=True)
        answer.gospel_trip = gt
        answer.trainee = trainee
        answer.question = Question.objects.get(id=f.prefix)
        answer.save()
        return HttpResponseRedirect("")
    else:
      context['answer_forms'] = answer_forms
  else:
    answer_forms = []
    for q in Question.objects.filter(section__gospel_trip=gt).all():
      answer = Answer.objects.get_or_create(trainee=trainee, gospel_trip=gt, question=q)[0]
      answer_forms.append(AnswerForm(prefix=q.id, instance=answer))
    context['answer_forms'] = answer_forms
  return render(request, 'gospel_trips/gospel_trips.html', context=context)

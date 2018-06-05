# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from aputils.decorators import group_required
from aputils.trainee_utils import trainee_from_user
from braces.views import GroupRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from .forms import AnswerForm, GospelTripForm, SectionFormSet
from .models import Answer, GospelTrip, Question, Destination


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


@group_required(['training_assistant'])
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
  answer_forms = []
  if request.method == "POST":
    for q in Question.objects.filter(section__gospel_trip=gt):
      answer = Answer.objects.get_or_create(trainee=trainee, gospel_trip=gt, question=q)[0]
      answer_forms.append(
        AnswerForm(request.POST, prefix=q.id, instance=answer)
      )
    if all(f.is_valid() for f in answer_forms):
      for f in answer_forms:
        answer = f.save(commit=False)
        answer.gospel_trip = gt
        answer.trainee = trainee
        answer.question = Question.objects.get(id=f.prefix)
        answer.save()
      return HttpResponseRedirect("")
    else:
      context['answer_forms'] = answer_forms
  else:
    for q in Question.objects.filter(section__gospel_trip=gt):
      answer = Answer.objects.get_or_create(trainee=trainee, gospel_trip=gt, question=q)[0]
      answer_forms.append(AnswerForm(prefix=q.id, instance=answer))
    context['answer_forms'] = answer_forms
  return render(request, 'gospel_trips/gospel_trips.html', context=context)


class GospelTripResponseView(GroupRequiredMixin, TemplateView):
  template_name = 'gospel_trips/gospel_trip_responses.html'
  group_required = ['training_assistant']

  def get_context_data(self, **kwargs):
    ctx = super(GospelTripResponseView, self).get_context_data(**kwargs)
    gt = GospelTrip.objects.get(pk=self.kwargs['pk'])
    questions_qs = Question.objects.filter(section__gospel_trip=gt)

    questions = self.request.GET.getlist('questions', [])
    if questions:
      if -1 not in questions:
        questions_qs = questions_qs.filter(id__in=questions)

    answer_sets = []
    for q in questions_qs:
      answer_sets.append(Answer.objects.filter(gospel_trip=gt, question=q))
    ctx['questions'] = Question.objects.filter(section__gospel_trip=gt)
    ctx['answer_sets'] = answer_sets
    ctx['page_title'] = 'Gospel Trip Response Report'
    return ctx


class DestinationEditorView(GroupRequiredMixin, TemplateView):
  template_name = 'gospel_trips/destination_editor.html'
  group_required = ['training_assistant']

  def get_context_data(self, **kwargs):
    context = super(DestinationEditorView, self).get_context_data(**kwargs)
    gt = GospelTrip.objects.get(pk=self.kwargs['pk'])
    context['page_title'] = 'Destination Editor'
    context['destinations'] = Destination.objects.filter(gospel_trip=gt)
    return context


def destination_add(request, pk):
  gt = get_object_or_404(GospelTrip, pk=pk)
  if request.method == "POST":
    name = request.POST.get('destination_name', None)
    if name:
      obj, _ = Destination.objects.get_or_create(gospel_trip=gt, name=name)
  return redirect('gospel_trips:destination-editor', pk=pk)


def destination_remove(request, pk):
  get_object_or_404(GospelTrip, pk=pk)
  if request.method == "POST":
    destinations = request.POST.getlist('destinations', [])
    if destinations:
      to_remove = Destination.objects.filter(id__in=destinations)
      to_remove.delete()
  return redirect('gospel_trips:destination-editor', pk=pk)


def destination_edit(request, pk):
  get_object_or_404(GospelTrip, pk=pk)
  if request.method == "POST":
    destination = request.POST.get('destination', None)
    name = request.POST.get('destination_edit', None)
    if name and destination:
      obj = get_object_or_404(Destination, pk=destination)
      obj.name = name
      obj.save()
  return redirect('gospel_trips:destination-editor', pk=pk)

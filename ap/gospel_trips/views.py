# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from accounts.models import Trainee
from aputils.decorators import group_required
from aputils.trainee_utils import trainee_from_user
from braces.views import GroupRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from .forms import AnswerForm, GospelTripForm, SectionFormSet
from .models import Answer, Destination, GospelTrip, Question


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
        AnswerForm(request.POST, prefix=q.id, instance=answer, gospel_trip__pk=pk)
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
      answer_forms.append(AnswerForm(prefix=q.id, instance=answer, gospel_trip__pk=pk))
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
    gt = get_object_or_404(GospelTrip, pk=self.kwargs['pk'])
    context['page_title'] = 'Destination Editor'
    context['destinations'] = Destination.objects.filter(gospel_trip=gt).order_by('name')
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


class DestinationByPreferenceView(GroupRequiredMixin, TemplateView):
  template_name = 'gospel_trips/by_preference.html'
  group_required = ['training_assistant']

  def get_context_data(self, **kwargs):
    context = super(DestinationByPreferenceView, self).get_context_data(**kwargs)
    gt = get_object_or_404(GospelTrip, pk=self.kwargs['pk'])
    dest_choices = [{'id': 0, 'name': ''}]
    dest_choices.extend([d for d in Destination.objects.filter(gospel_trip=gt).values('id', 'name')])
    context['destinations'] = dest_choices
    context['by_preference'] = self.get_trainee_dict(gt)
    context['page_title'] = 'Destination By Preference'
    return context

  def get_trainee_dict(self, gospel_trip):
    data = []
    for t in Trainee.objects.all():
      answer_set = t.answer_set.filter(gospel_trip=gospel_trip).values('response', 'question__instruction')
      data.append({
        'id': t.id,
        'name': t.full_name,
        'term': t.current_term,
        'locality': t.locality,
        'destination': 0,
      })
      dest = t.destination_set.filter(gospel_trip=gospel_trip)
      if dest.exists():
        data[-1]['destination'] = dest.first().id
      for a in answer_set:
        if 'Preference 2' in a['question__instruction']:
          if a['response']:
            data[-1]['preference_2'] = Destination.objects.get(id=a['response']).name
        if 'Preference 3' in a['question__instruction']:
          if a['response']:
            data[-1]['preference_3'] = Destination.objects.get(id=a['response']).name
        if 'Preference 1' in a['question__instruction']:
          if a['response']:
            data[-1]['preference_1'] = Destination.objects.get(id=a['response']).name
    return data


def assign_destination(request, pk):
  if request.method == "POST":
    for k, v in request.POST.items():
      if 'destination_select' in k:
        try:
          tr = Trainee.objects.get(id=k.split('_')[-1])
          new_dest = Destination.objects.get(id=v)
          gt = GospelTrip.objects.get(id=pk)
          old_dests = tr.destination_set.filter(gospel_trip=gt)
          if old_dests.exists():
            old_dest = old_dests.first()
            old_dest.trainees.remove(tr)
            old_dest.save()
          new_dest.trainees.add(tr)
          new_dest.save()
          JsonResponse({'success': True})
        except ObjectDoesNotExist:
          JsonResponse({'success': False})
    return JsonResponse({'success': False})
  return JsonResponse({'success': False})


def assign_team_contact(request, pk):
  '''Make sure to call assign_destination first'''
  if request.method == "POST":
    trainee_id = request.POST.get('team_contact_selection', 0)
    try:
      gt = GospelTrip.objects.get(id=pk)
      tr = Trainee.objects.get(id=trainee_id)
      dests = tr.destination_set.filter(gospel_trip=gt)
      if dests.exists():
        dest = dests.first()
        dest.team_contact = tr
        dest.save()
      return JsonResponse({'success': True})
    except ObjectDoesNotExist:
      return JsonResponse({'success': False})
  return JsonResponse({'success': False})

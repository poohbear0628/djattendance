# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from accounts.models import Trainee
from aputils.decorators import group_required
from aputils.trainee_utils import trainee_from_user
from braces.views import GroupRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from .forms import AnswerForm, GospelTripForm, SectionFormSet
from .models import Answer, Destination, GospelTrip, Question
from .utils import export_to_json, import_from_json


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


@group_required(['training_assistant'])
def gospel_trip_admin_delete(request, pk):
  gt = get_object_or_404(GospelTrip, pk=pk)
  if request.is_ajax and request.method == "DELETE":
    gt.delete()
  return JsonResponse({'success': True})


@group_required(['training_assistant'])
def gospel_trip_admin_duplicate(request, pk):
  gt = get_object_or_404(GospelTrip, pk=pk)
  path = export_to_json(gt)
  import_from_json(path)
  return redirect('gospel_trips:admin-create')


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
    # TODO: Improve performance
    data = []
    dest_dict = Destination.objects.filter(gospel_trip=gospel_trip).values('id', 'name')
    qs = Trainee.objects.select_related('locality__city').prefetch_related('team_contact', 'destination')
    all_answers = gospel_trip.answer_set.filter(question__instruction__icontains='preference')
    for t in qs:
      answer_set = all_answers.filter(trainee=t).values('response', 'question__instruction')
      data.append({
        'id': t.id,
        'name': t.full_name,
        'term': t.current_term,
        'locality': t.locality.city.name,
        'destination': 0,
        'team_contact': t.team_contact.filter(gospel_trip=gospel_trip).exists()
      })
      dest = dest_dict.filter(trainees__in=[t])
      if dest.exists():
        data[-1]['destination'] = dest.first()['id']
      for a in answer_set:
        if 'Preference 2' in a['question__instruction']:
          if a['response']:
            data[-1]['preference_2'] = dest_dict.get(id=a['response'])['name']
        if 'Preference 3' in a['question__instruction']:
          if a['response']:
            data[-1]['preference_3'] = dest_dict.get(id=a['response'])['name']
        if 'Preference 1' in a['question__instruction']:
          if a['response']:
            data[-1]['preference_1'] = dest_dict.get(id=a['response'])['name']
    return data


class DestinationByGroupView(GroupRequiredMixin, TemplateView):
  template_name = 'gospel_trips/by_group.html'
  group_required = ['training_assistant']

  def post(self, request, *args, **kwargs):
    trainee_ids = request.POST.getlist('choose_trainees', [])
    dest_id = request.POST.get('destination', 0)
    if dest_id:
      dest = Destination.objects.get(id=dest_id)
      new_set = Trainee.objects.filter(id__in=trainee_ids)
      dest.trainees.set(new_set)
      dest.save()
    context = self.get_context_data()
    return super(DestinationByGroupView, self).render_to_response(context)

  def get_context_data(self, **kwargs):
    context = super(DestinationByGroupView, self).get_context_data(**kwargs)
    gt = get_object_or_404(GospelTrip, pk=self.kwargs['pk'])
    all_destinations = Destination.objects.filter(gospel_trip=gt)
    if self.request.method == 'POST':
      destination = self.request.POST.get('destination', all_destinations.first().id)
    else:
      destination = self.request.GET.get('destination', all_destinations.first().id)
    dest = Destination.objects.get(id=destination)
    to_exclude = all_destinations.filter(~Q(trainees=None), ~Q(id=dest.id))

    context['chosen'] = dest.trainees.values_list('id', flat=True)
    context['choose_from'] = Trainee.objects.exclude(id__in=to_exclude.values_list('trainees__id'))
    if 'destinit' not in context:
      context['destinit'] = dest.id
    context['all_destinations'] = all_destinations
    context['page_title'] = 'Destination By Group'
    context['post_url'] = reverse('gospel_trips:by-group', kwargs={'pk': gt.id})
    return context


class RostersAllTeamsView(TemplateView):
  template_name = 'gospel_trips/rosters_all_teams.html'

  def get_context_data(self, **kwargs):
    context = super(RostersAllTeamsView, self).get_context_data(**kwargs)
    gt = get_object_or_404(GospelTrip, pk=self.kwargs['pk'])
    all_destinations = Destination.objects.filter(gospel_trip=gt)
    context['destination'] = all_destinations.first()
    context['page_title'] = "Rosters: All Teams"
    if self.request.user.has_group(['training_assistant']):
      context['trainees'] = self.get_trainee_dict(all_destinations)
    return context

  def get_trainee_dict(self, destination_qs):
    data = []
    contacts = destination_qs.values_list('team_contact', flat=True)
    for t in Trainee.objects.all():
      data.append({
        'name': t.full_name,
        'id': t.id,
        'team_contact': t.id in contacts,
        'destination': destination_qs.filter(trainees=t).first()
      })
    return data


class RostersIndividualTeamView(GroupRequiredMixin, TemplateView):
  template_name = 'gospel_trips/rosters_individual_team.html'
  group_required = ['training_assistant']

  def get_context_data(self, **kwargs):
    context = super(RostersIndividualTeamView, self).get_context_data(**kwargs)
    gt = get_object_or_404(GospelTrip, pk=self.kwargs['pk'])
    all_destinations = Destination.objects.filter(gospel_trip=gt)
    destination = self.request.GET.get('destination', all_destinations.first().id)
    context['all_destinations'] = all_destinations
    context['destination'] = destination
    context['page_title'] = "Rosters: Individual Teams"
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


def assign_destination(request, pk):
  if request.is_ajax() and request.method == "POST":
    dest_id = request.POST.get('destination_id', 0)
    trainee_id = request.POST.get('trainee_id', 0)
    try:
      tr = Trainee.objects.get(id=trainee_id)
      gt = GospelTrip.objects.get(id=pk)
      old_dests = tr.destination.filter(gospel_trip=gt)
      if old_dests.exists():
        # Even if dest_id is 0, trainee is still removed
        old_dest = old_dests.first()
        old_dest.trainees.remove(tr)
        if old_dest.team_contact == tr:
          old_dest.team_contact = None
        old_dest.save()
      new_dest = Destination.objects.get(id=dest_id)
      new_dest.trainees.add(tr)
      new_dest.save()
      JsonResponse({'success': True})
    except ObjectDoesNotExist:
      JsonResponse({'success': False})
    return JsonResponse({'success': False})
  return JsonResponse({'success': False})


def assign_team_contact(request, pk):
  '''Make sure to call assign_destination first'''
  if request.is_ajax() and request.method == "POST":
    trainee_id = request.POST.get('trainee_id', 0)
    is_contact = request.POST.get('is_contact', 'false') == 'true'
    try:
      gt = GospelTrip.objects.get(id=pk)
      tr = Trainee.objects.get(id=trainee_id)
      dests = tr.destination.filter(gospel_trip=gt)
      if dests.exists():
        dest = dests.first()
        if is_contact:
          dest.team_contact = tr
        else:
          if dest.team_contact == tr:
            dest.team_contact = None
        dest.save()
      return JsonResponse({'success': True})
    except ObjectDoesNotExist:
      return JsonResponse({'success': False})
  return JsonResponse({'success': False})

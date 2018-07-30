# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from accounts.models import Trainee
from aputils.decorators import group_required
from aputils.trainee_utils import is_trainee, trainee_from_user
from braces.views import GroupRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from .forms import AnswerForm, GospelTripForm, LocalImageForm, SectionFormSet
from .models import Answer, Destination, GospelTrip, Question, Section
from .utils import (export_to_json, get_airline_codes, get_airport_codes,
                    import_from_json)


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


def gospel_trip_base(request):
  # TODO: make this more robust
  return HttpResponseRedirect(reverse('gospel_trips:gospel-trip', kwargs={'pk': GospelTrip.objects.order_by('open_time').first().pk}))


def gospel_trip_trainee(request, pk):
  gt = get_object_or_404(GospelTrip, pk=pk)
  context = {'page_title': gt.name}
  if is_trainee(request.user):
    trainee = trainee_from_user(request.user)
  else:
    trainee = Trainee.objects.first()
    context['preview'] = trainee.full_name

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
  context['AIRPORT_CODES'] = json.dumps(get_airport_codes())
  context['AIRLINE_CODES'] = json.dumps(get_airline_codes())
  return render(request, 'gospel_trips/gospel_trips.html', context=context)


class GospelTripReportView(GroupRequiredMixin, TemplateView):
  template_name = 'gospel_trips/gospel_trip_report.html'
  group_required = ['training_assistant']

  @staticmethod
  def get_trainee_dict(destination_qs, question_qs):
    data = []
    contacts = destination_qs.values_list('team_contact', flat=True)
    destination_names = destination_qs.values('name')
    for t in Trainee.objects.all():
      entry = {
          'name': t.full_name,
          'id': t.id,
          'team_contact': t.id in contacts,
          'destination': destination_qs.filter(trainees=t).first(),
          'responses': []}
      responses = question_qs.filter(answer__trainee=t).values('answer_type', 'answer__response')
      for r in responses:
        if r['answer_type']['type'] == 'destinations':
          r['answer__response'] = destination_names.get(id=r['answer__response'])['name']
      entry['responses'] = responses
      data.append(entry)
    return data

  def get_context_data(self, **kwargs):
    ctx = super(GospelTripReportView, self).get_context_data(**kwargs)
    gt = GospelTrip.objects.get(pk=self.kwargs['pk'])
    questions_qs = Question.objects.filter(section__gospel_trip=gt)
    all_destinations = Destination.objects.filter(gospel_trip=gt)

    questions = self.request.GET.getlist('questions', [0])
    questions_qs = questions_qs.filter(id__in=questions)

    ctx['questions'] = questions_qs
    ctx['chosen'] = questions_qs.values_list('id', flat=True)
    ctx['sections'] = Section.objects.filter(gospel_trip=gt)
    ctx['trainees'] = self.get_trainee_dict(all_destinations, questions_qs)
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

  @staticmethod
  def get_trainee_dict(gospel_trip):
    data = []
    dest_dict = Destination.objects.filter(gospel_trip=gospel_trip).values('id', 'name', 'team_contact')
    contacts = Destination.objects.filter(gospel_trip=gospel_trip).values_list('team_contact', flat=True)
    qs = Trainee.objects.select_related('locality__city').prefetch_related('team_contact', 'destination')
    all_answers = gospel_trip.answer_set.filter(question__instruction__icontains='preference').values('response', 'question__instruction')
    for t in qs:
      answer_set = all_answers.filter(trainee=t)
      data.append({
        'id': t.id,
        'name': t.full_name,
        'term': t.current_term,
        'locality': t.locality.city.name,
        'destination': 0,
        'team_contact': t.id in contacts
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

  def get_context_data(self, **kwargs):
    context = super(DestinationByPreferenceView, self).get_context_data(**kwargs)
    gt = get_object_or_404(GospelTrip, pk=self.kwargs['pk'])
    dest_choices = [{'id': 0, 'name': ''}]
    dest_choices.extend([d for d in Destination.objects.filter(gospel_trip=gt).values('id', 'name')])
    context['destinations'] = dest_choices
    context['by_preference'] = self.get_trainee_dict(gt)
    context['page_title'] = 'Destination By Preference'
    return context


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

  @staticmethod
  def get_trainee_dict(destination_qs):
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

  def get_context_data(self, **kwargs):
    context = super(RostersAllTeamsView, self).get_context_data(**kwargs)
    gt = get_object_or_404(GospelTrip, pk=self.kwargs['pk'])
    all_destinations = Destination.objects.filter(gospel_trip=gt)
    if is_trainee(self.request.user) and all_destinations.filter(trainees=self.request.user).exists():
      context['destination'] = all_destinations.get(trainees=self.request.user)
    if self.request.user.has_group(['training_assistant']):
      context['trainees'] = self.get_trainee_dict(all_destinations)
    context['page_title'] = "Rosters: All Teams"
    return context


class RostersIndividualTeamView(GroupRequiredMixin, TemplateView):
  template_name = 'gospel_trips/rosters_individual_team.html'
  group_required = ['training_assistant']

  def get_context_data(self, **kwargs):
    context = super(RostersIndividualTeamView, self).get_context_data(**kwargs)
    gt = get_object_or_404(GospelTrip, pk=self.kwargs['pk'])
    all_destinations = Destination.objects.filter(gospel_trip=gt)
    destinations = self.request.GET.getlist('destinations', [])
    chosen_destinations = all_destinations.filter(id__in=destinations)
    context['all_destinations'] = all_destinations
    context['destinations'] = chosen_destinations
    context['chosen'] = chosen_destinations.values_list('id', flat=True)
    context['page_title'] = "Rosters: Individual Teams"
    return context


def destination_add(request, pk):
  gt = get_object_or_404(GospelTrip, pk=pk)
  if request.method == "POST":
    name = request.POST.get('destination_name', None)
    if name:
      Destination.objects.get_or_create(gospel_trip=gt, name=name)
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
    is_contact = request.POST.get('is_contact', 'false') == 'true'
    try:
      tr = Trainee.objects.get(id=trainee_id)
      gt = GospelTrip.objects.get(id=pk)
      old_dests = tr.destination.filter(gospel_trip=gt)
      if old_dests.exists():
        # Even if dest_id is 0, trainee is still removed
        old_dest = old_dests.first()
        old_dest.remove_trainee(tr)
      new_dest = Destination.objects.get(id=dest_id)
      new_dest.trainees.add(tr)
      new_dest.save()
      new_dest.set_team_contact(tr, is_contact=is_contact)
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
        dest.set_team_contact(tr, is_contact=is_contact)
        dest.save()
      return JsonResponse({'success': True})
    except ObjectDoesNotExist:
      return JsonResponse({'success': False})
  return JsonResponse({'success': False})


@csrf_exempt  # TODO: add csrf
def upload_image(request):
  form = LocalImageForm(request.POST, request.FILES)
  if form.is_valid():
    form.save()
    # TODO: fix invalid JSON
    return JsonResponse({'success': 'True'}, status=200)
  errors = {f: e.get_json_data() for f, e in form.errors.items()}
  return JsonResponse({'success': 'False', 'errors': errors}, status=500)

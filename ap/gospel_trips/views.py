# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from braces.views import GroupRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView

from .forms import GospelTripAdminForm, SectionFormSet, AnswerForm
from .models import GospelTripAdmin, Question
from aputils.trainee_utils import trainee_from_user


# Create your views here.
class GospelTripAdminView(GroupRequiredMixin, CreateView):
  model = GospelTripAdmin
  template_name = 'gospel_trips/gospel_trips_admin.html'
  form_class = GospelTripAdminForm
  group_required = ['training_assistant']

  def get_context_data(self, **kwargs):
    ctx = super(GospelTripAdminView, self).get_context_data(**kwargs)
    ctx['gospel_trips'] = GospelTripAdmin.objects.all()
    ctx['page_title'] = 'Gospel Trip Admin'
    return ctx


def gospel_trip_admin_update(request, pk):
  admin = get_object_or_404(GospelTripAdmin, pk=pk)
  context = {'page_title': 'Gospel Trip Editor'}

  if request.method == "POST":
    form = GospelTripAdminForm(request.POST, instance=admin)
    form_set = SectionFormSet(request.POST, instance=admin)
    if form.is_valid() and form_set.is_valid():
      form.save()
      form_set.save()
      return HttpResponseRedirect("")
    else:
      context['admin_form'] = form
      context['section_formset'] = form_set
      context['last_form_counter'] = len(form_set)
  else:
    section_formset = SectionFormSet(instance=admin)
    context['admin_form'] = GospelTripAdminForm(instance=admin)
    context['section_formset'] = section_formset
    context['last_form_counter'] = len(section_formset)
  return render(request, 'gospel_trips/gospel_trips_admin_update.html', context=context)


def gospel_trip_trainee(request, pk):
  admin = get_object_or_404(GospelTripAdmin, pk=pk)
  trainee = trainee_from_user(request.user)
  # gt = get_object_or_404(GospelTrip, admin=admin, trainee=trainee)
  context = {'page_title': admin.name}
  context['gospel_trip'] = admin
  if request.method == "POST":
    print request.POST
  else:
    qids = admin.section_set.exclude(question=None).values_list('question', flat=True)
    context['answer_form'] = AnswerForm()
  return render(request, 'gospel_trips/gospel_trips.html', context=context)

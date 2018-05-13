# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from braces.views import GroupRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView, UpdateView

from .forms import GospelTripAdminForm, SectionFormSet
from .models import GospelTripAdmin, Instruction, Question, Section


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
    context['admin_form'] = GospelTripAdminForm(instance=admin)
    context['section_formset'] = SectionFormSet(instance=admin)
  return render(request, 'gospel_trips/gospel_trips_admin_update.html', context=context)

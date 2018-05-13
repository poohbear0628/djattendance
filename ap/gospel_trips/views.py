# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from braces.views import GroupRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404
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
  if request.method == "GET":

    context = {
      'admin_form': GospelTripAdminForm(instance=admin),
      'section_formset': SectionFormSet(),
    }
  return render(request, 'gospel_trips/gospel_trips_admin_update.html', context=context)

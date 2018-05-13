# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from braces.views import GroupRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import CreateView

from .forms import GospelTripAdminForm, SectionFormSet
from .models import GospelTripAdmin, Instruction, Question, Section


# Create your views here.
class GospelTripAdminView(GroupRequiredMixin, CreateView):
  model = GospelTripAdmin
  template_name = 'gospel_trips/gospel_trips_admin.html'
  form_class = GospelTripAdminForm
  group_required = ['training_assistant']
  success_url = reverse_lazy('gospel_trips:gospel-trips-admin')

  def get_context_data(self, **kwargs):
    ctx = super(GospelTripAdminView, self).get_context_data(**kwargs)
    ctx['gospel_trips'] = GospelTripAdmin.objects.all()
    ctx['page_title'] = 'Gospel Trip Admin'
    return ctx
# def create_gospel_trip(request):

#   if request.method == "GET":
#     admin_qs = GospelTripAdmin.objects.all()
#     admin_form = GospelTripAdminForm()

#     context = {
#       'admin_qs': admin_qs,
#       'admin_form': admin_form,
#       'section_formset': SectionFormSet(),
#     }
#   return render(request, 'gospel_trips/new_gospel_trip.html', context=context)

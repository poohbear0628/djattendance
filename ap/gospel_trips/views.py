# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from .forms import GospelTripAdminForm, SectionFormSet
from gospel_trips.models import GospelTripAdmin, Section, Instruction, Question


# Create your views here.
def create_gospel_trip(request):

  if request.method == "GET":
    admin_qs = GospelTripAdmin.objects.all()
    admin_form = GospelTripAdminForm()

    context = {
      'admin_qs': admin_qs,
      'admin_form': admin_form,
      'section_formset': SectionFormSet(),
    }
  return render(request, 'gospel_trips/new_gospel_trip.html', context=context)

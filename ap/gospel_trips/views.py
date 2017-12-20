# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from gospel_trips.models import GospelTrip
from gospel_trips.forms import gospel_trip_forms


# Create your views here.
def create_gospel_trip(request, pk):
  ctx = {}
  gt, created = GospelTrip.objects.get_or_create(id=1)

  if request.method == 'POST':
    data = request.POST
    print data

    all_forms = gospel_trip_forms(gt, data)

    print all_forms

    if all([form.is_valid() for form in all_forms]):

      for form in all_forms:

        if form.__class__.__name__ == 'GospelTripForm':
          obj = form.save(commit=False)
          if obj.name:
            form.save()

        elif form.__class__.__name__ == 'SectionForm':
          print form
          obj = form.save(commit=False)
          obj.gospel_trip = gt
          obj.index = int(form.prefix[1:])
          if obj.name:
            form.save()

        elif form.__class__.__name__ == 'InstructionForm':
          obj = form.save(commit=False)
          obj.index = int(form.prefix[1:])
          if obj.name or obj.instruction:
            obj.save()

        elif form.__class__.__name__ == 'QuestionForm':
          obj = form.save(commit=False)
          obj.index = int(form.prefix[1:])
          if obj.instruction:
            obj.save()

      print 'good!'

    return HttpResponseRedirect(gt.get_absolute_url())
  else:  # GET

    all_forms = gospel_trip_forms(gt)
    ctx['all_forms'] = all_forms
    print all_forms
    return render(request, 'gospel_trips/new_gospel_trip.html', ctx)

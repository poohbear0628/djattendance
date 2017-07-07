from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .models import RoomReservation
from .forms import RoomReservationForm
from accounts.models import Trainee

import json
from datetime import datetime, timedelta
from django.core.serializers import serialize

class RoomReservationSubmit(CreateView):
  model = RoomReservation
  template_name = 'room_reservations/room_reservation.html'
  form_class = RoomReservationForm
  #context_object_name = 'room_reservation'

  def get_context_data(self, **kwargs):
    ctx = super(RoomReservationSubmit, self).get_context_data(**kwargs)
    #room_reservaton = self.get_object()
    reservations = RoomReservation.objects.filter(status='P') #order by submission date?
    ctx['reservations'] = reservations
    ctx['page_title'] = 'Submit New Request'
    ctx['button_label'] = 'Submit'
    return ctx

  def form_valid(self, form):
    room_reservation = form.save(commit=False)
    room_reservation.trainee = Trainee.objects.get(id = self.request.user.id)

    # check valid date (at least 24 hrs in advance)
    start_dt = datetime.combine(room_reservation.date, room_reservation.start)
    diff = start_dt - datetime.now()
    if diff.seconds <= 83699: #less than 24 hours
      pass #return submitted too late!
    # check valid time range (end is after start)
    elif room_reservation.end <= room_reservation.start:
      pass #return invalid time range

    room_reservation.save()
    return HttpResponseRedirect(reverse('room_reservations:room-reservation-submit'))

class RoomReservationUpdate(UpdateView):
  model = RoomReservation
  template_name = 'room_reservations/room_reservation.html'
  form_class = RoomReservationForm
  context_object_name = 'room_reservation'

  def get_context_data(self, **kwargs):
    ctx = super(RoomReservationUpdate, self).get_context_data(**kwargs)
    room_reservation = self.get_object()
    reservations = RoomReservation.objects.exclude(id=room_reservation.id).filter(status='P')
    ctx['reservations'] = reservations
    ctx['page_title'] = 'Edit Request'
    ctx['button_label'] = 'Update'
    return ctx

  def form_valid(self, form):
    room_reservation = form.save(commit=False)

    # other form validation (e.g., valid time range, valid date, etc.)
    room_reservation.save()
    return HttpResponseRedirect(reverse('room_reservations:room-reservation-submit'))

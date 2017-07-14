from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .models import RoomReservation
from .forms import RoomReservationForm
from accounts.models import Trainee

import json
from datetime import datetime, timedelta
from django.core.serializers import serialize

from braces.views import GroupRequiredMixin

class RoomReservationSubmit(CreateView):
  model = RoomReservation
  template_name = 'room_reservations/room_reservation.html'
  form_class = RoomReservationForm

  def get_context_data(self, **kwargs):
    ctx = super(RoomReservationSubmit, self).get_context_data(**kwargs)
    reservations = RoomReservation.objects.filter(status='P') #order by submission date?
    ctx['reservations'] = reservations
    ctx['page_title'] = 'Submit New Request'
    ctx['button_label'] = 'Submit'
    return ctx

  def form_valid(self, form):
    room_reservation = form.save(commit=False)
    room_reservation.trainee = Trainee.objects.get(id = self.request.user.id)
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
    room_reservation.save()
    return HttpResponseRedirect(reverse('room_reservations:room-reservation-submit'))

class TARoomReservationList(GroupRequiredMixin, TemplateView):
  model = RoomReservation
  group_required = ['administration']
  template_name = 'room_reservations/ta_list.html'

  def get_context_data(self, **kwargs):
    ctx = super(TARoomReservationList, self).get_context_data(**kwargs)
    reservations = RoomReservation.objects.filter(status='P')
    ctx['reservations'] = reservations
    return ctx

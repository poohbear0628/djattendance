from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q

from .models import RoomReservation
from .forms import RoomReservationForm
from accounts.models import Trainee, TrainingAssistant, User
from rooms.models import Room
from aputils.decorators import group_required
from aputils.trainee_utils import is_TA
from aputils.utils import modify_model_status

import json
from datetime import datetime, timedelta, time
from braces.views import GroupRequiredMixin

TIMES_AM = ['%s:%s%s' % (h, m, 'am')\
  for h in (list(range(6,12))) \
  for m in ('00', '30')]

TIMES_PM = ['%s:%s%s' % (h, m, 'pm')\
  for h in (list(range(1,12))) \
  for m in ('00', '30')]

TIMES = TIMES_AM + TIMES_PM


class RoomReservationSubmit(CreateView):
  model = RoomReservation
  template_name = 'room_reservations/room_reservation.html'
  form_class = RoomReservationForm

  def get_success_url(self, **kwargs):
    if is_TA(self.request.user):
      return reverse_lazy('room_reservations:room-reservation-schedule')
    else:
      return reverse_lazy('room_reservations:room-reservation-submit')

  def get_context_data(self, **kwargs):
    ctx = super(RoomReservationSubmit, self).get_context_data(**kwargs)

    approved_reservations = RoomReservation.objects.filter(status='A')
    reservations = RoomReservation.objects.filter(requester=self.request.user)
    rooms = Room.objects.all()
    approved_reservations_json = serialize('json', approved_reservations)
    rooms_json = serialize('json', rooms)
    bro_rooms = Room.objects.filter(Q(access='B'))
    sis_rooms = Room.objects.filter(Q(access='S'))

    ctx['reservations'] = approved_reservations_json
    ctx['requested_reservations'] = reservations
    ctx['rooms_list'] = rooms_json
    ctx['bro_rooms_list'] = serialize('json', bro_rooms)
    ctx['sis_rooms_list'] = serialize('json', sis_rooms)
    ctx['times_list'] = TIMES
    ctx['page_title'] = 'Create Room Reservation' if is_TA(self.request.user) else \
                        'Request Room Reservation'
    ctx['button_label'] = 'Submit'
    return ctx

  def form_valid(self, form):
    room_reservation = form.save(commit=False)
    user_id = self.request.user.id
    room_reservation.requester = User.objects.get(id=user_id)
    if TrainingAssistant.objects.filter(id=user_id).exists():
      room_reservation.status = 'A'
    room_reservation.save()
    return super(RoomReservationSubmit, self).form_valid(form)

class RoomReservationUpdate(RoomReservationSubmit, UpdateView):
  def get_context_data(self, **kwargs):
    ctx = super(RoomReservationUpdate, self).get_context_data(**kwargs)
    ctx['page_title'] = 'Edit Reservation'
    ctx['button_label'] = 'Update'
    return ctx

class RoomReservationDelete(RoomReservationSubmit, DeleteView):
  model = RoomReservation

class TARoomReservationList(GroupRequiredMixin, TemplateView):
  model = RoomReservation
  group_required = ['administration']
  template_name = 'room_reservations/ta_list.html'

  def get_context_data(self, **kwargs):
    ctx = super(TARoomReservationList, self).get_context_data(**kwargs)
    reservations = RoomReservation.objects.filter(Q(status='P')|Q(status='F'))
    ctx['reservations'] = reservations
    return ctx

class RoomReservationSchedule(GroupRequiredMixin, RoomReservationSubmit, TemplateView):
  object = None
  group_required = ['administration']
  template_name = 'room_reservations/schedule.html'

reservation_modify_status = modify_model_status(RoomReservation, reverse_lazy('room_reservations:ta-room-reservation-list'))

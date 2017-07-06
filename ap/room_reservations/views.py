from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .models import RoomReservation
from .forms import RoomReservationForm
from accounts.models import Trainee

import json
from django.core.serializers import serialize

class RoomReservationSubmit(CreateView):
    model = RoomReservation
    template_name = 'room_reservations/room_reservation.html'
    form_class = RoomReservationForm
    #context_object_name = 'room_reservation'
    

    def get_context_data(self, **kwargs):
        ctx = super(RoomReservationSubmit, self).get_context_data(**kwargs)
        #room_reservaton = self.get_object()
        rrs = RoomReservation.objects.filter(status='P')
        reservations = []
        for rr in rrs:
          reservations.append({
            'status': rr.status,
             'group': rr.group,
             'date': rr.date,
             'start': rr.start,
             'end': rr.end,
             'room': rr.room,
             'group_size': rr.group_size,
             'frequency': rr.frequency,
             'reason': rr.reason
          })
        ctx['reservations'] = reservations
        ctx['start'] = 'hello'
        return ctx

    def form_valid(self, form):
        room_reservation = form.save(commit=False)
        room_reservation.trainee = Trainee.objects.get(id = self.request.user.id)
        print room_reservation.trainee
        room_reservation.save()
        return HttpResponseRedirect(reverse('room_reservations:room-reservation-submit'))

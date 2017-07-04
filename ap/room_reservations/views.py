from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView
from .models import RoomReservation
from .forms import RoomReservationForm

import json

class RoomReservationSubmit(CreateView):
    model = RoomReservation
    template_name = 'room_reservations/room_reservation.html'
    form_class = RoomReservationForm
    #context_object_name = 'room_reservation'
    

    def get_context_data(self, **kwargs):
        ctx = super(RoomReservationSubmit, self).get_context_data(**kwargs)
        #room_reservaton = self.get_object()
        reservations = []
        reservations.append({
          'status': 'Pending',
          'group': 'LB Team',
          'date': '07/02/2017',
          'start': '16:00',
          'end': '17:30',
          'room': 'NE3',
          'group_size': '25',
          'frequency' : 'All Term',
          'reason': 'Team Fellowship'
        })
        reservations.append({
          'status': 'Approved',
          'group': '2nd Year Bros',
          'date': '07/01/2017',
          'start': '12:00',
          'end': '13:30',
          'room': 'MC',
          'group_size': '100',
          'frequency' : 'Once',
          'reason': 'Term Prayer'
        })
        reservations.append({
          'status': 'Denied',
          'group': 'Grace 05&19',
          'date': '07/05/2017',
          'start': '16:00',
          'end': '17:30',
          'room': 'NE209',
          'group_size': '15',
          'frequency' : 'All Term',
          'reason': 'PSRP'
        })
        ctx['reservations'] = reservations
        ctx['start'] = 'hello'
        return ctx

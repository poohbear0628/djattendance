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
          'Group': 'LB Team',
          'Date': '07/02/2017',
          'Start': '16:00',
          'End': '17:30',
          'Room': 'NE3',
          'Group Size': '25',
          'Frequency' : 'All Term',
          'Reason': 'Team Fellowship'
        })
        reservations.append({
          'Group': '2nd Year Bros',
          'Date': '07/01/2017',
          'Start': '12:00',
          'End': '13:30',
          'Room': 'MC',
          'Group Size': '100',
          'Frequency' : 'Once',
          'Reason': 'Term Prayer'
        })
        reservations.append({
          'Group': 'Grace 05&19',
          'Date': '07/05/2017',
          'Start': '16:00',
          'End': '17:30',
          'Room': 'NE209',
          'Group Size': '15',
          'Frequency' : 'All Term',
          'Reason': 'PSRP'
        })
        ctx['reservations'] = reservations
        ctx['start'] = 'hello'
        return ctx

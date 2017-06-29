from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView
from .models import RoomReservation
from .forms import RoomReservationForm


class RoomReservationSubmit(CreateView):
    model = RoomReservation
    template_name = 'room_reservations/room_reservation.html'
    form_class = RoomReservationForm
    #context_object_name = 'room_reservation'

    def get_context_data(self, **kwargs):
        ctx = super(RoomReservationSubmit, self).get_context_data(**kwargs)
        #room_reservaton = self.get_object()
        ctx['start'] = 'hello'
        return ctx

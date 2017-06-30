from django import forms

from .models import RoomReservation

class RoomReservationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RoomReservationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = RoomReservation
        fields = ['group', 'date', 'start', 'end', 'room', 'group_size', 'frequency', 'reason']

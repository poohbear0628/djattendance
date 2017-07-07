from django import forms

from .models import RoomReservation
from aputils.widgets import SelectTimeWidget, DatePicker

class RoomReservationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RoomReservationForm, self).__init__(*args, **kwargs)
        self.fields['start'].widget = SelectTimeWidget(twelve_hr=True, use_seconds=False, minute_step=30, required=True)
        self.fields['end'].widget = SelectTimeWidget(twelve_hr=True, use_seconds=False, minute_step=30, required=True)
        
        req_keys = ['group', 'date', 'start', 'end', 'room', 'group_size', 'frequency', 'reason']
        for key in req_keys:
          self.fields[key].required = True

    class Meta:
        model = RoomReservation
        fields = ['group', 'date', 'start', 'end', 'room', 'group_size', 'frequency', 'reason']
        widgets = {
            'date': DatePicker(),
            }


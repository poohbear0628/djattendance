from django import forms

from bootstrap3_datetime.widgets import DateTimePicker

from .models import Announcement

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ('type', 'announcement', 'announcement_date', 'announcement_end_date')
        widgets = {'announcement_date': DateTimePicker(options={'format': 'MM/DD/YYYY HH:mm'}),
                   'announcement_end_date': DateTimePicker(options={'format': 'MM/DD/YYYY HH:mm'})}

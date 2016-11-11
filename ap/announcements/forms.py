from django import forms

from .models import Announcement

from functools import partial

DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class AnnouncementForm(forms.ModelForm):

    announcement_date = forms.DateField(widget=DateInput())
    announcement_end_date = forms.DateField(widget=DateInput())

    class Meta:
        model = Announcement
        fields = ('type', 'announcement', 'announcement_date', 'announcement_end_date')


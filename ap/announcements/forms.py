from django import forms

from django_select2 import *

from .models import Announcement
from accounts.models import Trainee

from functools import partial

DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class AnnouncementForm(forms.ModelForm):

    announcement_date = forms.DateField(widget=DateInput())
    announcement_end_date = forms.DateField(widget=DateInput())
    active_trainees = Trainee.objects.select_related().filter(is_active=True)
    trainees = ModelSelect2MultipleField(queryset=active_trainees, required=False, search_fields=['^first_name', '^last_name'])

    class Meta:
        model = Announcement
        fields = ('type', 'announcement', 'announcement_date', 'announcement_end_date', 'trainees')


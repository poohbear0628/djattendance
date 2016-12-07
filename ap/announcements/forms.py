from django import forms

from django_select2 import *

from .models import Announcement
from accounts.models import Trainee, User
from teams.models import Team
from houses.models import House
from localities.models import Locality
from aputils.trainee_utils import is_TA

from functools import partial

DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class AnnouncementForm(forms.ModelForm):
    announcement_date = forms.DateField(widget=DateInput())
    announcement_end_date = forms.DateField(widget=DateInput())
    active_trainees = Trainee.objects.select_related().filter(is_active=True)
    trainees = ModelSelect2MultipleField(queryset=active_trainees, required=False, search_fields=['^last_name', '^first_name'])

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(AnnouncementForm, self).__init__(*args, **kwargs)
        if not is_TA(user):
            del self.fields['status']
            del self.fields['TA_comments']

    class Meta:
        model = Announcement
        fields = ('type', 'status', 'announcement', 'TA_comments', 'trainee_comments', 'announcement_date', 'announcement_end_date', 'trainees')

class AnnouncementTACommentForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['TA_comments']

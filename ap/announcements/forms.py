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
  announcement_end_date = forms.DateField(widget=DateInput(), required=False)
  active_trainees = Trainee.objects.select_related().filter(is_active=True)
  trainees = ModelSelect2MultipleField(queryset=active_trainees, required=False, search_fields=['^last_name', '^first_name'])

  def __init__(self, *args, **kwargs):
    user = kwargs.pop('user', None)
    super(AnnouncementForm, self).__init__(*args, **kwargs)
    # if the user can see/modify the status, not trainee, so make it easy for approved announcements to be created by non-trainees
    self.fields['status'].initial = 'A'
    self.fields['announcement_end_date'].widget.attrs['class'] += ' hide-if-in-class hide-if-popup'
    self.fields['trainees_show'].widget.attrs['class'] = 'hide-if-in-class'
    self.fields['is_popup'].widget.attrs['class'] = 'hide-if-in-class'
    if not is_TA(user):
      del self.fields['status']
      del self.fields['TA_comments']

  def clean(self):
    cleaned_data = super(AnnouncementForm, self).clean()
    type = cleaned_data.get('type')
    end_date = cleaned_data.get('announcement_end_date')
    is_popup = cleaned_data.get('is_popup')
    if type == 'SERVE' and not end_date and not is_popup:
      self._errors["announcement_end_date"] = self.error_class(["This is a required field."])
    return cleaned_data

  class Meta:
    model = Announcement
    fields = (
      'type',
      'status',
      'announcement',
      'TA_comments',
      'trainee_comments',
      'announcement_date',
      'announcement_end_date',
      'is_popup',
      'trainees_show'
    )

class AnnouncementDayForm(forms.Form):
  announcement_day = forms.DateField(widget=DateInput(), label="Choose a date")

class AnnouncementTACommentForm(forms.ModelForm):
  class Meta:
    model = Announcement
    fields = ['TA_comments']

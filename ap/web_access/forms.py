from django import forms
from django_select2.forms import Select2Widget

from datetime import datetime

from .models import WebRequest
from aputils.widgets import DatePicker
from accounts.models import Trainee


class WebAccessRequestCreateForm(forms.ModelForm):

  date_expire = forms.DateField(widget=DatePicker(), label="Request expires after: ")
  comments = forms.CharField(
      widget=forms.Textarea(
          attrs={
              'placeholder': 'Please be as detailed and specific as possible to prevent unnecessary delays'
          }
      )
  )

  def clean_date_expire(self):
    """ Invalid form if date expire is earlier than today """
    data = self.cleaned_data['date_expire']
    if datetime.now().date() > data:
      raise forms.ValidationError("Date expire has already passed.")
    return data

  class Meta:
    model = WebRequest
    fields = ['reason', 'minutes', 'date_expire', 'comments', 'urgent']


class EShepherdingRequest(forms.Form):
  companion = forms.ModelChoiceField(
      queryset=Trainee.objects.all(),
      required=True,
      widget=Select2Widget
  )


class WebAccessRequestGuestCreateForm(WebAccessRequestCreateForm):
  class Meta:
    model = WebRequest
    fields = ['guest_name', 'reason', 'minutes', 'date_expire', 'comments', 'urgent']


class WebAccessRequestTACommentForm(forms.ModelForm):

  class Meta:
    model = WebRequest
    fields = ['TA_comments']


class DirectWebAccess(forms.Form):

  mac_address = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'placeholder': '11:22:33:44:55:66'}))
  minutes = forms.ChoiceField(choices=WebRequest.MINUTES_CHIOCES)

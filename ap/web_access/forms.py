from django import forms

from django_select2 import ModelSelect2Field

from datetime import datetime
from functools import partial

from accounts.models import Trainee
from .models import WebRequest

# Needed for JQuery datepicker UI to work
DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class WebAccessRequestCreateForm(forms.ModelForm):

    date_expire = forms.DateField(widget=DateInput())
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
    active_trainees = Trainee.objects.select_related().filter(is_active=True)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(EShepherdingRequest, self).__init__(*args, **kwargs)
        trainees = EShepherdingRequest.active_trainees.filter(team=self.user.team).exclude(pk=self.user.pk)
        self.fields['companion'] = ModelSelect2Field(queryset=trainees, required=False, search_fields=['^first_name', '^last_name'])
        self.fields['companion'].required = True


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

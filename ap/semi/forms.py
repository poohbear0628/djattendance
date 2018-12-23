from semi.models import SemiAnnual
from semi.utils import ROLL_STATUS, LOCATIONS, REQUEST_STATUS
from django import forms

class AttendanceForm(forms.Form):

  tuesday = forms.ChoiceField(choices=ROLL_STATUS, widget=forms.RadioSelect)
  wednesday = forms.ChoiceField(choices=ROLL_STATUS, widget=forms.RadioSelect)
  thursday = forms.ChoiceField(choices=ROLL_STATUS, widget=forms.RadioSelect)
  friday = forms.ChoiceField(choices=ROLL_STATUS, widget=forms.RadioSelect)
  saturday = forms.ChoiceField(choices=ROLL_STATUS, widget=forms.RadioSelect)


class LocationForm(forms.ModelForm):

  def __init__(self, *args, **kwargs):
    super(LocationForm, self).__init__(*args, **kwargs)

    self.fields['other_location'].required = False

    self.fields['request_comments'].label = "Comments"
    self.fields['request_comments'].placeholder = "Insert the reason for wihy you would like to study here"
    self.fields['request_comments'].required = False

    self.fields['ta_comments'].label = "TA Response"
    self.fields['ta_comments'].disabled = True
    self.fields['ta_comments'].required = False

    self.fields['request_status'].label = "Request Status"
    self.fields['request_status'].disabled = True
    self.fields['request_status'].required = False

  location = forms.ChoiceField(choices=LOCATIONS, widget=forms.RadioSelect)
  other_location = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'location'}))
  request_comments = forms.Textarea(attrs={'rows': 4, 'cols': '100vh'})
  ta_comments = forms.Textarea(attrs={'rows': 4, 'cols': '100vh'})
  request_status = forms.ChoiceField(choices=REQUEST_STATUS)

  class Meta:
    model = SemiAnnual
    exclude = ['trainee', 'term', 'attendance', ]
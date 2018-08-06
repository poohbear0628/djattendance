from django import forms

from accounts.widgets import TraineeSelect2MultipleInput
from django_select2.forms import ModelSelect2MultipleWidget, ModelSelect2Widget
from .models import IndividualSlip, GroupSlip
from accounts.models import Trainee, User
from services.models import Assignment
from aputils.widgets import DatetimePicker


class LeaveslipForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(LeaveslipForm, self).__init__(*args, **kwargs)
    self.fields['type'].label = 'Reason'
    # TODO: uncomment after we add a group for TA sisters
    # self.fields['TA'].queryset = TrainingAssistant.objects.filter(Q(groups__name='regular_training_assistant') || Q(groups__name='sister_training_assistant'))
    if self.instance.TA:
      self.fields['TA'].label = 'TA assigned to this leave slip: %s' % self.instance.TA.full_name + '. Transfer to:'
    else:
      self.fields['TA'].label = 'No TA assigned'
    self.fields['TA_informed'].label = 'Training office informed? ' + ('Yes' if self.instance.informed else 'No')
    if not self.instance.informed:
      self.fields['TA_informed'].widget.attrs['class'] = 'hidden-input'
    self.fields['description'].widget.attrs['rows'] = 2
    self.fields['private_TA_comments'].widget.attrs['rows'] = 2
    self.fields['comments'].widget.attrs['rows'] = 2
    self.fields['TA'].queryset = User.objects.filter(groups__name='regular_training_assistant')
    self.fields['TA_informed'].queryset = User.objects.filter(groups__name='regular_training_assistant')


class IndividualSlipForm(LeaveslipForm):
  def __init__(self, *args, **kwargs):
    super(IndividualSlipForm, self).__init__(*args, **kwargs)
    self.fields['location'].widget.attrs['rows'] = 2
    self.fields['location'].widget.attrs['class'] = 'night-out meal-out'
    self.fields['host_name'].widget.attrs['rows'] = 2
    self.fields['host_name'].widget.attrs['class'] = 'night-out meal-out'
    self.fields['host_phone'].widget.attrs['class'] = 'night-out'
    self.fields['hc_notified'].label = 'HC notified'
    self.fields['hc_notified'].widget.attrs['rows'] = 2
    self.fields['hc_notified'].widget.attrs['class'] = 'night-out'

  class Meta:
    model = IndividualSlip
    fields = ['type', 'description', 'location', 'host_name', 'host_phone', 'hc_notified',
              'comments', 'TA_informed', 'texted', 'TA', 'private_TA_comments']


class GroupSlipForm(LeaveslipForm):
  trainees = forms.ModelMultipleChoiceField(
      queryset=Trainee.objects.all(),
      required=True,
      widget=ModelSelect2MultipleWidget(
        model=Trainee,
        search_fields=['firstname__icontains', 'lastname__icontains']
      ),
  )

  def __init__(self, *args, **kwargs):
    super(GroupSlipForm, self).__init__(*args, **kwargs)

  class Meta:
    model = GroupSlip
    fields = ['trainees', 'type', 'description', 'comments', 'start', 'end', 'TA_informed', 'texted', 'TA', 'private_TA_comments']


class IndividualSlipAdminForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    trainee = Trainee.objects.filter(groups__name='attendance_monitors').first()
    if 'trainee' in kwargs:
      trainee = kwargs.pop('trainee')
    super(IndividualSlipAdminForm, self).__init__(*args, **kwargs)
    self.fields['rolls'].queryset = trainee.rolls.all()
    self.fields['TA'].queryset = User.objects.filter(groups__name='regular_training_assistant')
    self.fields['TA_informed'].queryset = User.objects.filter(groups__name='regular_training_assistant')
    self.fields['trainee'].widget.attrs['class'] = 'select-fk'
    self.fields['TA'].widget.attrs['class'] = 'select-fk'
    self.fields['TA_informed'].widget.attrs['class'] = 'select-fk'
    self.fields['finalized'].widget = DatetimePicker()

  class Meta:
    model = IndividualSlip
    fields = "__all__"


class GroupSlipAdminForm(forms.ModelForm):
  trainees = forms.ModelMultipleChoiceField(
      queryset=Trainee.objects.all(),
      label='Trainees',
      required=False,
      widget=TraineeSelect2MultipleInput,
  )

  service_assignment = forms.ModelChoiceField(
      label='Service Assignment',
      queryset=Assignment.objects.all(),
      required=False,
      widget=ModelSelect2Widget(
          model=Assignment,
          search_fields=['service__name__icontains'],
      ),
  )

  def __init__(self, *args, **kwargs):
    super(GroupSlipAdminForm, self).__init__(*args, **kwargs)
    self.fields['trainee'].widget.attrs['class'] = 'select-fk'
    self.fields['TA'].widget.attrs['class'] = 'select-fk'
    self.fields['TA_informed'].widget.attrs['class'] = 'select-fk'
    self.fields['finalized'].widget = DatetimePicker()
    self.fields['start'].widget = DatetimePicker()
    self.fields['end'].widget = DatetimePicker()

  class Meta:
    model = GroupSlip
    fields = "__all__"

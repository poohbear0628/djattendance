from accounts.models import Trainee
from aputils.widgets import DatePicker
from attendance.models import Roll
from django import forms
from django.db.models import Max
from schedules.models import Event
from django.db.models import Max


class RollAdminForm(forms.ModelForm):

  def __init__(self, *args, **kwargs):
    trainee = None
    if 'trainee' in kwargs:
      trainee = kwargs.pop('trainee')
    super(RollAdminForm, self).__init__(*args, **kwargs)

    if trainee is not None:
      event_qs = Event.objects.none()
      for s in trainee.schedules.all():
        event_qs = event_qs | s.events.all()
      self.fields['event'].queryset = event_qs

    self.fields['event'].widget.attrs['class'] = 'select-fk'
    self.fields['trainee'].widget.attrs['class'] = 'select-fk'
    self.fields['submitted_by'].widget.attrs['class'] = 'select-fk'
    self.fields['date'].widget = DatePicker()

  def clean(self):
    cleaned_data = self.cleaned_data
    data_date = cleaned_data['date']
    data_event = cleaned_data['event']
    data_trainee = cleaned_data['trainee']
    data_submitted_by = cleaned_data['submitted_by']
    invalid_dup = False


    # Date needs to match the event weekday
    if not data_date.weekday() == data_event.weekday:  # 0 is Monday
      raise forms.ValidationError("Date selected does not match Event selected!!")

    sched = data_event.schedules.filter(trainees__in=[data_trainee])
    pr = sched.aggregate(Max('priority'))['priority__max']

    # Event needs to match the trainee
    if pr == None:
      raise forms.ValidationError("Event selected does not match Trainee selected!!")

    # Roll date and event needs to match schedule week
    if not sched.get(priority=pr).active_in_week(data_event.week_from_date(data_date)):
      raise forms.ValidationError("Event is not active for date selected!!")

    # trainees not on self attendance can only have one roll for any event on the same date
    # trainees on self attendance can have two rolls for any event on the same date given that one is submitted by themselves and another one is not
    # if data_trainee.self_attendance:  # if self-attendance
    #   roll_check = Roll.objects.filter(date=data_date, trainee=data_trainee, event=data_event, submitted_by=data_submitted_by)
    #   if data_trainee == data_submitted_by:  # a self-roll submitted
    #     if roll_check.exist():  # if check if self-roll exists
    #       if self.instance:  # if we are editing roll
    #         if roll_check.exclude(id=self.instance.id).exists():  # remove the one we are editing
    #           pass

    return cleaned_data

  class Meta:
    model = Roll
    fields = "__all__"

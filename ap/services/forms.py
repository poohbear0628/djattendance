from django import forms
from services.models.service_hours import ServiceRoll, ServiceAttendance
from services.models.service import Service
from aputils.widgets import DatetimePicker


class ServiceRollForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(ServiceRollForm, self).__init__(*args, **kwargs)

  class Meta:
    model = ServiceRoll
    fields = ["start_datetime", "end_datetime", "task_performed", ]
    widgets = {
      "start_datetime": DatetimePicker(),
      "end_datetime": DatetimePicker(),
    }


class ServiceAttendanceForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    worker = kwargs.pop('worker')
    super(ServiceAttendanceForm, self).__init__(*args, **kwargs)
    service_ids = []
    for assignment in worker.assignments.all().filter(service__designated=True):
      service_ids.append(assignment.service.id)
    self.fields['designated_service'].queryset = Service.objects.filter(id__in=service_ids)
    self.fields['designated_service'].required = False
    self.fields['week'].required = False

  class Meta:
    model = ServiceAttendance
    fields = ["designated_service", "week", ]

from django import forms
from django.contrib import admin
from django_select2.forms import ModelSelect2MultipleWidget

from .models import Roll, Trainee, Event
from accounts.widgets import TraineeSelect2MultipleInput


class RollChangeForm(forms.ModelForm):
  class Meta:
    fields = ['event', 'trainee', 'status', 'finalized', 'date', 'notes', 'submitted_by', ]
    model = Roll


class RollAdminForm(forms.ModelForm):
  class Meta:
    fields = ['events', 'trainees', 'status', 'finalized', 'date', 'notes', 'submitted_by']
    model = Roll

  events = forms.ModelMultipleChoiceField(
      label="Events",
      queryset=Event.objects.all(),
      required=True,
      widget=ModelSelect2MultipleWidget(
          queryset=Event.objects.all(),
          required=True,
          search_fields=['name__icontains', 'weekday__icontains'],
      )
  )

  trainees = forms.ModelMultipleChoiceField(
      queryset=Trainee.objects.all(),
      label='Trainee(s)',
      required=True,
      widget=TraineeSelect2MultipleInput(attrs={'id': 'id_trainees'}),
  )

  submitted_by = forms.ModelChoiceField(
      label="",
      queryset=Trainee.objects.filter(is_active=True),
      required=False,
      widget=forms.HiddenInput,
  )

  def save(self, commit=True):
    data = self.cleaned_data
    for t in data['trainees']:
      for e in data['events']:
        r = Roll(trainee=t, event=e, status=data['status'], notes=data['notes'],
                 date=data['date'], submitted_by=self.user, finalized=data['finalized'])
        r.save()
    return r

  def save_m2m(self):
    return


class RollAdmin(admin.ModelAdmin):
  list_display = ('pk', 'date', 'event', 'status', 'finalized', 'trainee')
  list_filter = ('date', 'event__name', 'status')
  ordering = ('date', 'event')
  search_fields = ('pk', 'trainee__firstname', 'trainee__lastname', 'event__name', 'event__weekday', 'status', 'date')
  form = RollAdminForm

  def get_form(self, request, obj=None, **kwargs):
    if obj:
      return RollChangeForm
    form = super(RollAdmin, self).get_form(request, obj=None, **kwargs)
    form.user = request.user
    return form


admin.site.register(Roll, RollAdmin)

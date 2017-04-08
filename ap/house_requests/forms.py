from django import forms

from .models import MaintenanceRequest

class MaintenanceRequestForm(forms.ModelForm):
  class Meta:
    model = MaintenanceRequest
    fields = ['description', 'urgent']
    labels = {
      'description': ('Please describe the problem in detail.'),
    }

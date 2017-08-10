# forms.py
from django import forms
from .models import Badge, BadgePrintSettings
from paintstore.widgets import ColorPickerWidget

class BadgeForm(forms.ModelForm):
  class Meta:
    model = Badge
    exclude = ('avatar',)

  def save(self, commit=True):
    badge = super(BadgeForm, self).save(commit=False)
    if commit:
      badge.save() #should also save the resizes avatar
    return badge

class BadgeUpdateForm(forms.ModelForm):
  class Meta:
    model = Badge
    exclude = ('avatar',)

  def save(self, commit=True):
    badge = super(BadgeUpdateForm, self).save(commit=False)
    if commit:
      badge.save()
    return badge

class BadgePrint(forms.Form):
  printoption = forms.BooleanField(required=False)

class BadgePrintForm(forms.ModelForm):
  class Meta:
    model = Badge
    exclude = ('avatar',)

  def save(self, commit=True):
    badge = super(BadgeUpdateForm, self).save(commit=False)
    if commit:
      badge.save()
    return badge

class BadgePrintSettingsUpdateForm(forms.ModelForm):
  banner_color = forms.CharField(max_length=7, widget=ColorPickerWidget)
  class Meta:
    model = BadgePrintSettings
    exclude = ()

  def save(self, commit=True):
    badgePrintSettings = super(BadgePrintSettingsUpdateForm, self).save(commit=False)
    if commit:
      badgePrintSettings.save()
    return badgePrintSettings

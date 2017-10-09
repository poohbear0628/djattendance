from django import forms

from django_select2.forms import ModelSelect2Widget, Select2Widget

from .models import User, Trainee

class UserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ('firstname', 'lastname', )


class EmailForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ('email',)


class SwitchUserForm(forms.Form):
  user_id = forms.ModelChoiceField(
      label="User",
      queryset=User.objects.filter(is_active=True),
      required=True,
      widget=ModelSelect2Widget(
          queryset=User.objects.filter(is_active=True),
          required=True,
          search_fields=['firstname__icontains', 'lastname__icontains'],
      ),
  )

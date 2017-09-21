from django import forms
from .models import User, Trainee


class APUserCreationForm(forms.ModelForm):
  """ A form for creating a new user """

  password = forms.CharField(label="Password", widget=forms.PasswordInput)
  password_repeat = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

  class Meta:
    model = User
    fields = ("email", "firstname", "lastname", "gender",)

  def clean(self):
    cleaned_data = super(APUserCreationForm, self).clean()
    password = cleaned_data.get("password")
    password_repeat = cleaned_data.get("password_repeat")
    if password != password_repeat:
      raise forms.ValidationError("Passwords don't match")
    return cleaned_data

  def save(self, commit=True):
    """ Save the provided password in hashed format """
    user = super(APUserCreationForm, self).save(commit=False)
    user.set_password(self.cleaned_data["password"])
    if commit:
      user.save()
    return user


class APUserChangeForm(forms.ModelForm):
  """ A form for updating users. """

  class Meta:
    model = User
    exclude = ['password']


class UserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ('firstname', 'lastname',)


class EmailForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ('email',)

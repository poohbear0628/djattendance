from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend

class CaseInsensitiveModelBackend(ModelBackend):
  def authenticate(self, username=None, password=None, **kwargs):
    if username:
      username = username.lower()
    request = kwargs.pop('request', None)
    return super(CaseInsensitiveModelBackend, self).authenticate(request, username, password, **kwargs)

from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend

class CaseInsensitiveModelBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
    	if username:
        	username = username.lower()
        return super(CaseInsensitiveModelBackend, self).authenticate(username, password, **kwargs)

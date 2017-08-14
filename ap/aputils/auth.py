from django.conf import settings

def login_user(request, user):
  """
  Log in a user without requiring credentials (using ``login`` from
  ``django.contrib.auth``, first finding a matching backend).

  """
  from django.contrib.auth import load_backend, login
  if not hasattr(user, 'backend'):
    for backend in settings.AUTHENTICATION_BACKENDS:
      if user == load_backend(backend).get_user(user.pk):
        user.backend = backend
        break
  if hasattr(user, 'backend'):
    return login(request, user)

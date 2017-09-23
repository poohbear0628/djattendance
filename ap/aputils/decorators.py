from django.utils import six
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test


# Code from: https://djangosnippets.org/snippets/10508/
def group_required(group, login_url=None, raise_exception=False):
  """
  Decorator for views that checks whether a user has a group permission,
  redirecting to the log-in page if necessary.
  If the raise_exception parameter is given the PermissionDenied exception
  is raised.

  Usage:

  @group_required('toto', login_url='/loginpage/')
  def my_view(request):
    ...

  """
  def check_perms(user):
    if isinstance(group, six.string_types):
      groups = (group, )
    else:
      groups = group
    # First check if the user has the permission (even anon users)

    if user.groups.filter(name__in=groups).exists():
      return True
    # In case the 403 handler should be called raise the exception
    if raise_exception:
      raise PermissionDenied
    # As the last resort, show the login form
    return False
  return user_passes_test(check_perms, login_url=login_url)

def for_all_methods(decorator):
  """
  Decorate a class to apply a decorator to all methods in it.
  Example: @for_all_methods(some_decorator_function)
  """
  def decorate(cls):
    for attr in cls.__dict__:
      if callable(getattr(cls, attr)):
        setattr(cls, attr, decorator(getattr(cls, attr)))
    return cls
  return decorate

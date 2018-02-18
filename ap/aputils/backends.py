from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class CaseInsensitiveModelBackend(ModelBackend):
  def authenticate(self, username=None, password=None, **kwargs):
    UserModel = get_user_model()
    if username is None:
      username = kwargs.get(UserModel.USERNAME_FIELD)
    try:
      case_insensitive_username_field = '{}__iexact'.format(UserModel.USERNAME_FIELD)
      user = UserModel._default_manager.get(**{case_insensitive_username_field: username})
    except UserModel.DoesNotExist:
      pass
    else:
      if user.check_password(password) and self.user_can_authenticate(user):
        return user
    # if username:
    #   username = username.lower()
    # request = kwargs.pop('request', None)
    # return super(CaseInsensitiveModelBackend, self).authenticate(request, username, password, **kwargs)

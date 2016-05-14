from django.shortcuts import redirect
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied


class UserCheckMixin(object):
    user_check_failure_path = ''  # can be path, url name or reverse_lazy

    def check_user(self, user):
        return True

    def user_check_failed(self, request, *args, **kwargs):
        raise PermissionDenied

    def dispatch(self, request, *args, **kwargs):
        if not self.check_user(request.user):
            return self.user_check_failed(request, *args, **kwargs)
        return super(UserCheckMixin, self).dispatch(request, *args, **kwargs)
from django.shortcuts import render
from django.views.generic.edit import UpdateView

from .models import XBApplication
from .forms import XBApplicationForm
from braces.views import GroupRequiredMixin
from aputils.trainee_utils import is_trainee, trainee_from_user

from datetime import datetime


class XBApplicationView(UpdateView):
  model = XBApplication
  form_class = XBApplicationForm
  template_name = 'xb_application/application_form.html'

  def get_object(self, queryset=None):
    if is_trainee(self.request.user):
      obj, created = XBApplication.objects.get_or_create(trainee=trainee_from_user(self.request.user))
      return obj
    return None

  def get(self, request, *args, **kwargs):
    self.object = self.get_object()
    return super(XBApplicationView, self).get(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    self.object = self.get_object()
    return super(XBApplicationView, self).post(request, *args, **kwargs)

  def form_valid(self, form):
    return super(XBApplicationView, self).form_valid(form)

  def get_context_data(self, **kwargs):
    ctx = super(XBApplicationView, self).get_context_data(**kwargs)
    ctx['page_title'] = 'FTTA-XB Application'
    ctx['button_label'] = 'Update'
    if is_trainee(self.request.user):
      obj, created = XBApplication.objects.get_or_create(trainee=trainee_from_user(self.request.user))
      if created:
        ctx['button_label'] = 'Save'
    return ctx

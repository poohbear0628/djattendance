from datetime import datetime

from django.views.generic.edit import UpdateView

from .models import XBApplication
from .forms import XBApplicationForm
from aputils.trainee_utils import is_trainee, trainee_from_user
from terms.models import Term


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
    if 'submit' in request.POST:
      self.object.submitted = True
    self.object.last_updated = datetime.now()
    self.object.date_submitted = self.object.last_updated
    self.object.save()
    return super(XBApplicationView, self).post(request, *args, **kwargs)

  def form_valid(self, form):
    return super(XBApplicationView, self).form_valid(form)

  def get_context_data(self, **kwargs):
    ctx = super(XBApplicationView, self).get_context_data(**kwargs)
    self.object = self.get_object()
    ctx['submitted'] = self.object.submitted
    ctx['last_updated'] = self.object.last_updated
    ctx['page_title'] = 'FTTA-XB Application'
    ctx['term'] = Term.current_term()
    if not self.object.submitted:
      ctx['save_button'] = '<button type="submit" class="btn btn-primary btn-save">Save</button>'
      ctx['submit_button'] = '<button type="submit" class="btn btn-primary btn-save" name="submit">Submit</button>'
    return ctx

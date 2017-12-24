# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import UpdateView

from terms.models import Term
from graduation.models import Testimony, Consideration, Website, Outline, Misc, GradAdmin
from graduation.forms import TestimonyForm, ConsiderationForm, WebsiteForm, MiscForm, OutlineForm, GradAdminForm

from braces.views import GroupRequiredMixin

from datetime import datetime


class CreateUpdateView(UpdateView):
  template_name = 'graduation/graduation_form.html'

  def get_object(self, queryset=None):
    grad_admin, created = GradAdmin.objects.get_or_create(term=Term.current_term())
    obj, created = self.model.objects.get_or_create(trainee=self.request.user, grad_admin=grad_admin)
    return obj

  def get(self, request, *args, **kwargs):
    self.object = self.get_object()
    return super(CreateUpdateView, self).get(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    self.object = self.get_object()
    return super(CreateUpdateView, self).post(request, *args, **kwargs)

  def form_valid(self, form):
    return super(CreateUpdateView, self).form_valid(form)

  def get_context_data(self, **kwargs):
    ctx = super(CreateUpdateView, self).get_context_data(**kwargs)
    today = datetime.now().date()
    if self.object.show_status == 'SHOW' or today > self.object.due_date:
      ctx['read_only'] = True
    ctx['page_title'] = self.object.name
    ctx['button_label'] = 'Save'
    return ctx


class TestimonyView(CreateUpdateView):
  model = Testimony
  form_class = TestimonyForm


class ConsiderationView(CreateUpdateView):
  model = Consideration
  form_class = ConsiderationForm


class WebsiteView(CreateUpdateView):
  model = Website
  form_class = WebsiteForm


class OutlineView(CreateUpdateView):
  model = Outline
  form_class = OutlineForm


class MiscView(CreateUpdateView):
  model = Misc
  form_class = MiscForm


class GradAdminView(UpdateView, GroupRequiredMixin):
  model = GradAdmin
  form_class = GradAdminForm
  template_name = 'graduation/grad_admin.html'
  group_required = ['administration', 'grad_committee']

  def get_object(self, queryset=None):
    obj, created = self.model.objects.get_or_create(term=Term.current_term())
    return obj

  def get(self, request, *args, **kwargs):
    self.object = self.get_object()
    return super(GradAdminView, self).get(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    self.object = self.get_object()
    return super(GradAdminView, self).post(request, *args, **kwargs)

  def form_valid(self, form):
    return super(GradAdminView, self).form_valid(form)

  def get_statistics(self):
    stats = {}
    term = Term.current_term()

    stats['Testimony responses'] = 0
    for t in Testimony.objects.filter(grad_admin__term=term):
      if t.responded:
        stats['Testimony responses'] += 1

    stats['Consideration responses'] = 0
    for c in Consideration.objects.filter(grad_admin__term=term):
      if c.responded:
        stats['Consideration responses'] += 1

    stats['Website resopnses'] = 0
    for w in Website.objects.filter(grad_admin__term=term):
      if w.responded:
        stats['Website resopnses'] += 1

    stats['Outline responses'] = 0
    for o in Outline.objects.filter(grad_admin__term=term):
      if o.responded:
        stats['Outline responses'] += 1

    return stats

  def get_context_data(self, **kwargs):
    ctx = super(GradAdminView, self).get_context_data(**kwargs)
    ctx['stats'] = self.get_statistics()
    ctx['page_title'] = "Grad Admin"
    ctx['button_label'] = 'Save'
    return ctx

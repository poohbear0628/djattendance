from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, TemplateView, DetailView, ArchiveIndexView, CreateView, DeleteView
from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy

from terms.models import Term

from .forms import NewSyllabusForm
from .models import Syllabus, ClassSession

class HomeView(ListView):
  template_name = "syllabus/termlist.html"
  model = Term
  context_object_name = 'termlist'

class CLView(ListView):
  template_name = "syllabus/classlist.html"
  context_object_name = 'list'
  model = Syllabus

  """this is to get ?P<term> from urls.py
  and make it accessible to the template classlist.html
  by using {{term}}"""
  def get_context_data(self, **kwargs):
    context = super(CLView, self).get_context_data(**kwargs)
    term = self.kwargs['term']
    context['term'] = term
    context['term_id'] = filter(lambda t: t.code == term, Term.objects.all())[0].id
    return context
  # def get_queryset(self):
  #   term = self.kwargs['term']

class DetailView(DetailView):
  template_name = "syllabus/details.html"
  model = Syllabus
  context_object_name = 'syllabus'
  slug_url_kwarg = 'term','kode'

  def get_context_data(self, **kwargs):
    context = super(DetailView, self).get_context_data(**kwargs)
    context['term'] = self.kwargs['term']
    context['kode'] = self.kwargs['kode']
    context['pk'] = self.kwargs['pk']
    return context

  # def get_queryset(self):
  #   kode = self.kwargs['kode']
  #   term = self.kwargs['term']
  #   return Syllabus.objects.filter(class_syllabus__code= kode)
  #   # .filter(class_syllabus__term = term)

class AddSyllabusView(CreateView):
  model = Syllabus
  template_name = 'syllabus/new_syllabus_form.html'
  form_class = NewSyllabusForm

  def get_context_data(self, **kwargs):
    context = super(AddSyllabusView, self).get_context_data(**kwargs)
    context['term'] = self.kwargs['term']
    return context

  def get_success_url(self):
    term = self.kwargs['term']
    return reverse_lazy('syllabus:classlist-view', kwargs=self.kwargs)

class DeleteSyllabusView(DeleteView):
  model = Syllabus
  template_name = 'syllabus/delete_syllabus_confirm.html'
  # def get_queryset(self):
  #   term = self.kwargs['term']
  def get_success_url(self):
    term = self.kwargs['term']
    return reverse_lazy('syllabus:classlist-view', kwargs={'term': term})

class TestView(ListView):
  template_name = "syllabus/detail.html"
  model = Syllabus
  context_object_name = 'syl_list'

class SyllabusDetailView(ListView):
  model = Syllabus
  template_name = "syllabus/detail.html"
  context_object_name = 'syllabus'
  slug_field = 'code'
  slug_url_kwarg = 'code'

# class SLView(ListView):
#   model = Session
#   template_name = 'session/sessionlist.html'
#   context_object_name = 'ses_list'

class AddSessionView(CreateView):
  model = ClassSession
  template_name = 'session/new_session_form.html'

  def get_success_url(self):
    term = self.kwargs['term']
    kode = self.kwargs['kode']
    pk = self.kwargs['pk']
    return reverse_lazy('syllabus:detail-view', kwargs=self.kwargs)

class DeleteSessionView(DeleteView):
  model = ClassSession
  template_name = 'session/delete_session_confirm.html'
  # def get_queryset(self):
  #   term = self.kwargs['term']
  def get_success_url(self):
    term = self.kwargs['term']
    kode = self.kwargs['kode']
    syllabus_pk = self.kwargs['syllabus_pk']
    return reverse_lazy('syllabus:detail-view', args=[term,kode,syllabus_pk])

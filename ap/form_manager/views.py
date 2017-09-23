from django.views.generic import TemplateView

class FormManagerView(TemplateView):
  template_name = "form_manager/form_manager_base.html"

class ViewFormView(TemplateView):
  template_name = "form_manager/form_viewer_base.html"

  def get_context_data(self, **kwargs):
    context = super(ViewFormView, self).get_context_data(**kwargs)
    context['form_slug'] = self.kwargs['form_slug']
    return context

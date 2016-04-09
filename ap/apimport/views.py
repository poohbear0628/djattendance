from django.shortcuts import render
from django.views.generic.edit import CreateView

from terms.models import Term

# Create your views here.
class CreateTermView(CreateView):
    template_name = 'apimport/term_details.html'
    model = Term
    fields = []

    def get_context_data(self, **kwargs):
        context = super(CreateTermView, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)
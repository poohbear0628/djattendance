from django.shortcuts import render
from django.views.generic.edit import CreateView

from terms.models import Term

from apimport.utils import generate_term_name, term_start_date_from_semiannual

# Create your views here.
class CreateTermView(CreateView):
    template_name = 'apimport/term_details.html'
    model = Term
    fields = []

    # default term values--c_initweeks + c_graceweeks needs to be a multiple of 2
    c_totalcount = 20
    c_initweeks = 0
    c_graceweeks = 2
    c_periods = (c_totalcount - c_initweeks - c_graceweeks) / 2

    def get_context_data(self, **kwargs):
        context = super(CreateTermView, self).get_context_data(**kwargs)
        context['season'], context['year'] = generate_term_name()

        semi_season = "Summer" if context['season'] == "Spring" else "Winter"
        context['start_date'] = term_start_date_from_semiannual(semi_season, context['year'])
        context['initial_weeks'] = self.c_initweeks
        context['grace_weeks'] = self.c_graceweeks
        context['periods'] = self.c_periods

        return context

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)
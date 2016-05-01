import sys

from datetime import datetime, timedelta

from django.shortcuts import render
from django.views.generic.edit import CreateView

from terms.models import Term

from .forms import CsvFileForm
from .utils import generate_term, term_start_date_from_semiannual, validate_term, \
                   check_csvfile, save_file

# Create your views here.
class CreateTermView(CreateView):
    template_name = 'apimport/term_details.html'
    model = Term
    fields = []

    # default term values--c_initweeks + c_graceweeks needs to be a multiple of 2
    c_totalweeks = 20
    c_initweeks = 0
    c_graceweeks = 2
    c_periods = (c_totalweeks - c_initweeks - c_graceweeks) / 2

    def get_context_data(self, **kwargs):
        context = super(CreateTermView, self).get_context_data(**kwargs)
        context['season'], context['year'] = generate_term()

        semi_season = "Summer" if context['season'] == "Spring" else "Winter"
        #context['start_date'] = term_start_date_from_semiannual(semi_season, context['year'])
        context['initial_weeks'] = self.c_initweeks
        context['grace_weeks'] = self.c_graceweeks
        context['periods'] = self.c_periods
        return context

    def post(self, request, *args, **kwargs):
        term_name = request.POST['termname']

        # Store interesting variables for later -- TODO(haileyl): delete these variables
        request.session['c_initweeks'] = request.POST['initial_weeks']
        request.session['c_graceweeks'] = request.POST['grace_weeks']
        request.session['c_periods'] = request.POST['periods']

        start_date = request.POST['startdate']
        end_date = request.POST['enddate']

        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        # Refresh if bad input received
        if not validate_term(start_date, end_date, request.session['c_initweeks'], 
            request.session['c_graceweeks'], request.session['c_periods'],
            self.c_totalweeks, request):
            return self.get(request, *args, **kwargs)

        # Save out the CSV Form
        file_path = save_file(request.FILES['csvFile'], 'csvFiles\\')

        # Check the CSV File
        localities, teams, residences = check_csvfile(file_path)

        # TODO: process errors from localities, etc.

        # TODO: This should be moved somewhere else
        # Actually import the information        
        if (not localities) and (not teams) and (not residences):
            pass     
        return self.get(request, *args, **kwargs)
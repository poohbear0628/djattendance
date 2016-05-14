import sys

from datetime import datetime, timedelta
import json

from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from terms.models import Term

from .forms import CityForm, CityFormSet
from .utils import create_term, generate_term, term_start_date_from_semiannual, validate_term, \
                   check_csvfile, import_csvfile, save_file, \
                   save_locality
                   
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

        context['start_date'] = term_start_date_from_semiannual(semi_season, context['year'])
        context['initial_weeks'] = self.c_initweeks
        context['grace_weeks'] = self.c_graceweeks
        context['periods'] = self.c_periods
        return context

    def post(self, request, *args, **kwargs):
        term_name = request.POST['termname']
        season, year = term_name.split(" ")
        
        # Store interesting variables for later -- TODO(haileyl): delete these variables
        request.session['c_initweeks'] = request.POST['initial_weeks']
        request.session['c_graceweeks'] = request.POST['grace_weeks']
        request.session['c_periods'] = request.POST['periods']

        start_date = request.POST['startdate']
        end_date = request.POST['enddate']

        start_date = datetime.strptime(start_date, "%m/%d/%Y")
        end_date = datetime.strptime(end_date, "%m/%d/%Y")

        # Refresh if bad input received
        if not validate_term(start_date, end_date, request.session['c_initweeks'], 
            request.session['c_graceweeks'], request.session['c_periods'],
            self.c_totalweeks, request):
            return self.get(request, *args, **kwargs)

        # Save term to database
        create_term(season, year, start_date, end_date)

        # Save out the CSV File
        file_path = save_file(request.FILES['csvFile'], 'apimport\\csvFiles\\')

        # Check the CSV File
        localities, teams, residences = check_csvfile(file_path)

        if localities or teams or residences:
            request.session['localities'] = localities
            request.session['teams'] = teams
            request.session['residences'] = residences
            return redirect('apimport:process_csv')

        # No errors!
        import_csvfile(file_path)
        
        return self.get(request, *args, **kwargs)

class ProcessCsvData(TemplateView):
    template_name = 'apimport/process_csv.html'
    fields = []

    def get_context_data(self, **kwargs):
        context = super(ProcessCsvData, self).get_context_data(**kwargs)
        context['teams'] = self.request.session['teams']
        context['residences'] = self.request.session['residences']

        if self.request.POST:
            context['cityformset'] = CityFormSet(self.request.POST)
        else:
            initial = []
            for locality in self.request.session['localities']:
                initial.append({'name': locality})
            context['cityformset'] = CityFormSet(initial=initial)
            self.request.session['localities'] = []
        return context

    def post(self, request, *args, **kwargs):
        pass

def save_data(request):
    if request.is_ajax():
        save_type = request.POST['type']
        if save_type == 'locality':
            save_locality(request.POST['city_name'], request.POST['state_id'], request.POST['country_code'])

    response = {'Todo(apimport2)' : 'Check failure'}
    return HttpResponse(json.dumps(response), content_type="application/json")
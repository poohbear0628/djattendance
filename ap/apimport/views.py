import sys

from datetime import datetime, timedelta

from django.shortcuts import render
from django.views.generic.edit import CreateView

from terms.models import Term

from .utils import generate_term, term_start_date_from_semiannual, validate_term
from .forms import CsvFileForm

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
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']

        # Store interesting variables for later -- TODO(haileyl): delete these variables
        request.session['c_initweeks'] = request.POST['initial_weeks']
        request.session['c_graceweeks'] = request.POST['grace_weeks']
        request.session['c_periods'] = request.POST['periods']

        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        # end date is not coming in yet so just set one for now.  TODO(haileyl): remove this
        end_date = start_date + timedelta(days=(7 * self.c_totalweeks - 1))

        # Refresh if bad input received
        if not validate_term(start_date, end_date, request.session['c_initweeks'], 
            request.session['c_graceweeks'], request.session['c_periods'],
            self.c_totalweeks, request):
            return self.get(request, *args, **kwargs)

        # File saved to csvfiles
        form = CsvFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                upload = ImportFile(docFile=form.cleaned_data['csvFile'])
                upload.save()
            except:
                print "Other error"
                print sys.exec_info()[0]

        print request.FILES

        return self.get(request, *args, **kwargs)
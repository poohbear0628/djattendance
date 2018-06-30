from django.core.management.base import BaseCommand

from terms.models import Term
from apimport.utils import term_start_date_from_semiannual, term_end_date_from_semiannual, currently_in_term, create_term

from datetime import date
import calendar
from dateutil.relativedelta import relativedelta

class Command(BaseCommand):
  # to use: python ap/manage.py populate_terms --settings=ap.settings.dev

  def _create_terms(self):
    today = date.today()
    for year in range(2010, today.year + 1):
      seasons_to_semiannual = {'Fall': 'Winter', 'Spring': 'Summer'}
      for season, semiannual in seasons_to_semiannual.items():
        term_start = term_start_date_from_semiannual(semiannual, year)
        term_end = term_end_date_from_semiannual(semiannual, year)
        in_term = currently_in_term(term_start, term_end)
        create_term(season, year, term_start, term_end)
        if in_term: # we've reached our current term, so stop
          break

  def handle(self, *args, **options):
    print("* Populating terms...")
    self._create_terms()

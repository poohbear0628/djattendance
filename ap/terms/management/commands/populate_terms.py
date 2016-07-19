from django.core.management.base import BaseCommand
from terms.models import Term

from datetime import timedelta, date, datetime, time

class Command(BaseCommand):
    # to use: python ap/manage.py populate_terms --settings=ap.settings.dev

    def date_for_day_of_week(self, date, day):
        """ returns the date of the specified day in the week identified by date.
        For example, if date 4/9/2016 (Saturday) and 0 (Monday) are passed in,
        4/4/2016 will be returned. """
        return datetime.combine(date + timedelta(days=day-date.weekday()), time(0,0))

    def _create_terms(self):
        today = date.today()
        for i in range(0,4):
            this_year = today.year
            this_month = today.month

            if this_month > 1 and this_month < 8:
                seed_date = datetime(this_year, 7, 4)
            else:
                seed_date = datetime(this_year, 12, 25)
        
            # Make it a Monday
            seed_date = self.date_for_day_of_week(seed_date, 0)

            # return date of 19 weeks previous-- one week for semi-annual
            term_start = datetime.combine(seed_date + timedelta(weeks=-19, days=0), time(0,0)).date()
            term_start = self.date_for_day_of_week(seed_date, 6)

            # TODO: finish this...

    def handle(self, *args, **options):
        self._create_terms()
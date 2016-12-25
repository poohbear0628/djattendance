from django.core.management.base import BaseCommand
from terms.models import Term

from datetime import date
import calendar
from dateutil.relativedelta import relativedelta

def nth_weekday(n, weekday, year, month):
  return calendar.Calendar(weekday).monthdatescalendar(year, month)[n][0]

class Command(BaseCommand):
  # to use: python ap/manage.py populate_terms --settings=ap.settings.dev

  def _create_terms(self):
    today = date.today()
    for year in range(2010, date.today().year + 1):
      fall_start = nth_weekday(2, 0, year, 8)
      fall_end = fall_start + relativedelta(weeks=20) + relativedelta(days=-2)
      spring_start = nth_weekday(3, 0, year, 2)
      spring_end = spring_start + relativedelta(weeks=20) + relativedelta(days=-2)
      if fall_start <= today and fall_end >= today:
        current = True
      else:
        current = False
      fall = Term(current=current, season='Fall', year=year, start=fall_start, end=fall_end)
      if spring_start <= today and spring_start >= today:
        current = True
      else:
        current = False
      spring = Term(current=current, season='Spring', year=year, start=fall_start, end=fall_end)
      fall.save()
      spring.save()

  def handle(self, *args, **options):
    self._create_terms()

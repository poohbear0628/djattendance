from django.core.management.base import BaseCommand
from terms.models import Term

from datetime import date
import calendar
from dateutil.relativedelta import relativedelta

def date_for_day_of_week(date, day):
  """ returns the date of the specified day in the week identified by date.
      For example, if date 4/9/2016 (Saturday) and 0 (Monday) are passed in,
      4/4/2016 will be returned. """
  return date + relativedelta(days=day-date.weekday())

def is_current_term(start, end):
  return date.today() >= start and date.today() <= end

class Command(BaseCommand):
  # to use: python ap/manage.py populate_terms --settings=ap.settings.dev

  def _create_terms(self):
    today = date.today()
    monday, saturday = (0, 5)
    term_length_minus_semiannual = 20 - 1
    for year in range(2010, today.year + 1):
      july_fourth = date(year, 7, 4)
      christmas = date(year, 12, 25)
      # Because Monday == 0, if these are on Sunday, we incorrectly get the previous week, so adjust
      if christmas.weekday() == 6:
        christmas += relativedelta(days=1)
      if july_fourth.weekday() == 6:
        july_fourth += relativedelta(days=1)
      spring_semiannual_monday = date_for_day_of_week(july_fourth, monday)
      spring_start = spring_semiannual_monday + relativedelta(weeks=-term_length_minus_semiannual)
      spring_end = date_for_day_of_week(july_fourth, saturday)
      fall_semiannual_monday = date_for_day_of_week(christmas, monday)
      fall_start = fall_semiannual_monday + relativedelta(weeks=-term_length_minus_semiannual)
      fall_end = date_for_day_of_week(christmas, saturday)
      fall = Term(current=is_current_term(fall_start, fall_end), season='Fall', year=year, start=fall_start, end=fall_end)
      fall.save()
      spring = Term(current=is_current_term(spring_start, spring_end), season='Spring', year=year, start=spring_start, end=spring_end)
      spring.save()

  def handle(self, *args, **options):
    self._create_terms()

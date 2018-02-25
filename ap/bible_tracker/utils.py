from datetime import datetime, timedelta
from .models import BibleReading
from terms.models import Term
from aputils.trainee_utils import is_trainee, trainee_from_user
import json


def bible_reading_finalized(user):
  finalized = True
  term = Term.current_term()
  try:
    if is_trainee(user):
      trainee = trainee_from_user(user)
      today = datetime.now().date()
      week = term.term_week_of_date(today)
      if week > 0:
        week = week - 1
      term_week_code = str(term.id) + "_" + str(week)

      try:
        trainee_weekly_reading = BibleReading.objects.get(trainee=trainee).weekly_reading_status[term_week_code]
        json_weekly_reading = json.dumps(trainee_weekly_reading)
      except (BibleReading.DoesNotExist, KeyError):
        trainee_weekly_reading = "{\"status\": \"_______\", \"finalized\": \"N\"}"
        json_weekly_reading = json.loads(trainee_weekly_reading)

      try:
        if str(json_weekly_reading['finalized']) == 'N' and (today > get_prev_tuesday()):
          finalized = False
      except TypeError:
        pass

  except AttributeError:
    pass

  return finalized


def get_prev_tuesday():
  today = datetime.now().date()
  t = timedelta((1 - today.weekday()) % 7)  # Mon-0, Sun-6
  return today - t

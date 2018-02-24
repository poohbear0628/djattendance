from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from django.core.urlresolvers import reverse
from .models import BibleReading
from terms.models import Term
from aputils.trainee_utils import is_trainee, trainee_from_user
from datetime import datetime, timedelta
import json


class BibleReadingMiddleware(MiddlewareMixin):
    forced = True

    def process_request(self, request):
      if request.path not in [reverse('bible_tracker:index'), reverse('login'), reverse('logout')]:
        if request.user.is_authenticated() and not bible_reading_finalized(request):
          self.forced = False
          return HttpResponseRedirect(reverse('bible_tracker:index'))
      return None

    def process_template_response(self, request, response):
      response.context_data['forced'] = self.forced
      return response


def bible_reading_finalized(request):
  finalized = True
  term = Term.current_term()
  try:
    if is_trainee(request.user):
      trainee = trainee_from_user(request.user)
      try:
        trainee_bible_reading = BibleReading.objects.get(trainee=trainee)
        today = datetime.now().date()

        week = term.term_week_of_date(today)
        if week > 0:
          week = week - 1
          week_code = str(term.id) + "_" + str(week)
          try:
            trainee_weekly_reading = trainee_bible_reading.weekly_reading_status[week_code]
            json_weekly_reading = json.loads(trainee_weekly_reading)
            if str(json_weekly_reading['finalized']) == 'N' and (today > get_prev_tuesday()):
              finalized = False
          except KeyError:
            pass
      except BibleReading.DoesNotExist:
        pass
  except AttributeError:
    pass

  return finalized


def get_prev_tuesday():
  today = datetime.now().date()
  t = timedelta((1 - today.weekday()) % 7)  # Mon-0, Sun-6
  return today - t

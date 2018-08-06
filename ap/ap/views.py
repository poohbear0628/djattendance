from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date
from dailybread.models import Portion
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from announcements.notifications import get_announcements, get_popups
from aputils.trainee_utils import is_trainee, is_TA, trainee_from_user
from bible_tracker.models import BibleReading, EMPTY_WEEKLY_STATUS, UNFINALIZED_STR
from bible_tracker.views import EMPTY_WEEK_CODE_QUERY
from terms.models import Term
from house_requests.models import MaintenanceRequest
from django.core.urlresolvers import reverse_lazy
import json

from aputils.utils import WEEKDAY_CODES


@login_required
def home(request):
  user = request.user

  # Default for Daily Bible Reading
  current_term = Term.current_term()
  term_id = current_term.id

  try:
    # Do not set as user input.
    current_week = Term.current_term().term_week_of_date(date.today())
  except ValueError:
    current_week = 19
  term_week_code = str(term_id) + "_" + str(current_week)

  try:
    trainee_bible_reading = BibleReading.objects.get(trainee=user)
  except ObjectDoesNotExist:
    trainee_bible_reading = BibleReading(
      trainee=trainee_from_user(user),
      weekly_reading_status={term_week_code: EMPTY_WEEK_CODE_QUERY},
      books_read={})
    trainee_bible_reading.save()
  except MultipleObjectsReturned:
    return HttpResponse('Multiple bible reading records found for trainee!')

  weekly_status = EMPTY_WEEKLY_STATUS
  finalized_str = UNFINALIZED_STR
  if term_week_code in trainee_bible_reading.weekly_reading_status:
    weekly_reading = trainee_bible_reading.weekly_reading_status[term_week_code]
    json_weekly_reading = json.loads(weekly_reading)
    weekly_status = str(json_weekly_reading['status'])
    finalized_str = str(json_weekly_reading['finalized'])

  data = {
      'daily_nourishment': Portion.today(),
      'user': user,
      'isTrainee': is_trainee(user),
      'trainee_info': BibleReading.weekly_statistics,
      'current_week': current_week,
      'weekly_status': weekly_status,
      'weeks': Term.all_weeks_choices(),
      'finalized': finalized_str,
      'weekday_codes':json.dumps(WEEKDAY_CODES)
  }
  notifications = get_announcements(request)
  for notification in notifications:
    tag, content = notification
    messages.add_message(request, tag, content)
  data['popups'] = get_popups(request)

  if is_trainee(user):
    trainee = trainee_from_user(user)
    # Bible Reading progress bar
    trainee_bible_reading = BibleReading.objects.filter(trainee=trainee).first()
    if trainee_bible_reading is None:
      data['bible_reading_progress'] = 0
    else:
      _, year_progress = BibleReading.calcBibleReadingProgress(trainee_bible_reading, user)
      data['bible_reading_progress'] = year_progress

  # condition for maintenance brothers
  elif is_TA(user) and user.has_group(['facility_maintenance']) and user.groups.all().count() == 1:
    data['house_requests'] = MaintenanceRequest.objects.all()
    data['request_status'] = MaintenanceRequest.STATUS

  return render(request, 'index.html', context=data)


def custom404errorview(request):
  ctx = {
    'image_path': 'img/404error.png',
    'page_title': 'Page Not Found'
  }
  return render(request, 'error.html', context=ctx)


def custom500errorview(request):
  ctx = {
    'image_path': 'img/500error.png',
    'page_title': 'Internal Server Error'
  }
  return render(request, 'error.html', context=ctx)


def custom503errorview(request):
  ctx = {
    'image_path': 'img/503error.png',
    'page_title': 'Service Unavailable'
  }
  return render(request, 'error.html', context=ctx)

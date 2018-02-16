from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date
from dailybread.models import Portion
from announcements.notifications import get_announcements, get_popups

from aputils.trainee_utils import is_trainee, is_TA, trainee_from_user
from bible_tracker.models import BibleReading
from terms.models import Term

@login_required
def home(request):

  data = {
    'daily_nourishment': Portion.today(),
    'user': request.user,
    'trainee_info': BibleReading.weekly_statistics,
    'current_week' : Term.current_term().term_week_of_date(date.today()),
    'weeks' : Term.all_weeks_choices()
  }

  notifications = get_announcements(request)
  for notification in notifications:
    tag, content = notification
    messages.add_message(request, tag, content)

  data['popups'] = get_popups(request)

  if is_trainee(request.user):
    trainee = trainee_from_user(request.user)
    data['schedules'] = trainee.active_schedules

    # Bible Reading progress bar
    trainee_bible_reading = BibleReading.objects.filter(trainee=trainee).first()

    if (trainee_bible_reading == None):
      data['bible_reading_progress'] = 0
    else:
      year_checked_list, year_progress = BibleReading.calcBibleReadingProgress(trainee_bible_reading, request.user)
      data['bible_reading_progress'] = year_progress

  elif is_TA(request.user):
    #do stuff to TA
    pass
  else:
    #do stuff to other kinds of users
    pass

  return render(request, 'index.html', context=data)
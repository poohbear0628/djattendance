from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from dailybread.models import Portion
from announcements.notifications import get_announcements, get_popups

from aputils.trainee_utils import is_trainee, is_TA, trainee_from_user
from bible_tracker.models import BibleReading

@login_required
def home(request):

  data = {
    'daily_nourishment': Portion.today(),
    'user': request.user,
  }

  notifications = get_announcements(request)
  for notification in notifications:
    tag, content = notification
    messages.add_message(request, tag, content)

  data['popups'] = get_popups(request)

  print "hello first"

  if is_trainee(request.user):
    trainee = trainee_from_user(request.user)
    data['schedules'] = trainee.active_schedules

    trainee_bible_reading = BibleReading.objects.filter(trainee=trainee).first()

    print "hello"
    print trainee_bible_reading

    data['first_year_progress'] = trainee_bible_reading.calcFirstYearProgress()
    data['second_year_progress'] = trainee_bible_reading.calcSecondYearProgress()

  elif is_TA(request.user):
    #do stuff to TA
    pass
  else:
    #do stuff to other kinds of users
    pass

  return render(request, 'index.html', context=data)
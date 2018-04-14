from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date
from dailybread.models import Portion
from announcements.notifications import get_announcements, get_popups

from aputils.trainee_utils import is_trainee, is_TA, trainee_from_user
from bible_tracker.models import BibleReading
from terms.models import Term
from house_requests.models import MaintenanceRequest


@login_required
def home(request):
  user = request.user
  data = {
      'daily_nourishment': Portion.today(),
      'user': user,
      'trainee_info': BibleReading.weekly_statistics,
      'current_week': Term.current_term().term_week_of_date(date.today()),
      'weeks': Term.all_weeks_choices()
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
  return render(request, '404error.html')

import datetime
from itertools import chain

from django.contrib import messages
from django.db.models import Count, Q
from django.core.urlresolvers import reverse

from models import Announcement
from bible_tracker.models import BibleReading
from leaveslips.models import IndividualSlip, GroupSlip
from web_access.models import WebRequest
from terms.models import Term
from aputils.trainee_utils import is_trainee, trainee_from_user

def get_popups(request):
  if not is_trainee(request.user):
    return []
  trainee = trainee_from_user(request.user)
  announcements = Announcement.announcements_for_today(trainee, is_popup=True)
  return announcements

def get_announcements(request):
  notifications = []
  if is_trainee(request.user):
    trainee = trainee_from_user(request.user)
    notifications = chain(discipline_announcements(trainee),
                          server_announcements(trainee),
                          bible_reading_announcements(trainee),
                          request_statuses(trainee))
  # sort on severity level of message
  return sorted(notifications, lambda a, b: b[0] - a[0])

def request_statuses(trainee):
  requests = chain(
    IndividualSlip.objects.filter(trainee=trainee, status='F'),
    GroupSlip.objects.filter(trainee=trainee, status='F'),
    WebRequest.objects.filter(trainee=trainee, status='F'),
    Announcement.objects.filter(trainee_author=trainee, status='F')
  )
  return [(messages.ERROR, 'Your <a href="{url}">{request}</a> has been marked for fellowship'.format(url=req.get_absolute_url(), request=req._meta.verbose_name)) for req in requests]

def bible_reading_announcements(trainee):
  term = Term.current_term()
  week = term.term_week_of_date(datetime.date.today())
  url = reverse('bible_tracker:index')
  fmtString = 'You have not filled out your <a href="{url}">Bible reading</a>'
  try:
    reading = BibleReading.objects.get(trainee=trainee)
  except:
    return [(messages.WARNING, fmtString.format(url=url))]
  unreadWeeks = []
  fmtString += ' for week {week} yet'
  for w in range(week):
    stats = reading.weekly_statistics(w, w, term.id)
    if stats['number_filled'] < 7:
      unreadWeeks.append(str(w))
  if not unreadWeeks:
    return []
  return [(messages.WARNING, fmtString.format(url=url, week=', '.join(unreadWeeks)))]

def server_announcements(trainee):
  announcements = Announcement.announcements_for_today(trainee)
  return [(messages.INFO, a.announcement) for a in announcements]

def discipline_announcements(trainee):
  notifications = []
  url = reverse('lifestudies:discipline_list')
  for discipline in trainee.discipline_set.all():
    if discipline.get_num_summary_due() > 0:
      content = 'Life Study Summary due for {infraction}. <a href="{url}">Still need: {due}</a>'.format(infraction=discipline.get_infraction_display(), url=url, due=discipline.get_num_summary_due())
      notifications.append((messages.WARNING, content))
  return notifications

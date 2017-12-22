from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from collections import OrderedDict
from dailybread.models import Portion
from announcements.notifications import get_announcements, get_popups

from aputils.trainee_utils import is_trainee, is_TA, trainee_from_user
from bible_tracker.models import BibleReading

@login_required

def calcFirstYearProgress(user_checked_list):
    first_year_checked_list = [int(book_code.split("_")[1]) for book_code in user_checked_list.keys() if book_code.startswith('1_')]
    first_year_progress = 0

    for checked_book in first_year_checked_list:
        first_year_progress = first_year_progress + sum([int(chapter_verse_count) for chapter_verse_count in bible_books[checked_book][3]])

    return (first_year_checked_list, int(float(first_year_progress) / 31102.0 * 100))

def calcSecondYearProgress(user_checked_list):
    second_year_checked_list = [int(book_code.split("_")[1]) for book_code in user_checked_list.keys() if book_code.startswith('2_')]
    second_year_progress = 0

    for checked_book in second_year_checked_list:
        second_year_progress = second_year_progress + sum([int(chapter_verse_count) for chapter_verse_count in bible_books[checked_book][3]])

    return (second_year_checked_list, int(float(second_year_progress) / 7957.0 * 100))

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

  if is_trainee(request.user):
    trainee = trainee_from_user(request.user)
    data['schedules'] = trainee.active_schedules

    trainee_bible_reading = BibleReading.objects.get(trainee=trainee)
    user_checked_list = trainee_bible_reading.books_read

    data['first_year_progress'] = calcFirstYearProgress(user_checked_list)
    data['second_year_progress'] = calcSecondYearProgress(user_checked_list)

  elif is_TA(request.user):
    #do stuff to TA
    pass
  else:
    #do stuff to other kinds of users
    pass

  return render(request, 'index.html', context=data)
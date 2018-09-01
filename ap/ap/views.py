from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import F, Q, Count
# from accounts.models import Trainee
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
from services.models import (Assignment, Category, Prefetch, SeasonalServiceSchedule,
                     Service, ServiceAttendance, ServiceException, ServiceRoll,
                     ServiceSlot, WeekSchedule, Worker)
from services.serializers import (AssignmentPinSerializer, ExceptionActiveSerializer,
                          ServiceActiveSerializer, ServiceCalendarSerializer,
                          ServiceSlotWorkloadSerializer, ServiceTimeSerializer,
                          UpdateWorkerSerializer, WorkerAssignmentSerializer,
                          WorkerIDSerializer)
from services.utils import (assign, assign_leaveslips, merge_assigns,
                    save_designated_assignments, SERVICE_CHECKS)

import json

from aputils.utils import WEEKDAY_CODES


@login_required
def home(request):
  user = request.user
  trainee=trainee_from_user(user)

  # Default for Daily Bible Reading
  current_term = Term.current_term()
  term_id = current_term.id

  try:
    # Do not set as user input.
    current_week = Term.current_term().term_week_of_date(date.today())
    cws = WeekSchedule.get_or_create_week_schedule(trainee, current_week)

  except ValueError:
    current_week = 19
    cws = WeekSchedule.get_or_create_current_week_schedule(trainee)
    # week_start, week_end = cws.week_range
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

  workers = Worker.objects.select_related('trainee').all().order_by('trainee__firstname', 'trainee__lastname')

  order = [
      'Breakfast Prep',
      'Breakfast Cleanup',
      'Lunch Prep',
      'Lunch Cleanup',
      'Sack Lunch',
      'Supper Prep',
      'Supper Cleanup',
      'Supper Delivery',
      'Dust Mopping',
      'Restroom Cleaning',
      'Space Cleaning',
      'Chairs',
  ]
  ordering = dict([reversed(o) for o in enumerate(order)])
  categories = Category.objects.filter(~Q(name='Designated Services')).prefetch_related(
      Prefetch('services', queryset=Service.objects.order_by('weekday'))
  ).distinct()
  categories = sorted(categories, key=lambda c: ordering.get(c.name, float('inf')))

  worker_assignments = Worker.objects.select_related('trainee').prefetch_related(
      Prefetch('assignments', queryset=Assignment.objects.filter(week_schedule=cws).select_related('service', 'service_slot', 'service__category').order_by('service__weekday'), to_attr='week_assignments'))\
      .order_by('trainee__lastname', 'trainee__firstname')

  # schedulers = list(Trainee.objects.filter(groups__name='service_schedulers').exclude(groups__name='dev').values_list('firstname', 'lastname'))
  # schedulers = ", ".join("%s %s" % tup for tup in schedulers)

  # attach services directly to trainees for easier template traversal
  for worker in worker_assignments:
    service_db = {}
    designated_list = []
    for a in worker.week_assignments:
      if a.service.category.name == "Designated Services":
        designated_list.append(a.service)
      else:
        service_db.setdefault(a.service.category, []).append((a.service, a.service_slot.name))
      # re-order so service dates in box are in ascending order
      for cat, services in service_db.items():
        service_db[cat] = sorted(services, key=lambda s: (s[0].weekday + 6) % 7)
    worker.services = service_db
    worker.designated_services = designated_list

  # For Review Tab
  categories = Category.objects.prefetch_related(
      Prefetch('services', queryset=Service.objects.order_by('weekday', 'start')),
      Prefetch('services__serviceslot_set', queryset=ServiceSlot.objects.filter(assignments__week_schedule=cws).annotate(workers_count=Count('assignments__workers')).order_by('-worker_group__assign_priority')),
      Prefetch('services__serviceslot_set', queryset=ServiceSlot.objects.filter(~Q(Q(assignments__isnull=False) & Q(assignments__week_schedule=cws))).filter(workers_required__gt=0), to_attr='unassigned_slots'),
      Prefetch('services__serviceslot_set__assignments', queryset=Assignment.objects.filter(week_schedule=cws)),
      Prefetch('services__serviceslot_set__assignments__workers', queryset=Worker.objects.select_related('trainee').order_by('trainee__gender', 'trainee__firstname', 'trainee__lastname'))
  ).distinct()

  data = {
      'daily_nourishment': Portion.today(),
      'user': user,
      'isTrainee': is_trainee(user),
      'trainee_info': BibleReading.weekly_statistics,
      'current_week': current_week,
      'weekly_status': weekly_status,
      'weeks': Term.all_weeks_choices(),
      'finalized': finalized_str,
      'weekday_codes':json.dumps(WEEKDAY_CODES),
      'workers': workers
  }

  # ctx = {
  #     'columns': 2,
  #     'pagesize': 'letter',
  #     'orientation': 'landscape',
  #     'wkstart': str(week_start),
  #     'categories': categories,
  #     'worker_assignments': worker_assignments,
  #     'encouragement': cws.encouragement,
  #     'schedulers': schedulers,
  #     'page_title': 'FTTA Service Schedule'
  # }

  # if house:
  #   ctx['houses'] = House.objects.filter(id__in=Trainee.objects.values_list('house', flat=True))
  #   return render(request, 'services/services_report_house.html', ctx)

  # if request.POST.get('encouragement') is not None:
  #   if cws is None:
  #     print "no current week schedule"
  #   else:
  #     cws.encouragement = request.POST.get('encouragement')
  #     cws.save()

  # return render(request, 'services/services_report_base.html', ctx)

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


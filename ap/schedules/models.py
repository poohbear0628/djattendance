from copy import deepcopy
from datetime import datetime, date, time, timedelta
from sets import Set

from django.db import models
from django.db.models import Q
from django.core.urlresolvers import reverse

from terms.models import Term
from accounts.models import Trainee
from seating.models import Chart
from aputils.models import QueryFilter
from teams.models import Team
from .utils import next_dow
from schedules.constants import WEEKDAYS
from collections import OrderedDict

from aputils.eventutils import EventUtils
from aputils.utils import comma_separated_field_is_in_regex

""" SCHEDULES models.py
This schedules module is for representing weekly trainee schedules.
Data Models
- Event:
  an event, such as class or study time, that trainees need to attend.
- WeeklyEvents:
- Schedule:
  a collection of events for one trainee. each trainee should have one
  schedule per term.
- ScheduleTemplate:
  a generic collection of events for one week that can be applied to a
  trainee or group of trainees.
"""


'''
Event - Only defines one particular event. i.e. Full Min (Tuesday morning, weekly)
Can never be something like: Thursday/Saturday evening study
'''
class Event(models.Model):

  # different colors assigned to each event type
  # Use this to display Rolls
  EVENT_TYPES = (
    ('C', 'Class'),
    ('S', 'Study'),
    ('R', 'Rest'),
    ('M', 'Meal'),
    ('H', 'House'),
    ('T', 'Team'),
    ('Y', 'YPC'),
    ('L', 'Church Meeting'),  # C is taken, so L for locality
    ('*', 'Special'),  # S is taken, so * for special
  )

  # This field determines if person can enter roll. Does not affect how it shows on their view
  MONITOR_TYPES = (
    ('AM', 'Attendance Monitor'),
    ('TM', 'Team Monitor'),
    ('HC', 'House Coordinator'),
    ('RF', 'RFID reader'),
  )

  CLASS_TYPE = (
    ('MAIN', 'Main'),
    ('1YR', '1st Year'),
    ('2YR', '2nd Year'),
    ('AFTN', 'Afternoon'),
  )

  # name of event, e.g. Full Ministry of Christ, or Lights Out
  name = models.CharField(max_length=255)

  # the event's shortcode, e.g. FMoC or Lights
  code = models.CharField(max_length=20)

  # a description of the event (optional)
  description = models.CharField(max_length=250, blank=True)

  # if this event is a class, relate it
  # classs = models.ForeignKey(Class, blank=True, null=True, verbose_name='class')  # class is a reserved keyword :(

  # the type of event
  type = models.CharField(max_length=1, choices=EVENT_TYPES)

  # which type of class this is, e.g. Main, 1st year
  class_type = models.CharField(max_length=4, choices=CLASS_TYPE, blank=True, null=True)

  # who takes roll for this event
  monitor = models.CharField(max_length=2, choices=MONITOR_TYPES, blank=True, null=True)

  start = models.TimeField()

  end = models.TimeField()

  # Optional to catch one-off days, only happen once
  day = models.DateField(blank=True, null=True)

  weekday = models.PositiveSmallIntegerField(choices=WEEKDAYS, verbose_name='Day of the week')

  # Reference to Chart
  # Optional field, not all Events have seating chart
  chart = models.ForeignKey(Chart, blank=True, null=True)

  # Unifies the way to get weekday from events with self.day or self.weekday
  def get_uniform_weekday(self):
    if not self.day:
      return self.weekday
    else:
      return self.day.weekday()

  @staticmethod
  def week_from_date(date):
    return Term.current_term().term_week_of_date(date)

  # the date of the event for a given week
  def date_for_week(self, week):
    start_date = Term.current_term().start
    event_week = start_date + timedelta(weeks=week)
    return event_week + timedelta(days = self.weekday)

  # checks for time conflicts between events. Returns True if conflict exists.
  def check_time_conflict(self, event):
    return (self.end > event.start) and (event.end > self.start)

  def get_absolute_url(self):
    return reverse('schedules:event-detail', kwargs={'pk': self.pk})

  def __unicode__(self):
    if self.day:
      date = self.day
    else:
      date = self.get_weekday_display()
    return "%s %s [%s - %s] %s" % (date, self.weekday, self.start.strftime('%H:%M'), self.end.strftime('%H:%M'), self.name)




'''
Schedules stack on top of each other to create a master schedule for each trainee
Base schedules may include rising schedule, meal schedule, class schedule, night schedule
Special schedules may include a specific campus's work schedule (UCLA, USC, OCC, PCC), ITERO, service week, Thanksgiving
(e.g. Campus - CHAP - Chapman University - Orange, Class - General Class, Conference - Memorial Day Meals)
A complete schedule would result from something like
Rise + meal + class + UCLA work + UCLA study + night = schedule for UCLA trainee for a normal week
Schedules can not be edited, only cloned + deactivated.
All active schedules carry over from term to term -> 4th termres taken off,
1st termers addee
Deactivation governed by length of trainees attached to schedule
It is done by taking trainees off schedules, this prevents human
error of accidentally reactivating a schedule with a stale set of
trainees attached to it
'''
class Schedule(models.Model):

  # Add filter choices here.
  TRAINEE_FILTER = (
    ('MC', 'Main Classroom'), # A for all trainees
    ('FY', 'First Year'),
    ('SY', 'Second Year'),
    ('TE', 'Team'),
    ('YP', 'YP'),
    ('CH', 'Children'),
    ('MA', 'Manual')
  )

  name = models.CharField(max_length=255)

  # Optional comments to describe schedule
  comments = models.CharField(max_length=250, blank=True)

  # which trainee this schedule belongs to
  trainees = models.ManyToManyField(Trainee, related_name="schedules", blank=True)

  # which events are on this schedule
  events = models.ManyToManyField(Event, blank=True, related_name="schedules")

  # For override calculation with services?, could -1
  priority = models.SmallIntegerField()

  # weeks schedule is active in selected season (e.g. [1,2,3,4,5,6,7,8,9,10])
  # max_length=50 fits exactly 1 to 20 with commas and no spaces
  weeks = models.CommaSeparatedIntegerField(max_length=50, default='0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19', blank=True, null=True)

  # Only active schedule used for term schedule calculation
  # active = models.BooleanField(default=True)

  # None means valid for both spring + fall
  season = models.CharField(max_length=6,
                choices=(
                  ('Spring', 'Spring'),
                  ('Fall', 'Fall'),
                  ('All', 'All')
                ),
                default=None)

  # Choose auto fill trainees or manually selecting trainees
  trainee_select = models.CharField(max_length=2, choices=TRAINEE_FILTER)

  # Choose which team roll this schedule shows up on
  team_roll = models.ForeignKey(Team, related_name='schedules', blank=True, null=True)

  date_created = models.DateTimeField(auto_now=True)

  import_to_next_term = models.BooleanField(default=False, verbose_name='Auto import schedule to the following term')

  # If a change comes in part-term, a schedule may differ in different parts of the term.
  # Parent schedule points to a full-term version of the most-recent schedule, which can be
  # easily imported to the next term.
  # This is to keep historical data intact. See assign_trainees_to_schedule method
  parent_schedule = models.ForeignKey('self', related_name='parent', null=True, blank=True)

  # is_locked means that for the rest of this term, the trainee set will not change.
  # If this schedule gets moved to the next term, then we should make sure to reset the
  # is_locked flag
  is_locked = models.BooleanField(default=False)

  term = models.ForeignKey(Term, null=True, blank=True)

  query_filter = models.ForeignKey(QueryFilter, null=True, blank=True)

  # Hides "deleted" schedule but keeps it for the sake of record
  is_deleted = models.BooleanField(default=False)

  # Whether the schedule has the week
  def active_in_week(self, week):
    weeks = [int(x) for x in self.weeks.split(',')]
    return week in weeks

  def active_in_period(self, period):
    weeks = [int(x) for x in self.weeks.split(',')]
    for week in weeks:
      if ((week+1) // 2) == period:
        return True
    return False

  @property
  def start_date(self):
    weeks = [int(x) for x in self.weeks.split(',')]
    start_week = weeks[0]
    return Term.current_term().start + timedelta(weeks=start_week - 1)

  @property
  def end_date(self):
    weeks = [int(x) for x in self.weeks.split(',')]
    end_week = weeks[len(weeks)-1]
    return Term.current_term().start + timedelta(weeks=end_week - 1)

  class Meta:
    ordering = ('priority', 'season')

  def __unicode__(self):
    return '[%s] %s - %s schedule' % (self.priority, self.name, self.season)

  def get_absolute_url(self):
    return reverse('schedules:schedule-detail', kwargs={'pk': self.pk})

  @staticmethod
  def current_term_schedules():
    return Schedule.objects.filter(Q(season=Term.current_season()) | Q(season='All')).filter(is_deleted=False)

  # Gets all schedules with event of type in a week. Optionally for a team
  @staticmethod
  def get_all_schedules_by_type_in_weeks(type, weeks, team=None):
    active_schedules = Schedule.current_term_schedules()
    if team:
      active_schedules = active_schedules.filter(team=team)
    active_schedules = active_schedules.filter(events__type=type).distinct()
    wks_reg = comma_separated_field_is_in_regex(weeks)
    # Queries schedules with week defined
    active_schedules = active_schedules.filter(weeks__regex=wks_reg).order_by('priority')
    return active_schedules

  # Gets all schedules for selected trainees within a given list of weeks. Optionally for a team
  # Returns object type QuerySet
  @staticmethod
  def get_all_schedules_in_weeks_for_trainees(weeks, trainees, team=None):
    wks_reg = comma_separated_field_is_in_regex(weeks)
    # print wks_reg, trainees
    # Queries schedules with week defined
    active_schedules = Schedule.current_term_schedules()
    active_schedules = active_schedules.filter(is_deleted=False, weeks__regex=wks_reg, trainees__in=trainees)
    if team:
      active_schedules = active_schedules.filter(team=team)
    active_schedules = active_schedules.distinct().order_by('priority')
    return active_schedules

  @staticmethod
  def get_roll_table_by_type_in_weeks(trainees, type, weeks, team=None):
    '''
      Grab all active schedules of trainees and collapse in order of priority.
      This saves us from recalculated shared schedule common among many trainees,
      We only need to collapse them once.

      get_all_schedules_in_weeks_for_trainees():
      --------------------------------------------------------
        Get all the schedules for all trainees (distinct) in order of inc. priorities


      collapse_priority_event_trainee_table():
      --------------------------------------------------------
        Go through all schedules and override conflicting events trainee roster list
      with trainee list that has higher priority

      Returns table {ev: set([trainee1, trainee2])} in order of increasing start/end time of ev


      export_typed_ordered_roll_list():
      --------------------------------------------------------
        Pull out all remaining events after priority-collapsing of type we are taking roll for

        Returns {event: Set([trainee1, trainee2])


      flip_roll_list():
      --------------------------------------------------------
        we flip the table
        Return object {trainee: [Events, ]}
    '''

    t_set = set(trainees)
    schedules = Schedule.get_all_schedules_in_weeks_for_trainees(weeks, trainees)
    w_tb = EventUtils.collapse_priority_event_trainee_table(weeks, schedules, t_set)
    return EventUtils.flip_roll_list(EventUtils.export_typed_ordered_roll_list(w_tb, type))

  def __get_qf_trainees(self):
    if not self.query_filter:
      return Trainee.objects.all()
    else:
      return Trainee.objects.filter(**eval(self.query_filter.query))

  # TODO: Hailey will write a wiki to explain this function.
  def assign_trainees_to_schedule(self):
    if self.is_locked:
      return

    new_set = self.__get_qf_trainees()
    current_set = self.trainees.all()

    # If the schedules are identical, bail early
    to_add = new_set.exclude(pk__in = current_set)
    to_delete = current_set.exclude(pk__in = new_set)

    if not to_add and not to_delete:
      return

    # Does the schedule need to be split?
    term = Term.current_term()
    if term == None or datetime.now().date() > term.end:
      return

    if datetime.now().date() < term.start:
      week = -1
    else:
      week = term.term_week_of_date(datetime.today().date())

    weeks = eval(self.weeks)

    # todo(import2): this doesn't work yet
    if False: #(len(Set(range(0, week + 1)).intersection(weeks_set))> 0):
      # Splitting
      s1 = Schedule(name=self.name, comments=self.comments,
              priority=self.priority, season=self.season, term=term)
      s2 = Schedule(name=self.name, comments=self.comments,
              priority=self.priority, season=self.season, term=term)

      if self.parent_schedule:
        s1.parent_schedule = self.parent_schedule
        s2.parent_schedule = self.parent_schedule
      else:
        s1.parent_schedule = self
        s2.parent_schedule = self

      sched_weeks = [int(x) for x in self.weeks.split(',')]
      s1_weeks = []
      s2_weeks = []
      for x in sched_weeks:
        if x <= week:
          s1_weeks.append(x)
        else:
          s2_weeks.append(x)

      s1.weeks = str(s1_weeks)
      s2.weeks = str(s2_weeks)

      s1.is_locked = True

      # only the most recent needs a query_filter.  Older ones don't need it.
      s2.query_filter = self.query_filter
      s1.save()
      s2.save()

      s1.trainees = current_set
      s2.trainees = new_set

      s1.save()
      s2.save()

      self.trainees = []
      self.is_locked = True
      self.save()
    else:
      # No split necessary
      self.trainees = new_set
      self.save()

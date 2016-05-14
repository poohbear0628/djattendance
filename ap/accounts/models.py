from django.conf import settings
from datetime import date, datetime

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
  PermissionsMixin
from django.core.mail import send_mail
from django.utils.http import urlquote

from aputils.models import Vehicle, Address, EmergencyInfo
from terms.models import Term
from teams.models import Team
from houses.models import House, Bunk
# from services.models import Service
from badges.models import Badge
from localities.models import Locality
from collections import OrderedDict
from copy import copy

""" accounts models.py
The user accounts module takes care of user accounts and
utilizes/extends Django's auth system to handle user authentication.

USER ACCOUNTS
  Because we want to use the user's email address as the unique
  identifier, we have chosen to implement a custom User model,

  ...

PROFILES
  User accounts are extended by Profiles, which contain additional
  information, generally representing roles that various users fill. The two
  most common ones, Trainee and TA, are implemented here. Other examples
  include:
    - every Trainee is also a service worker, so those user accounts also
    have a ServiceWorker profile that contains information needed for the
    ServiceScheduler algorithm
    - before coming to the FTTA, a trainee may have come to short-term.
    These trainees will have a Short-Term profile at that time, and later
    also have a Trainee  profile when they come for the full-time.

  The usage of profiles allows user to have multiple roles at once, and also
  allows a clean transition between roles (e.g. a Short-termer who becomes a
  Trainee and then later a TA can keep the same account throughout).
"""


class APUserManager(BaseUserManager):

  def create_user(self, email, password=None):
    """ Creates a user, given an email and a password (optional) """

    if not email:
      raise ValueError("Users must have an email address")

    user = self.model(email=APUserManager.normalize_email(email))

    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, email, password):
    """ Creates a super user, given an email and password (required) """

    user = self.create_user(email, password=password)

    user.is_admin = True
    user.is_staff = True
    user.is_superuser = True
    user.save(using=self.db)

    return user


class User(AbstractBaseUser, PermissionsMixin):
  """ A basic user account, containing all common user information.
  This is a custom-defined User, but inherits from Django's classes
  to integrate with Django's other provided User tools/functionality
  AbstractBaseUser provides Django's basic authentication backend.
  PermissionsMixin provides compatibility with Django's built-in permissions system.
  """

  email = models.EmailField(verbose_name=u'email address', max_length=255,
                unique=True, db_index=True)

  def _make_username(self):
    return self.email.split('@')[0]

  username = property(_make_username)

  firstname = models.CharField(verbose_name=u'first name', max_length=30)
  lastname = models.CharField(verbose_name=u'last name', max_length=30)
  middlename = models.CharField(verbose_name=u'middle name', max_length=30,
                  blank=True, null=True)
  nickname = models.CharField(max_length=30, blank=True, null=True)
  maidenname = models.CharField(verbose_name=u'maiden name', max_length=30,
                  blank=True, null=True)

  GENDER = (
    ('B', 'Brother'),
    ('S', 'Sister')
  )

  gender = models.CharField(max_length=1, choices=GENDER)
  date_of_birth = models.DateField(null=True)

  def _get_age(self):
    age = date.today() - self.date_of_birth
    return age.days/365

  age = property(_get_age)

  # to accomodate phone number such as: +(yyy)yyyyyyyyyy x.yyyyyy
  phone = models.CharField(max_length=25, null=True, blank=True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)

  objects = APUserManager()

  def get_absolute_url(self):
    return "/users/%s/" % urlquote(self.username)

  def get_full_name(self):
    fullname = '%s %s' % (self.firstname, self.lastname)
    return fullname.strip()

  def get_short_name(self):
    return self.firstname

  def email_user(self, subject, message, from_email=None):
    send_mail(subject, message, from_email, [self.email])

  def __unicode__(self):
    return "%s, %s <%s>" % (self.lastname, self.firstname, self.email)


class Profile(models.Model):
  """ A profile for a user account, containing user data. A profile can be
  thought of as a 'role' that a user has, such as a TA, a trainee, or a
  service worker. Profile files should be pertinent directly to that profile
  role. All generic data should either be in this abstract class or in the
  User model.
  """

  # each user should only have one of each profile
  account = models.OneToOneField(settings.AUTH_USER_MODEL)

  # whether this profile is still active
  # e.g. if a trainee becomes a TA, they no longer need a service worker profile
  active = models.BooleanField(default=True)

  date_created = models.DateField(auto_now_add=True)

  class Meta:
    abstract = True


class TrainingAssistant(Profile):

  badge = models.ForeignKey(Badge, blank=True, null=True)

  services = models.ManyToManyField('services.Service', blank=True)
  houses = models.ManyToManyField(House, blank=True)

  def __unicode__(self):
    return self.account.get_full_name()


'''
Trainees have 
 - need_services count (hard limit to # of services can take)
  - default need_service determined by algo (# services/# trainees)
  - let them relinquish count back to default
 - health (soft weight on how heavy each service should be) (0-10)
 

 - history of services, workload history (avg workload index)
 - service attendance (auto add for missed services)
 - leaveslip (type sickness, approved) count?

Service has
 - workload (how heavy service is)

'''
class Trainee(Profile):

  TRAINEE_TYPES = (
    ('R', 'Regular (full-time)'),  # a regular full-time trainee
    ('S', 'Short-term (long-term)'),  # a 'short-term' long-term trainee
    ('C', 'Commuter')
  )

  type = models.CharField(max_length=1, choices=TRAINEE_TYPES)

  term = models.ManyToManyField(Term)
  date_begin = models.DateField()
  date_end = models.DateField(null=True, blank=True)

  badge = models.ForeignKey(Badge, blank=True, null=True)

  TA = models.ForeignKey(TrainingAssistant, null=True, blank=True)
  mentor = models.ForeignKey('self', related_name='mentee', null=True,
                 blank=True)
  locality = models.ManyToManyField(Locality, blank=True)

  team = models.ForeignKey(Team, null=True, blank=True)
  house = models.ForeignKey(House, null=True, blank=True)
  bunk = models.ForeignKey(Bunk, null=True, blank=True)

  # personal information
  married = models.BooleanField(default=False)
  spouse = models.OneToOneField('self', null=True, blank=True)
  # refers to the user's home address, not their training residence
  address = models.ForeignKey(Address, null=True, blank=True,
                verbose_name='home address')

  # flag for trainees taking their own attendance
  # this will be false for 1st years and true for 2nd with some exceptions.
  self_attendance = models.BooleanField(default=False)

  # calculates what term the trainee is in
  def _calculate_term(self):
    return self.term.all().count()

  current_term = property(_calculate_term)

  def _trainee_email(self):
    return self.account.email

  def get_outstanding_discipline(self):
    o_discipline = []
    for discipline in self.discipline_set.all():
      if not discipline.is_completed():
        o_discipline.append(discipline)
    return o_discipline

  email = property(_trainee_email)  # should just use trainee.account.email

  def __unicode__(self):
    return self.account.get_full_name()
  
  @property
  def current_season(self):
    return Term.current_term().season

  # Handles ev.day correclty and returns all ev in terms of week, weekday
  def compute_prioritized_event_table(self, w_tb, weeks, evs, priority):
    '''
      Handles priority collision detection and normalizes ev.day events
    '''
    for ev in evs:
      if ev.day:
        # manually calculate week if day is specified
        weeks = [ev.week_from_date(ev.day),]
      for w in weeks:
        # absolute date is already calculated
        weekday = ev.weekday
        ev.priority = priority
        day_evnts = w_tb.setdefault((w, weekday), set())

        # check for conflicts. 
        # append ev to list, check for any conflicts (intersectinng time), replace any intersecting evs
        for day_evnt in day_evnts.copy():
          if day_evnt.check_time_conflict(ev):
            # replace ev if conflict
            # delete any conflicted evs
            day_evnts.remove(day_evnt)

        # append after remove all conflicting events
        day_evnts.add(ev)

    return w_tb

  # Create list from table and add absolute date to event
  def export_event_list_from_table(self, w_tb):
    event_list=[]
    for (w, d), evs in w_tb.items():
      for ev in evs:
        date = ev.date_for_week(w)
        # calc date from w
        ev.start_datetime = datetime.combine(date, ev.start)
        ev.end_datetime = datetime.combine(date, ev.end)
        # append a copy of ev to answer list you will return
        event_list.append(copy(ev))
    return event_list

  # events in list of weeks
  def events_in_week_list(self, weeks):
    schedules = self.schedules.filter(is_deleted=False, season=self.current_season).order_by('priority')
    w_tb=OrderedDict()
    for schedule in schedules:
      evs = schedule.events.all()
      w_tb = self.compute_prioritized_event_table(w_tb, weeks, evs)        

    # return all the calculated, composite, priority/conflict resolved list of events
    return self.export_event_list_from_table(w_tb)

  # events in date range.
  def events_in_date_range(self, start, end):
    schedules = self.schedules.filter(is_deleted=False, season=self.current_season).order_by('priority')
    # figure out which weeks are in the date range.
    c_term = Term.current_term()
    start_week = c_term.term_week_of_date(start)
    end_week = c_term.term_week_of_date(end)
    weeks = range(start_week, end_week + 1)
    w_tb=OrderedDict()
    # for every schedule, filter events to get events in the date range.
    for schedule in schedules:
      evs = schedule.events.filter(weekday__gte=start.weekday(), weekday__lte=end.weekday())
      # create week table
      w_tb = self.compute_prioritized_event_table(w_tb, weeks, evs)
    # create event list.
    return self.export_event_list_from_table(w_tb)
    # TODO: Think more about this

  @property
  def events(self):
    schedules = self.schedules.filter(is_deleted=False, season=self.current_season).order_by('priority')
    w_tb=OrderedDict()
    # create week table
    for schedule in schedules:
      evs = schedule.events.all()
      weeks = [int(x) for x in schedule.weeks.split(',')]
      w_tb = self.compute_prioritized_event_table(w_tb, weeks, evs, schedule.priority)

    # return all the calculated, composite, priority/conflict resolved list of events
    return self.export_event_list_from_table(w_tb)

# Statistics / records on trainee (e.g. attendance, absences, service/fatigue level, preferences, etc)
class Statistics(models.Model):
  trainee = models.OneToOneField(Trainee, related_name='statistics', null=True, blank=True)

  # String containing book name + last chapter of lifestudy written ([book_id]:[chapter], Genesis:3)
  latest_ls_chpt = models.CharField(max_length=400, null=True, blank=True)

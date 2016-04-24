from random import randint

from django.db import models
from django.utils import timezone

from schedules.constants import WEEKDAYS

from .constants import GENDER
from .constants import WORKER_ROLE_TYPES


class Category(models.Model):
    """
    Defines a service category such as Clean-up, Guard, Mopping, Chairs, etc.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name

# Should be able to define number and type of workers needed. 
# Also allow volunteers, extras to be added

# TODO: Add service rolls
class Service(models.Model):
    """
  Defines a weekly service, whether rotational (e.g. Tuesday Breakfast Clean-up)
    or designated (e.g. Attendance Project, Vehicle Maintenance, or Lights)

    Repeats weekly unless day is specified for a one-off service

    Each Service only covers one time slot (e.g. Tuesday Supper Cleanup)
    """

    # Name is made primary key so any changes would create a new service automatically.
    name = models.CharField(max_length=100, unique=True)
    # the event's shortcode, e.g. FMoC or Lights
    code = models.CharField(max_length=10)

    # Category groups all the individual services into one group for editting
    # e.g. Monday Breakfast Cleanup, Tuesday Breakfast Cleanup
    category = models.ForeignKey('Category', related_name="services")
    schedule = models.ManyToManyField('SeasonalServiceSchedule', related_name="services")

    active = models.BooleanField(default=True)
    designated = models.BooleanField(default=False)
    gender = models.CharField(max_length=1, choices=GENDER, default='E')

    # Total number of workers required for this service
    workers_required = models.PositiveSmallIntegerField(default=1)

    '''  
    - Specifies types of worker groups and how many to choose from and 
      what role to give them as well as gender roles
    - Also doubles to hold designated service workers.
    '''
    worker_groups = models.ManyToManyField('WorkerGroup', 
                            through='AssignmentPool')



    weekday = models.PositiveSmallIntegerField(choices=WEEKDAYS)
    start = models.TimeField()
    end = models.TimeField()
    # Optional day creates a one-off service that doesn't repeat weekly
    day = models.DateField(blank=True, null=True)

    last_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

''' 
TODO: Need a powerful editor for service worker groups for service schedulers 
to categorize trainees as workers based on qualifications/criteria

e.g.
Instance: 3/25/2016 Saturday Dinner Cleanup
 -> workers through assignments (roles)
Service: Cleanup
AssignmentPool: Cleanup star
WorkerGroup: 1st term stars

'''
class AssignmentPool(models.Model):
    service = models.ForeignKey('Service')
    worker_group = models.ForeignKey('WorkerGroup')
    workers_required = models.PositiveSmallIntegerField(default=1)
    # on a scale of 1-12, with 12 being the most intense (workload 
    # is potentially different for different roles depending within same service)
    workload = models.PositiveSmallIntegerField(default=3)
    role = models.CharField(max_length=3, choices=WORKER_ROLE_TYPES, default='wor')
    # Optional gender requirement + qualification requirement
    gender = models.CharField(max_length=1, choices=GENDER, default='E')

    last_modified = models.DateTimeField(auto_now=True)

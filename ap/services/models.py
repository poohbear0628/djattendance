from django.db import models
from django.contrib.auth.models import Group
from django.utils import timezone
from .constants import WORKER_ROLE_TYPES, GENDER
# from ss.models import WorkerGroup
# from ss.models import Qualification

""" services models.py

The services model defines both weekly and permanent (designated) services in the

Data Models:
    - Category: This is a broad category that contains specific services. For
    example,Cleanup is a category that contains services such as Tuesday
    Breakfast Cleanup or Saturday Lunch Cleanup. Guard contains Guards A, B, C,
    and D.

    - Service: This refers to a specific service that repeats on a weekly basis.
    I.e. Tuesday Breakfast Prep is a service. It repeats every week. A specific
    instance of that service is defined in the service scheduler module as a
    service Instance.

    - Period: This is a period in which services are active and generally
    changes with the schedule of the training. Most of the time, the regular
    FTTA schedule will be in effect, but there are exceptions such as Service
    Week and the semiannual training.
"""

class Category(models.Model):
    """
    Defines a service category such as Clean-up, Guard, Mopping, Chairs, etc.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.name


class SeasonalServiceSchedule(models.Model):
    """
    Defines a service period such as Pre-Training, FTTA regular week, etc.
    """

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, blank=True, null=True)
    isActive = models.BooleanField(default=True)

    # every service have different workload,
    # for example guard is much more intense than cleaning
    workload = models.IntegerField(default=1)

    def __unicode__(self):
        return self.name

from random import randint


"""

Worker Specs

 - gender
 - qualifications
 - WORKER_ROLE_TYPES
 - term_types
 - worker_group
 - count
 - workload

worker_group join


class Assignment(models.Model):

    ROLES = WORKER_ROLE_TYPES

    # schedule = models.ForeignKey('Schedule')
    instance = models.ForeignKey(Instance)
    worker = models.ForeignKey(Worker)
    role = models.CharField(max_length=3, choices=ROLES, default='wor')




"""

# Should be able to define number and type of workers needed. 
# Also allow volunteers, extras to be added
class Service(models.Model):
    """
	Defines a weekly service, whether rotational (e.g. Tuesday Breakfast Clean-up)
    or designated (e.g. Attendance Project, Vehicle Maintenance, or Lights)
    """

    # according to datetime.date.today()
    WEEKDAYS = (
        ('0', 'Monday'),
        ('1', 'Tuesday'),
        ('2', 'Wednesday'),
        ('3', 'Thursday'),
        ('4', 'Friday'),
        ('5', 'Saturday'),
        ('6', 'Sunday'),
    )

    name = models.CharField(max_length=100)

    category = models.ForeignKey(Category, related_name="services")
    period = models.ManyToManyField(Period, related_name="services")

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
    worker_groups = models.ManyToManyField('ss.WorkerGroup', 
                            through='ServiceWorkerGroup')

    weekday = models.CharField(max_length=1, choices=WEEKDAYS, default=str(randint(0,6)))
    start = models.TimeField(default=timezone.now())
    end = models.TimeField(default=timezone.now())

    def __unicode__(self):
        return self.name

''' 
TODO: Need a powerful editor for service worker groups for service schedulers 
to categorize trainees as workers based on qualifications/criteria

e.g.
Instance: 3/25/2016 Saturday Dinner Cleanup
 -> workers through assignments (roles)
Service: Cleanup
ServiceWorkerGroup: Cleanup star
WorkerGroup: 1st term stars

'''
class ServiceWorkerGroup(models.Model):
    service = models.ForeignKey(Service)
    worker_group = models.ForeignKey('ss.WorkerGroup')
    workers_required = models.PositiveSmallIntegerField(default=1)
    # on a scale of 1-12, with 12 being the most intense (workload 
    # is potentially different for different roles depending within same service)
    workload = models.PositiveSmallIntegerField(default=3)
    role = models.CharField(max_length=3, choices=WORKER_ROLE_TYPES, default='wor')
    # Optional gender requirement + qualification requirement
    gender = models.CharField(max_length=1, choices=GENDER, default='E')


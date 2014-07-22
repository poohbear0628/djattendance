from django.db import models
from django.db.models import Q
from datetime import datetime
from operator import itemgetter

from django.db.models import Sum, Max, Count

from accounts.models import Profile, Trainee, TrainingAssistant
from services.models import Service
from terms.models import Term
from teams.models import Team
from schedules.models import Event


""" SS models.py

The SS (Service Scheduler) module functions to assign services to trainees each
week.

Data Models:
    - Instance: to be completed.
    - WorkerGroup: to be completed.
    - ExceptionRequest: to be completed.
    - Filters: to be completed.
    - Scheduler: to be completed.
    - Assignment: to be completed.
    - Configuration: to be completed.
"""


class Worker(Profile):

    qualifications = models.ManyToManyField('Qualification')
    designated = models.ManyToManyField(Service)

    # TODO: store service history

    workload = models.PositiveIntegerField()
    weeks = models.PositiveSmallIntegerField()

    def _avg_workload(self):
        return self.workload / float(self.weeks)

    avg_workload = property(_avg_workload)

    def __unicode__(self):
        return self.account

class WorkerGroup(models.Model):

    name = models.CharField(max_length=100)
    desc = models.CharField(max_lenght=255)

    workers = models.ManyToManyField(Trainee, related_name="workergroups", null=True, blank=True)

    def __unicode__(self):
        return self.name


class Instance(models.Model):
    """
    Defines one instance of a service (e.g. 6/13/14 Tuesday Breakfast Prep)
    """

    WEEKDAY = (
        ('Sun', 'Sunday'),
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
    )

    service = models.ForeignKey(Service, related_name="instances")
    period = models.ForeignKey(Period, related_name="instances")

    date = models.DateField()

    # event created correponding to this service instance
    event = models.ForeignKey(Event, null=True, blank=True)

    def __unicode__(self):
        return self.date + " " + self.service.name


class Exception(models.Model):
    """
    Defines an ineligibility rule for workers to certain services.
    Exception types should extend this abstract class by implementing logic for
    checking service assignments against exceptions in check()
    """


    start = models.DateField()
    end = models.DateField(null=True, blank=True)

    active = models.BooleanField(default=False)  # whether this exception is in effect or not

    trainees = models.ManyToManyField(Worker, related_name="exception")

    def check(self):
        raise NotImplementedError('Exception should implement check logic')

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True


class Qualification(models.Model):
    """
    Defines an eligibility for workers to certain services.
    The opposite of Exception in many ways.
    """
    name = models.CharField(max_length=200)
    desc = models.TextField()


class Schedule(models.Model):
    """
    A service schedule for one week in the training.
    """

    start = models.DateField()  # should be the Tuesday of every week
    desc = models.TextField()
    period = models.ForeignKey(Period)

    instances = models.ManyToMany(Instance)

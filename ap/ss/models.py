from datetime import datetime, timedelta

from django.db import models
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

Abbreviations:
    sv = service
    inst = instance
"""


class Worker(Profile):

    qualifications = models.ManyToManyField('Qualification')
    designated = models.ManyToManyField(Service, related_name='designated_workers')

    services_eligible = models.ManyToManyField(Instance, related_name='workers_eligible')

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

    workers = models.ManyToManyField(Worker, through='Assignment', null=True)

    def _start(self):
        return datetime.combine(self.date, self.service.start)

    start = property(_start)

    def _end(self):
        return datetime.combine(self.date, self.service.end)

    end = property(_end)

    def __unicode__(self):
        return self.date + " " + self.service.name


class Assignment(models.Model):
    """
    Defines a relationship between a worker and a service instance
    """

    ROLES = (
        ('*', 'Star'),
        ('*it', 'Star in training'),
        ('os', 'Overseer'),
        ('oa', 'Overseer Assistant'),
        ('wor', 'Worker'),
        ('vol', 'Volunteer'),
        ('sub', 'Substitute'),
        ('1st', '1st timer'),
    )

    role = models.CharField(max_length=3, choices=ROLES, default='wor')


class Exception(models.Model):
    """
    Defines an ineligibility rule for workers to certain services.
    Exception types should extend this abstract class by implementing logic for
    checking service assignments against exceptions in check()
    """

    name = models.CharField(max_length=100)
    desc = models.Charfield(max_length=255)

    start = models.DateField()
    end = models.DateField(null=True, blank=True)  # some exceptions are just evergreen

    active = models.BooleanField(default=True)  # whether this exception is in effect or not

    trainees = models.ManyToManyField(Worker, related_name="exception")

    def check(self, worker, instance):
        """
        Define logic to check whether assigning worker to instance would violate
        this exception's condition (e.g. health, workload, schedule, etc.)
        returns False if exception is violated.
        """
        raise NotImplementedError('Exception should implement check logic')

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True


class ScheduleException(Exception):
    """ Occurs because of schedule conflict (e.g. YP trainee are gone Sat. nights).
    Often associated with team schedules, but could also be personal """

    team = models.ForeignKey(Team, null=True, blank=True)  # which team this is associated with, if any

    services = models.ManyToManyField(Service)  # which services are exempted

    def check(self, worker, instance):
        if instance.service in self.services:
            return False
        else:
            return True


class ServiceException(Exception):
    """ Virtually identically to ScheduleExceptions, but has to do with special service
    exceptions (e.g. piano service, bus drivers, books accounting) """

    service = models.ForeignKey(Team)  # which service this is associated with

    services = models.ManyToManyField(Service)  # which services are exempted

    def check(self, worker, instance):
        if instance.service in self.services:
            return False
        else:
            return True


class WorkloadException(Exception):
    """ Allows setting a custom workload ceiling for workers """

    workload = models.PositiveSmallIntegerField()

    def check(self, worker, instance):
        if worker.workload + instance.workload > self.workload:
            return False
        else:
            return True


class HealthException(Exception):
    """ Exempts a worker from a set of services because of health reasons. """

    services = models.ManyToManyField(Service)  # which services are exempted

    def check(self, worker, instance):
        if instance.service in self.services:
            return False
        else:
            return True


class Qualification(models.Model):
    """
    Defines an eligibility for workers to certain services.
    """
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)


class Schedule(models.Model):
    """
    A service schedule for one week in the training.
    """

    start = models.DateField()  # should be the Tuesday of every week
    desc = models.TextField()
    period = models.ForeignKey(Period)

    instances = models.ManyToMany(Instance)

    @classmethod
    def create(cls, start, desc, period):
        schedule = cls(start=start, desc=desc, period=period)

        # create instances
        for sv in self.period.services:
            inst = Instance(service=sv, period=self.period)
            # since the week starts on Tuesday, add 6 and modulo 7 to get the delta
            inst.date = self.start + timedelta(days=((int(sv.weekday) + 6) % 7))
            inst.save()
            self.instances.add(inst)  # add created instance to this schedule

        # assign designated services
        for dsv in self.instances.filter(service__designated=True):
            dsv.workers.add(dsv.service.designated_workers)

        # calculate solution space
        """ calculate the solution space:
        the solution space is a correlation of services to eligible workers and
        workers to services they are eligible for
        this is the primary data set from which the algo will determine which
        workers to assign to which services

        # this is a good use case for a graph data struct, but I don't know of any in Python....
        # for now, use postgres hstore
        solution_space = {
             # for each service instance, list all eligible workers
            'services': {
                'instance': set(trainee, trainee, trainee, trainee,...)
                ...
            },
            # for each each worker, list all services eligible
            'workers': {
                'worker': set(instance, instance, instance, instance,...)
            }
        }
    """

        # calculate mutually exclusive services
        

        return schedule

    """ ss algorithm psuedocode """
    def initialize(self):
        """ initialize data structures needed for running algorithm """

        # average workload for schedule
        AVG_WORKLOAD = self.instances.all().aggregate(Avg('workload'))
        # avg_workload + margin = workload ceiling
        WORKLOAD_MARGIN = 2


        

        """ calculate mutually exclusive services:
        services will have schedule conflicts with each other
        based on their start/end times and also recovery time
        e.g. a trainee cannot simultaneously be on supper cleanup and restroom cleaning
        and a trainee should not have breakfast cleanup right after breakfast prep
        """
        service_conflicts = {
            instance: set(instance, instance, instance, instance, instance)
            ...
        }


    def assign(self, worker, instance, commit=False):
        """ assign a worker to a service instance """

        warnings = WarningList()

        # check worker's qualifications match instance
        for qualification in instance.service.qualifications:
            if qualification not in worker.qualifications:
                warnings.append(QualificationNotMetWarning(worker, instance, qualification))

        # check worker's exceptions against instance
        for exception in worker.exceptions:
            if not exception.check(worker, instance):
                warnings.append(ExceptionViolatedWarning(worker, instance, exception))

        # check worker's new workload versus workload ceiling
        if (worker.workload + instance.workload) > (AVG_WORKLOAD + WORKLOAD_MARGIN):
            warnings.append(WorkloadExcessiveWarning(worker, instance))

        warnings.issue()  # send warnings to notification queue

        if commit:  # dry-run by default to preview warnings
            instance.workers = worker  # assign worker to instance
            # recalculate solution space
            if worker.workload > (AVG_WORKLOAD + WORKLOAD MARGIN):
                # deem inelligible for more services
                for service in solution_space['workers'][worker]:
                    solution_space['services'][service].remove(worker)
                solution_space['workers'][worker] = set()
            else:
                # remove mutually exclusive services
                for service in service_conflicts[instance]:
                    solution_space['services'][service].remove(worker)
                    solution_space['workers'][worker].remove(service)

    def unassign(self, worker, instance, commit=False):
        """ OLJ """
        pass

    def fill(self, instances=all, workers=all):  # defaults to entire schedule
        """ auto-fills a set of instances given a set of workers """

        unfilled_instances = instances

        # yes, i know nested is bad.
        until instances are filled:
            instance = weighted_random(unfilled_instances)  # selects which service to fill first based on which has the smallest pool of eligible workers
            until instance is filled:
                eligible_workers = intersection(workers, solution_space['services'][instance])
                """ calculate a heuristic for selecting a worker to assign
                based on: how many remaining services workers are eligible for (prefer workers who have fewer options)
                workers' workload (prefer workers with lower workloads)
                variety (prefer workers who have not had this service as many times)
                workers' historical workload (prefer workers who have lower avg workloads)
                """
                assign(heuristic_select(eligible_workers), instance)
            unfilled_instances.remove(instance)

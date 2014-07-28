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

    workers = models.ManyToManyField(Worker, through='Assignment')

    def __unicode__(self):
        return self.date + " " + self.service.name


class Assignment(models.Model):
    """
    Defines a relationship between a worker and a service instance
    """

    ROLES = (
        ('*', 'Star'),
        ('os', 'Overseer'),
        ('oa', 'Overseer Assistant'),
        ('w', 'Worker'),
        ('v', 'Volunteer'),
        ('s', 'Substitute'),
        ('1', '1st termer'),
    )

    role = models.CharField(max_length=1, choices=ROLES)


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

    def check(self, worker, instance):
        """
        Define logic to check whether assigning worker to instance would violate
        this exception's condition (e.g. health, workload, schedule, etc.)
        returns Boolean
        """
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


    """ ss algorithm psuedocode """"
    def initialize(self):
        """ initialize data structures needed for running algorithm """

        # average workload for schedule
        AVG_WORKLOAD = self.instances.all().aggregate(Avg('workload'))
        # avg_workload + margin = workload ceiling
        WORKLOAD_MARGIN = 2


        """ calculate the solution space:
        the solution space is a correlation of services to eligible workers and
        workers to services they are eligible for
        this is the primary data set from which the algo will determine which
        workers to assign to which services
        """
        # this is a good use case for a graph data struct, but I don't know of any in Python....
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

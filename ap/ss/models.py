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

    def _services_exempted(self):
        exemptions = set()
        for exception in self.exceptions:
            exemptions.add(exception.services.all())
        return exemptions

    services_exempted = property(_services_exempted)

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

    def _filled(self):
        return self.workers.count() >= self.service.workers_required
    filled = proprety(_filled)

    def _workers_needed(self):
        return self.service.workers_required - self.workers.count()
    workers_needed = property(_workers_needed)

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

    trainees = models.ManyToManyField(Worker, related_name="exceptions")
    services = models.ManyToManyField(Service)

    def check(self, worker, instance):
        if instance.service in self.services:
            return False
        else:
            return True

    def get_absolute_url(self):
        return "/ss/exceptions/%i/" % self.id

    def __unicode__(self):
        return self.name


class Qualification(models.Model):
    """
    Defines an eligibility for workers to certain services.
    """
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)


class LogEvent(models.Model):

    EVENT_TYPES = (
        ('d', 'debug'),
        ('i', 'info'),
        ('w', 'warning'),
    )

    schedule = models.ForeignKey('Schedule', related_name='log')

    type = models.CharField(max_length=1, choices=EVENT_TYPES)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    @classmethod
    def exception_violated(cls, schedule, exception, instance, worker):
        event = cls(schedule=schedule, type='w')
        event.message = "Exception Violated: Assigning %s to %s violates exception <a href='%s'>%s</a>" % worker, intance, exception.get_absolute_url(), exception
        return event

    @classmethod
    def workload_excessive(cls, schedule, instance, worker, workload):
        event = cls(schedule=schedule, type='w')
        event.message = "Excessive Workload: Assigning %s to %s increases workload to %d" % worker, instance, workload
        return event

    @classmethod
    def debug(schedule, message):
        event = cls(schedule=schedule, type='d')
        event.message = message
        return event


class Schedule(models.Model):
    """
    A service schedule for one week in the training.
    """

    start = models.DateField()  # should be the Tuesday of every week
    desc = models.TextField()
    period = models.ForeignKey(Period)

    # the actual schedule 
    instances = models.ManyToMany(Instance)

    # workload calculations
    workload_margin = models.PositiveSmallIntegerField(default=2)

    # average workload for this schedule
    _avg_workload = self.instances.all().aggregate(Avg('workload'))/Worker.objects.filter(active=True)
    avg_workload = proprety(_avg_workload)

    # avg_workload + margin = workload ceiling
    _workload_ceiling = self.avg_workload + self.workload_margin
    workload_ceiling = property(_workload_ceiling)

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
        
        return schedule

    def assign_designated_services(self):
        # assign designated services
        for dsv in self.instances.filter(service__designated=True):
            dsv.workers.add(dsv.service.designated_workers)

    def calculate_solution_space(self):
        # calculate solution space
        for worker in Worker.objects.filter(active=True):
            # clear any old eligibility data (e.g. from previous week)
            worker.services_eligible.clear()
            
            # if over workload ceiling, not eligible for any services, so skip
            if worker.workload >= self.workload_ceiling:
                continue

            # first assume everyone is eligible for every service
            worker.services_eligible.add(self.instances.all())

            # then remove based on exceptions
            worker.services_eligible.remove(worker.services_exempted)

            # remove based on gender
            if worker.account.gender == 'B':
                g = 'S'
            else:
                g = 'B'
            worker.services_eligible.remove(self.instances.filter(service__gender=g))


    def assign(self, workers, instance, commit=False):
        """ assign workers to a service instance """

        warnings = list()
        if type(workers) is not list: workers = [ workers ]  # convert to list if passed single worker

        for worker in workers:
            # check worker's exceptions against instance
            for exception in worker.exceptions:
                if not exception.check(worker, instance):
                    warnings.append(LogEvent.exception_violated(self, exception, instance, worker))

            # check worker's new workload versus workload ceiling
            if (worker.workload + instance.workload) > self.workload_ceiling:
                warnings.append(LogEvent.workload_excessive(self, instance, worker, worker.workload + instance.workload))

            if commit:  # dry-run by default to preview warnings
                instance.workers.add(worker)  # assign worker to instance
                warning.save() for warning in warnings  # write warnings to log
                # recalculate solution space
                if worker.workload > self.workload_ceiling:
                    worker.services_eligible.clear() 
                else:
                    # remove same-day services
                    worker.services_eligible.remove(self.instances.filter(date=instance.date))

        return warnings

    def unassign(self, worker, instance, commit=False):
        """ OLJ """
        pass

    def heuristic(self, instance):
        """ heuristic to choose a worker from an instance's eligible workers """
        # how many trainees are eligible for this service
        if instance.workers_eligible <= instance.workers_needed:
            return instance.workers_eligible  # return everyone if there's not enough
        # how many services the trainee is elilgible for
        if 
        # trainee's current workload
        # trainee's service history (variety)
        # trainee's trainees historical workload



    def fill(self, instances): 
        """ takes a list of instances and automatically assigns workers to them """

        # yes, i know nested loops are bad.
        while not instances:
            # sorts instances by number of eligilble workers
            instance = instances.sort(key=lambda inst: inst.workers_eligible.count()).pop()
            while not instance.filled and instance.workers_eligible > 0:
                assign(heuristic(instance), instance, commit=True)

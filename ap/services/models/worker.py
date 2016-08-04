from datetime import datetime, timedelta

from django.db import models
from week_schedule import *

from collections import Counter

""" Service models.py

Data Models:
    - Worker: a service worker who can fill a role on a service (e.g. trainee, short-termer, LSM hosp.)
    - WorkerGroup: a group of service workers (which can be defined by the service schedulers)

Related Models:
    - services.Service: a weekly service recurring one per week
    - services.Category: a way to group services of similar types together (e.g. Restroom cleaning)
    - services.Period: refers to time of year this service is active (e.g. semiannual, service week, FTTA)

Abbreviations:
    sv = service
    inst = instance
"""

class Qualification(models.Model):
    """
    Defines an eligibility for workers to certain services.
    """
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

# Has exceptions
class Worker(models.Model):
    # Field put here so if trainee deleted will auto-delete worker model
    trainee = models.OneToOneField('accounts.Trainee')
    qualifications = models.ManyToManyField('Qualification', blank=True, related_name='workers')
    designated = models.ManyToManyField(
        'Service', related_name='designated_workers', blank=True)

    services_eligible = models.ManyToManyField(
        'Service', related_name='workers_eligible', blank=True)

    #TODO: Add in service_history, id of all prev services?,
    @property
    def service_history(self):
        # Cache only exists for as long as this object exists so state should be accurate
        if not hasattr(self, 'service_history'):
            self.service_history = [(a.service, a.service_slot) for a in self.assignments.order_by('service__week_schedule__start')]
        # Return list of historical services assigned sorted by week_schedule start time
        return self.service_history

    @property
    def service_frequency(self):
        # cache results
        if not hasattr(self, '_service_freq'):
            self._services_freq = Counter()
            for a in self.assignments.all():
                self._services_freq[(a.service, a.service_slot)] += 1

        return self._services_freq




    # dictionary of all the types and freq

    # level from 0 to 10, 10 is healthy, 0 is dying
    health = models.PositiveIntegerField(default=10)

    services_cap = models.PositiveSmallIntegerField(default=3)

    # workload = models.PositiveIntegerField(default=3)  #history object
    # weeks = models.PositiveSmallIntegerField(default=1, blank=True, null=True)  #??? what does this do?

    last_modified = models.DateTimeField(auto_now=True)

    @property
    def services_needed(self):
        '''
            Calculates services needed for worker for current week_schedule
        '''
        cws = WeekSchedule.current_week_schedule()
        return self.services_cap - self.assignments.filter(week_schedule=cws).count()


    @property
    def avg_workload(self):
        return self.workload / float(self.weeks)

    @property
    def services_exempted(self):
        # TODO: support events in the future
        exemptions = set()
        for exception in self.exceptions:
            exemptions.add(exception.services.all())
        return exemptions

    def __unicode__(self):
        return self.trainee.full_name

    class Meta:
        ordering = ['trainee__firstname', 'trainee__lastname']



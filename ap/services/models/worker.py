from datetime import datetime, timedelta

from django.db import models

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
        return name

# Has exceptions
class Worker(models.Model):
    # Field put here so if trainee deleted will auto-delete worker model
    trainee = models.OneToOneField('accounts.Trainee')
    qualifications = models.ManyToManyField('Qualification', blank=True)
    designated = models.ManyToManyField(
        'Service', related_name='designated_workers', blank=True)

    services_eligible = models.ManyToManyField(
        'Service', related_name='workers_eligible')

    #TODO: Add in service_history, id of all prev services?, 
    # dictionary of all the types and freq

    # level from 0 to 10, 10 is healthy, 0 is dying
    health = models.PositiveIntegerField(default=10)

    # services_needed = models.PositiveSmallIntegerField(blank=True, null=True)

    workload = models.PositiveIntegerField(default=3)  #history object
    weeks = models.PositiveSmallIntegerField(default=1, blank=True, null=True)  #??? what does this do?

    def _avg_workload(self):
        return self.workload / float(self.weeks)

    avg_workload = property(_avg_workload)

    def _services_exempted(self):
        # TODO: support events in the future
        exemptions = set()
        for exception in self.exceptions:
            exemptions.add(exception.services.all())
        return exemptions

    services_exempted = property(_services_exempted)

    def __unicode__(self):
        return str(self.trainee)



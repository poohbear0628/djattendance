from django.db import models

from services.constants import WORKER_ROLE_TYPES, GENDER



class Assignment(models.Model):
    """
    Defines a relationship between a worker and a service instance
    """

    Week_schedule = models.ForeignKey('WeekSchedule', related_name='assignments')

    # role of worker in assignment (default worker, 'wor')
    role = models.CharField(max_length=3, choices=WORKER_ROLE_TYPES, default='wor')
    # on a scale of 1-12, with 12 being the most intense (workload 
    # is potentially different for different roles depending within same service)
    workload = models.PositiveSmallIntegerField(default=3)
    # Optional gender requirement + qualification requirement
    gender = models.CharField(max_length=1, choices=GENDER, default='E')


    service = models.ForeignKey('Service')
    # Get role + workload
    service_worker_group = models.ForeignKey('WorkerGroup')

    # schedule = models.ForeignKey('Schedule')
    workers = models.ManyToManyField(
        'Worker', related_name="assigned_services", blank=True)


    workers_required = models.PositiveSmallIntegerField(default=1)
    # workers_needed = property(_workers_needed)

    @property
    def _workers_needed(self):
        return self.workers_required - self.workers.count()

    # boolean determines if assignment made should be pinned, not altered by
    # flow algo, taken out of graph, trainee need services decremented (safest way to do it)
    # Maybe cost of edge 0?
    pin = models.BooleanField(default=False)
    

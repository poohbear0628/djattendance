from django.db import models
from django.contrib.postgres.fields import HStoreField

from django.contrib.auth.models import Group


'''
WorkerGroup inherits from django Group so service 

designated service 
 - permission
regular service
general groups 
seasonal groups

View functions:
1st term worker group
sisters worker group

group -> run when add a trainee
validator/updater for workergroups

generic worker groups -> auto-generated

Service Worker Group Trainee Filter Picklist

'''


class QueryFilter(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)

    # Dictionary of all filters applied to query
    query = HStoreField()

    def __unicode__(self):
        return self.name, '-', self.query


'''
Will either be a filter workergroup or manual workergroup

WorkerGroup can created via:

 - filter
    - http://ap.ftta.lan/api/trainees/term/2/?format=json&terms%5B%5D=2&terms%5B%5D=3&hc=false

 - manual assignment
 - doodle

Assignments may be 
 - static
 - rotational
 - weekly manual assignment


Inherits from Group:
 - name          Required. 80 characters or fewer. Any characters are permitted. Example: 'Awesome Users'.
 - permissions   Many-to-many field to Permission:



?? TODO: make workgroup have types, (e.g. designated)

'''
class WorkerGroup(Group):

    # Optional query_filter object. Only this filter or workers 
    # manual assignments allowed at a time
    query_filter = models.ForeignKey('QueryFilter', related_name='filtered_workergroup', 
        blank=True, null=True)

    description = models.TextField(blank=True, null=True)

    active = models.BooleanField(default=True)

    workers = models.ManyToManyField(
        'Worker', related_name="workergroups", blank=True)

    def get_workers(self):
        if not self.filter_str:
            # then it's a manual list of workers
            return self.workers
        else:
            pass
            # Return filtered result

    def __unicode__(self):
        return self.name

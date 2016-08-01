from django.db import models
from django.contrib.postgres.fields import HStoreField
from django_hstore import hstore


from django.contrib.auth.models import Group
from services.models import Worker


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
    description = models.TextField(blank=True, null=True)

    # Dictionary of all filters applied to query
    query = models.TextField()

    def __unicode__(self):
        return self.name
        q = eval(self.query)
        return '%s - %s' % (self.name, '(' + ','.join(['%s=%s' %(k, v) for k, v in q.items()]) + ')')


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
    query_filters = models.ManyToManyField('QueryFilter', related_name='filtered_workergroup')

    description = models.TextField(blank=True, null=True)

    active = models.BooleanField(default=True)

    workers = models.ManyToManyField(
        'Worker', related_name="workergroups", blank=True)

    last_modified = models.DateTimeField(auto_now=True)

    def get_workers(self):
        if not self.query_filters:
            # then it's a manual list of workers
            return self.workers.all()
        else:
            workers = Worker.objects
            # Chain all the filters together to get the composite filter
            for q in self.query_filters.all():
                workers = workers.filter(**eval(q.query))
            # Return filtered result
            return workers


    def __unicode__(self):
        return self.name

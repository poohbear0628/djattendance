from django.db import models
from django.contrib.auth.models import Group

""" SERVICES models.py 
This data model defines services in the training. We organize services in the following way:
    Category: this is a broad category that contains specific services. For example,
    Cleanup is a category that contains services such as Tuesday Breakfast Cleanup or
    Saturday Lunch Cleanup. Guard contains Guards A, B, C, and D. 

    Service: this refers to a specific service that repeats on a weekly basis.
    I.e. Tuesday Breakfast Prep is a service. It repeats every week. A specific instance
    of that service is defined in the service scheduler module as a service Instance.

    Period: this is a period in which services are active and generally changes with
    the schedule of the training. Most of the time, the regular FTTA schedule will be in
    effect, but there are exceptions such as Service Week and the semiannual training.

"""

class Category(Group):
    """
    Defines a service category such as Clean-up, Guard, Mopping, Chairs, etc.
    """
    # name = models.CharField(max_length=75)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class Service(Group):
    """" FTTA service class to define service such as
    Tues. Breakfast Cleanup, Dinner Prep, Guard A, Wednesday Chairs, etc.
    remove two unecessary methods and minor chagens in comments
    This also includes designated services such as Accounting or Lights.
    """

    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category)
    isActive = models.BooleanField(default=True)

    #Every service has different workload to describe its 
	#service hours and service intensity
    workload = models.IntegerField()
	
	#whether this service needs certain qualified trainees
    needQualification = models.BooleanField(blank=True)

	#Service qualification such as Sack lunch star,Kitchen Star,
	#Shuttle Driver, Piano, Usher, etc
    #Note: This is different from permanent designation. For example, 
	#two brothers are be designated as AV brothers,
    #but others brothers have the qualification to serve AV.
	qualifiedTrainees = models.ManyToManyField('accounts.Trainee')

    def __unicode__(self):
        return self.name


class Period(models.Model):
    """Define Service Period such as Pre-Training, FTTA regular week, etc"""

    name = models.CharField(max_length=200)
    description = models.TextField()

    #Service which is in this Period
    service = models.ManyToManyField(Service, related_name="periods")

    startDate = models.DateField('start date')
    endDate = models.DateField('end date')

    def __unicode__(self):
        return self.name

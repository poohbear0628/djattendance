from django.db import models
from service import *
#from users.models import UserAccount

#This is for service scheduler .
#Assign service to trainees

#define service group such as Monday Prep Brothers, etc
class workerGroup(models.Model):

    name = models.CharField(max_length=200)
    service = models.ForeignKey(service)
    period = models.ForeignKey(period)
    numberOfWorkers = models.IntegerField()
    isActive = models.BooleanField()


#service scheduler
class scheduler(models.Model):

    period = models.ForeignKey(period)
    startDate = models.DateField()
    modifiedTime = models.DateTimeField()
    #TODO Trainee = models.ForeignKey(Trainee)


#service assignment
class assignment(models.Model):

    #TODO Trainee=models.ForeignKey(Trainee)
    scheduler = models.ForeignKey(scheduler)
    workerGroup = models.ForeignKey(workerGroup)
    isAbsent = models.BooleanField()
    #subTrainee = models.ForeignKey(Trainee)


#service missed, not necessary
class missed(models.Model):

    #TODO Trainee = models.ForeignKey(Trainee)
    scheduler = models.ForeignKey(scheduler)
    workerGroup = models.ForeignKey(workerGroup)


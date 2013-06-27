from django.db import models
from service.models import *
from django.db.models import Q
from datetime import datetime
from operator import itemgetter
from collections import OrderedDict
from trainees.models import TraineeAccount


#This is for Service Scheduler .
#Assign Service to trainees


#define one specific Service Instance such as Monday Break Prep, Monday Guard C, etc
#also includes all those designate services such as ap, piano, etc
class Instance(models.Model):

    """define one specific Service Instance such as Monday Break Prep, Monday Guard C, etc"""

    WEEKDAY = (
        ('Sun', 'Sunday'),
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
    )

    service = models.ForeignKey(Service)
    period = models.ForeignKey(Period)
    weekday = models.CharField(max_length=3, choices=WEEKDAY)
    startTime = models.TimeField('start time')
    endTime = models.TimeField('end time')

    #after doing a service especially guard service , a trainee should have rest time(recoveryTime) for next time.
    recoveryTime = models.IntegerField('time')

    #get instances by service period and service
    def getInstancesByService(self, period, service):
        return Instance.objects.filter(service=service, period=period)

    #get instances of service of current week ordered by time
    def getInstancesOrderByTime(self):
        #get the current service period according to current datetime
        _current_date = datetime.now().date()
        period = Period.objects.filter(endTime_gte=_current_date, startTime_lte=_current_date)
        return Instance.objects.filter(period=period).order_by("startTime")


#define Service group such as Monday Prep Brothers, etc
#From example, Monday Breakfast Prep includes Kitchen Star, Brother, Sister
class WorkerGroup(models.Model):

    name = models.CharField(max_length=200)
    instance = models.ForeignKey(Instance)
    numberOfWorkers = models.IntegerField()
    isActive = models.BooleanField()

    #Some service instance is not designated, but some service worker group might be designated such Kitchen Star.
    isDesignated = models.BooleanField()

    #return the the WorkerGroup of a certain Instance
    def getWorkerGroup(self, instance):
        return WorkerGroup.objects.filter(instance=instance)

    def getNonDesignateGroupOrderByTime(self):
        """return the None-Designation Worker Group Order By Time of current week"""
        _current_date = datetime.now().date()
        period = Period.objects.filter(endTime_gte=_current_date, startTime_lte=_current_date)
        return WorkerGroup.objects.filter(~Q(instance_service_category="Designated"), instance_period=period).\
            order_by("instance_startTime")


#Service qualification group such as sack lunch star,Kitchen Star, House Inspector, Shuttle Driver, Piano, Usher, etc
#This is a not permanent designation. For example, two brothers might be designated as AV brothers, but others brothers
#have the qualification to serve AV.
class QualificationGroup(models.Model):

    name = models.CharField(max_length=200)
    Trainee = models.ManyToManyField(TraineeAccount)

    workerGroup = models.ForeignKey(WorkerGroup)


#Service filter which is a SQL query
class FilterQuery(models.Model):

    name = models.CharField(max_length=200)
    filterQuery = models.TextField()
    service = models.ManyToManyField(Service)
    qualificationGroup = models.ManyToManyField(QualificationGroup)
    workerGroup = models.ManyToManyField(WorkerGroup)


#Service exceptions
class ExceptionGroup(models.Model):

    name = models.CharField(max_length=200)
    startDate = models.DateField('start time')
    endDate = models.DateField('end time')
    Trainee = models.ManyToManyField(TraineeAccount)
    service = models.ManyToManyField(Instance)


#Service Scheduler
class Scheduler(models.Model):

    period = models.ForeignKey(Period)
    startDate = models.DateField()
    modifiedTime = models.DateTimeField()
    #TODO Trainee = models.ForeignKey(Trainee)

    def RunScheduling(self):

        """Run the Service Scheduler"""

        workerGroup = WorkerGroup()

        #get the non designated worker groups of current week
        workerGroups = workerGroup.getNonDesignateGroupOrderByTime()

        #get user service assignment history, use a list of dicts to store the history
        #trainees[{TraineeId:13, workLoad:10, previousService: 1}, {}, {}]
        #this list is easy to sort the list of dict.

        #TO IMPROVE: If want to reduce the time, use another list of trainee_track to track whether the history of a certain trainee
        #since list is easy to search the index by value
        #is already in the list of history dict.if not then add new history to the history list dict another wise skip.

        #Or to use OrderDict: for example dict_previousSv{traineeID:svId,...}, dict_thisweekWork{traineeId, workLoad..}
        #it is easy to sort and search
        trainees = TraineeAccount.objects.all()

        historyList = list(trainees.count())
        for i in range(0, trainees.count()):
            historyList[i] = self.getWorkLoadHistory(trainees[i])

        #Enumerate the worker groups to assign the services to different trainees
        for group in workerGroups:
            #ToDO get the available trainees
            #ToDO get the trainees service history
            #ToDo order the trainees according to their previous history
            #ToDo order the trainees according to their current week history(total workload and recovery time)
            #ToDo consider other
            pass

    def getWorkLoadHistory(self, trainee):
        """Get the trainee's service assignment history"""
        pass

    def getMissedInstances(self):
        """return missed services of current scheduler"""
        return self.assignment_set.all()


#Service Assignment
class Assignment(models.Model):

    #TODO Trainee=models.ForeignKey(Trainee)
    scheduler = models.ForeignKey(Scheduler)
    workerGroup = models.ForeignKey(WorkerGroup)
    isAbsent = models.BooleanField()
    subTrainee = models.ForeignKey(TraineeAccount)


#permanent designation
class PermanentDesignation(models.Model):

    trainee = models.ManyToManyField(TraineeAccount)
    workerGroup = models.ManyToManyField(WorkerGroup)
    isActive = models.BooleanField()

    def getAssignmentByTrainee(self, trainee):
        return WorkerGroup.objects.filter(trainee=trainee)
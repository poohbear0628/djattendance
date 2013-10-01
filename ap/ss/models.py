from django.db import models
from service.models import *
from django.db.models import Q
from datetime import datetime
from operator import itemgetter
from collections import OrderedDict
from trainees.models import Trainee


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
	
	def getWorkerGroup(self):
        return self.workergroup_set.all()

	def __unicode__(self):
        return self.period.name + "  " + self.weekday + "  " +self.service.name

#define Service group such as Monday Prep Brothers, etc
#From example, Monday Breakfast Prep includes Kitchen Star, Brother, Sister
class WorkerGroup(models.Model):

			"""define worker groups of each service instance"""

    name = models.CharField(max_length=200)
    instance = models.ForeignKey(Instance,related_name="workergroups")
    numberOfWorkers = models.IntegerField()
    isActive = models.BooleanField()

	#Some service instance is not designated, but its service worker group might be designated such Kitchen Star.
    isDesignated = models.BooleanField(blank=True)

    #If it is Designated,  Many to Many relationship, one trainee might be designated to different worker group,
    # and one worker group might have different trainees. This is permanent designation.
    designatedTrainees = models.ManyToManyField(Trainee, related_name="workergroups")

      #return the set worker groups of a certain trainee
    def getDesignationByTrainee(self, trainee):
        """return the set of service worker groups of a certain trainee"""
        return self.workerGroup.objects.filter(designatedTrainees=trainee)

    #return trainees of a certain designation
    def getTrainees(self, workerGroup):
        """return trainees in this designation"""
        return self.designatedTrainees
		
	def __unicode__(self):
        return self.name


#Service exceptions, some trainees might be not available for a certain services because of certain reasons. For
# example, they are out of town,or they are sick.
class ExceptionRequest(models.Model):

    #the name of that exception, or the name of that exception.
    name = models.CharField(max_length=200)

    startDate = models.DateField('start time')

    endDate = models.DateField('end time')

    reason = models.TextField()

    isApproved = models.BooleanField()

    traineeAssistant = models.ForeignKey(TrainingAssistant, related_name="exceptionrequest")
    trainees = models.ManyToManyField(Trainee, related_name="exceptionrequest")
    instances = models.ManyToManyField(Instance, related_name="exceptionrequest")

    def __unicode__(self):
        return self.name
	
	
#Service filter which is a SQL query
class FilterQuery(models.Model):

    name = models.CharField(max_length=200)
    filterQuery = models.TextField()
    services = models.ManyToManyField(Service,related_name="filters")
    workerGroups = models.ManyToManyField(WorkerGroup,related_name="filters")

    def __unicode__(self):
        return self.name
	
	
	
	def getFiltersByService(self, service):
        """return the filterQuery of a service"""
        return FilterQuery.filter(service=service)

    def getFiltersByWorkerGroups(self, workerGroup):
        """return the filterQuery of a workerGroup"""
        return FilterQuery.filter(workerGroup=workerGroup)
		
#Service Scheduler
class Scheduler(models.Model):

    period = models.ForeignKey(Period)
    startDate = models.DateField()
    modifiedTime = models.DateTimeField()
	
	#this is to record the attendance brothers
    trainee = models.ForeignKey(Trainee)

    def RunScheduling(self):

        """Run the Service Scheduler"""

        workerGroup = WorkerGroup()

        #get the non designated worker groups of current week
        #TO IMPROVE: order the workerGroup later by the ratio of
        #           the number of available trainees and the number of the needed trainees.
        workerGroups = workerGroup.getNonDesignateGroupOrderByTime()

        #get user service assignment history, use a list of dicts to store the history
        #trainees[{TraineeId:13, workLoad:10, previousService: 1}, {}, {}]
        #this list is easy to sort the list of dict.

        #TO IMPROVE: If want to reduce the time, use another list of trainee_track to track whether the history of
        #  a certain trainee since list is easy to search the index by value
        #is already in the list of history dict.if not then add new history to the history list dict another wise skip.

        #Or to use OrderDict: for example dict_previousSv{traineeID:svId,...}, dict_thisweekWork{traineeId, workLoad..}
        #it is easy to sort and search
        trainees = TraineeAccount.objects.all()

        historyList = list(trainees.count())
        for i in range(0, trainees.count()):
            historyList[i] = self.getWorkLoadHistory(trainees[i])

        #Enumerate the worker groups to count the available number of trainees of each workerGroups
        for group in workerGroups:
            trainees = self.getAvailableTrainees(group)
            #TODO sort workerGroups according the the number of available trainees

        listAssignment = dict(workerGroups.count())

        #Enumerate the worker groups to assign the services
        for i in range(workerGroups.count()):
            group = workerGroups[i]
            trainee = self.getBestCandidate(trainees, group)
            #ToDo assign the trainee

            assignment = Assignment()
            assignment.scheduler = self
            assignment.workerGroup = group
            assignment.trainee = trainee
            listAssignment[trainee] = assignment

    def getWorkLoadHistory(self, trainee):
        """Get the trainee's service assignment history"""
        pass

    def getAvailableTrainees(self, workerGroup):
        """get the available trainee list of workerGroup"""
        pass

    def checkConflict(self, trainee, workerGroups):
        """check the whether the trainee has the schedule conflict with his current service"""
        pass

    def getBestCandidate(self, trainees, group):
        pass

    def getMissedInstances(self):
        """return missed services of current scheduler"""
        return self.assignment_set.filter(isAbsent=1)

        #get instances by service period and service
    def getInstancesByService(self, period, service):
        return Instance.objects.filter(service=service, period=period)

    #get instances of service of current week ordered by time
    def getInstancesOrderByTime(self):
        """get the current service period according to current datetime"""

        #get the current date and get the current period
        _current_date = datetime.now().date()
        period = Period.objects.get(endDate__gte=_current_date, startDate__lte=_current_date)

        #return the QuerySet of instances of this period ordered by start time
        return Instance.objects.filter(period=period).order_by("startTime")

    #return the the WorkerGroup of a certain Instance
    def getWorkerGroup(self, instance):
        return WorkerGroup.objects.filter(instance=instance)

     #Get the time ordered worker group of current week.
    def getNonDesignateGroupOrderByTime(self):
        """return the None-Designation Worker Group Order By Time of current week"""

        #get the current date and get the current period
        _current_date = datetime.now().date()
        period = Period.objects.get(endDate__gte=_current_date, startDate__lte=_current_date)

        #get the QuerySet of WorkerGroup of non-designated services of current period,
        #ordered by instance startTime
        return WorkerGroup.objects.select_related().filter(~Q(instance__service__category__name="Designated"),
                                                           instance__period=period).order_by("instance__startTime")
    #---------------------------------------------------------------------------------------------------#
    #following functions are for testing and debugging
    def test(self):
        pass

    def importWorkerGroup(self):
        #delete unused workergroup
        """wgs = workerGroup_test.objects.all().order_by('period', 'service')
        for wg in wgs:
            ins = Instance.objects.filter(period=wg.period, service=wg.service)
            if ins.count() > 0:
                wg.instance = ins[0]
               # wg.save()
            else:
                wg.delete()
                print wg.service.name + "   " + wg.period.name

        #import workerGroup
        wgs = workerGroup_test.objects.all()
        for wg in wgs:
            wg_tmp = WorkerGroup()
            wg_tmp.id = wg.id
            wg_tmp.numberOfWorkers = wg.numberOfWorkers
            wg_tmp.name = wg.name
            wg_tmp.instance = wg.instance
            wg_tmp.isDesignated = wg.isDesignated
            wg_tmp.isActive = wg.isActive
            wg_tmp.save()"""

    #pring the worker groups by service instances
    def printWorkerGroups(self):
        cgs = Category.objects.all()
        for cg in cgs:
            print cg.name
            svs = cg.getServices()
            for sv in svs:
                print "   " + sv.name
                pds = Period.objects.filter(services=sv)
                for pd in pds:
                    print "     " + pd.name
                    ins = Instance.objects.filter(period=pd, service=sv)
                    if ins.count() > 0:
                        print "         " + "StarTime:" + str(ins[0].startTime) +\
                              "EndTime:" + str(ins[0].endTime)
                        wgs = ins[0].getWorkerGroup()
                        for wg in wgs:
                            print wg.name
                    else:
                        print "         None"

    def printService(self):
        cgs = Category.objects.all()
        for cg in cgs:
            print cg.name
            svs = cg.getServices()
            for sv in svs:
                print "   " + sv.name
                pds = Period.objects.filter(service=sv)
                for pd in pds:
                    print "     " + pd.name
                    ins = Instance.objects.filter(period=pd, service=sv)
                    if ins.count() > 0:
                        print "         " + "StarTime:" + str(ins[0].startTime) +\
                              "EndTime:" + str(ins[0].endTime)")
                    else:
                        print "         None"


#Service Assignment
class Assignment(models.Model):

    trainee = models.ForeignKey(TraineeAccount, related_name="assignment")
    scheduler = models.ForeignKey(Scheduler)
    workerGroup = models.ForeignKey(WorkerGroup)
    isAbsent = models.BooleanField()
    subTrainee = models.ForeignKey(TraineeAccount, related_name="assignment_sub")

    #return the service assignment of a certain trainee, scheduler
    def getAssignmentsByTrainee(self, trainee, scheduler):
        """return all the set of service instances of a trainee"""
        return Assignment.objects.filter(trainee=trainee, scheduler=scheduler)
       #return Assignment.workerGroup.filter()...
		







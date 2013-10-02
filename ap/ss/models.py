"""
This is to define Service Scheduler, which is to assign the services to trainees.
"""
from django.db import models
from services.models import *
from django.db.models import Q
from datetime import datetime
from operator import itemgetter
from collections import OrderedDict
from accounts.models import Trainee
from django.db.models import Sum
from django.db.models import Max

#define one specific Service Instance such as Monday Break Prep, Monday Guard C, etc
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

    service = models.ForeignKey(Service,related_name="instances")
    period = models.ForeignKey(Period,related_name="instances")
    weekday = models.CharField(max_length=3, choices=WEEKDAY)
    startTime = models.TimeField('start time', null=True)
    endTime = models.TimeField('end time', null=True)

    #after doing a service especially guard service , a trainee should have rest time(recoveryTime) for next time.
    recoveryTime = models.IntegerField('time')

    def __unicode__(self):
        return self.period.name + "  " + self.weekday + "  " +self.service.names

#define Service group such as Monday Prep Brothers, etc
#From example, Monday Breakfast Prep includes Kitchen Star, Brother, Sister
class WorkerGroup(models.Model):
    
    """define worker groups of each service instance"""

    name = models.CharField(max_length=200)
    instance = models.ForeignKey(Instance,related_name="workergroups")
    numberOfWorkers = models.IntegerField()
    minNumberOfWorkers = models.IntegerField()
    isActive = models.BooleanField()

    #Some service instance is not designated, but its service worker group might be designated such Kitchen Star.
    isDesignated = models.BooleanField(blank=True)

    #If it is Designated,  Many to Many relationship, one trainee might be designated to different worker group,
    # and one worker group might have different trainees. This is permanent designation.
    designatedTrainees = models.ManyToManyField(Trainee, related_name="workergroups")

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
    traineeAssistant = models.ForeignKey(TrainingAssistant, related_name="exceptionrequests")
    trainees = models.ManyToManyField(Trainee, related_name="exceptionrequests")
    instances = models.ManyToManyField(Instance, related_name="exceptionrequests")

    def __unicode__(self):
        return self.name

#Service filter which is a SQL query
class Filters(models.Model):

    name = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    services = models.ManyToManyField(Service,related_name="filters")
    workerGroups = models.ManyToManyField(WorkerGroup,related_name="filters")

    def __unicode__(self):
        return self.name

#Service Scheduler
class Scheduler(models.Model):
    """This is Scheduler class which will the class to run the service scheduling algorithm"""

    period = models.ForeignKey(Period)
    startDate = models.DateField()
    modifiedTime = models.DateTimeField()

    #this is to record the attendance brothers
    trainee_attendance = models.ForeignKey(Trainee)

    def RunScheduling(self):
        """Run the Service Scheduler, and store the assignment in the database"""

        #get the non designated worker groups of current week
        #TO IMPROVE: order the workerGroup later by the ratio of
        #the number of available trainees and the number of the needed trainees.
        workerGroups = self.getNonDesignateGroupOrderByTime()

        #Method ONE: get user service assignment history, use a list of dicts to store the history
        #trainees[{TraineeId:13, workLoad:10, previousService: 1}, {}, {}]
        #It is very easy to order the list.
        #But if we use this, it is not easy to update a certain trainee's update data. Every time we get a list of
        # available trainees, we have to re-build all the dada. One way to rebuild is to store all the data separately
        # in lists or dicts Then when we rebuild the trainees, we don't have to fetch from the database.

        #Method TWO use OrderDict:
        # for example dict_previousSv{traineeID:svId,...}, dict_thisWeekWork{traineeId:workLoad ..}
        #It is easy to sort and search, but it is hard to sort according to many parameter.
		
		#Method THREE we use the simplest way: trainees[], pre_sv[trainee.count()], tot_hour[], week_hour[],etc
        #this is the most efficient in performance. But have to implement the sorting by ourselves.

        #We use Method One:
        #Use the following variables to update and fetch the history date in a fast way
        trainees = Trainee.objects.all()

        #service non-related work history
        pre_assignment = dict()
        tot_workload = dict()

        #service related history
        same_sv_counts = dict()
        pre_same_sv_date = dict()

        #assignment of current related history
        week_workload = dict()

        #Get the service non related work history: pre_assignment and tot_workload
        for trainee in trainees:
            assignment = Assignment()
            pre_assignment[trainee.id] = assignment.getTotalWorkLoadByTrainee(trainee)
            tot_workload[trainee.id] = assignment.getPreAssignment(trainee)

        traineesWG=list()
        #Enumerate the worker groups to count the available number #of trainees of each workerGroups to decide the order of #workergroups
        for i in range(workerGroups.count()):
            group = workerGroups[i]
            availableTrainees = self.getAvailableTrainees(group)
            traineesWG.append(availableTrainees)
            #TODO sort workerGroups according the the number of available trainees

        #Enumerate the worker groups to assign the services
        listAssignment = list()
        for i in range(workerGroups.count()):
            group = workerGroups[i]
            bestCandidates = self.getBestCandidates(traineesWG[i], self,group, pre_assignment,
                                                   tot_workload,week_workload,
                                                   same_sv_counts,pre_same_sv_date)

            for candidate in bestCandidates:
                assignment = Assignment()
                assignment.scheduler = self
                assignment.workerGroup = group
                assignment.trainee = candidate["traineeId"]
                assignment.save()
                listAssignment.append(assignment)

    #get the list of available trainees
    @staticmethod
    def getAvailableTrainees(workerGroup):
        """get the available trainee list of workerGroup"""

        instance = workerGroup.instance
        service = instance.service

        if service.needQualification:
            trainees = service.qualifiedTrainees
        else:
            trainees = Trainee.objects.all()

        filter_sv = service.filters.all()
        filter_wg = workerGroup.filters.all()

        filters_tot = {}
        for filt in filter_sv:
            filters_tot[str(filt.keyword)]=str(filt.value)

        for filt in filter_wg:
            filters_tot[str(filt.keyword)]=str(filt.value)

        trainees = trainees.filter(**filters_tot)
        print trainees.count()

        trainees = trainees.filter(~Q(exceptionrequests__instances=instance))
        print trainees.count()
        return trainees

    #get the best candidates from available trainees for current group
    @staticmethod
    def getBestCandidates(trainees,scheduler, workergroup,pre_sv,tot_workload,week_workload,
                                                   sv_counts,prev_sv_date):
        """Get the list of best candidates of a certain group"""
        bestCandidates = list()
        candidate = {}
        assignment = Assignment()

        for trainee in trainees:
            sv_counts[trainee.id] = assignment.getPreAssignmentCountsByServices(trainee,workergroup.instance.service)

            #build the candidate{}, and bestCandidates[{},{},{}]
            candidate["traineeId"] = trainee.id
            candidate["tot_workload"] = tot_workload[trainee.id]
            candidate["week_workload"] = week_workload[trainee.id]
            candidate["sv_counts"] = sv_counts[trainee.id]
            candidate["prev_sv_date"] = prev_sv_date[trainee.id]
            candidate["pre_sv"] = pre_sv[trainee.id]
            bestCandidates.append(candidate)
            #TODO build the dict lists and sort and choose the best one

        count_asssigned = assignment.getAssignmentNumByWorkerGroup(workergroup,scheduler)
        return bestCandidates

    #get the missed services of current scheduler
    def getMissedAssignment(self):
        """return missed services of current scheduler"""
        return self.assignments.filter(isAbsent=1)

    #get instances by service period and service
    @staticmethod
    def getInstancesByService(period, service):
        """Get the QuerySet of instances by service"""
        return Instance.objects.filter(service=service, period=period)

    #get instances of service of current week ordered by time
    @staticmethod
    def getInstancesOrderByTime():
        """get the current service period according to current datetime"""

        #get the current date and get the current period
        _current_date = datetime.now().date()
        period = Period.objects.get(endDate__gte=_current_date, startDate__lte=_current_date)

        #return the QuerySet of instances of this period ordered by start time
        return Instance.objects.filter(period=period).order_by("startTime")

    #Get the time ordered worker group of current week
    @staticmethod
    def getNonDesignateGroupOrderByTime():
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
            #print getNonDesignateGroupOrderByTime()
        #self.printService()
        #self.printWorkerGroups()
        #inst = Instance.objects.get(id=1)
        #ers = inst.exceptionrequests.all()
        #ers = ExceptionRequest.objects.filter(instances=inst)
        #ers = ExceptionRequest.objects.all()
        #print ers
        #print ers[0]
        #print ers[1]
        #for er in ers:
            #print er
        self.RunScheduling()

    #pring the worker groups by service instances
    @staticmethod
    def printWorkerGroups():
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

    #print the services as following format
    # Category A
    #    Service A
    #       Period A
    #            Instance1: Details
    #            Instance2:...
    #        Period B
    #   Service B
    @staticmethod
    def printService():
        cgs = Category.objects.all()
        for cg in cgs:
            print cg.name
            svs = cg.getServices()
            for sv in svs:
                print "SV   " + sv.name
                pds = Period.objects.filter(services=sv)
                for pd in pds:
                    print "     " + pd.name
                    ins = Instance.objects.filter(period=pd, service=sv)
                    if ins.count() > 0:
                        print "         " + "StarTime:" + str(ins[0].startTime) +\
                              "EndTime:" + str(ins[0].endTime)
                    else:
                        print "         None"


#Service Assignment to record the scheduling solution
class Assignment(models.Model):
    """Service Assignment"""

    trainee = models.ForeignKey(Trainee, related_name="assignments")
    scheduler = models.ForeignKey(Scheduler,related_name="assignments")
    workerGroup = models.ForeignKey(WorkerGroup,related_name="assignments")
    isAbsent = models.BooleanField()
    assignmentDate = models.DateField('assignment Date')

    #For assignment, if the assigned trainee is absent, there can be a substitution
    subTrainee = models.ForeignKey(Trainee, related_name="assignments_sub")

    def getTotalWorkLoadByTrainee(self,trainee):
        """return the total workload of a trainee assigned already this term"""
        return self.objects.filter(trainee=trainee,isAbsent=1).aggregate(Sum(
            'workerGroup__instance__service__workLoad'))

    def getPreAssignmentCountsByServices(self,trainee,service):
        """return the times of a trainee already assigned of a service"""
        return self.objects.filter(trainee=trainee,isAbsen=1,workerGroup__instance__service=service).count()

    def getPreAssignmentDateByService(self,trainee,service):
        """return the last time the trainee was assigned to this service"""
        return self.objects.filter(trainee=trainee,isAbsent=1,workerGroup__instance__service=service).latest(
            "assignmentDate")

    def getPreAssignment(self,trainee):
        """return the last service instance"""
        return self.objects.filter(trainee=trainee).latest("assignmentDate")

    #return the service assignment of a certain trainee, scheduler
    def getAssignmentsByTrainee(self, trainee, scheduler):
        """return all the set of service instances of a trainee"""
        return self.objects.filter(trainee=trainee, scheduler=scheduler)

    #check whether a workergroup is already assigned.
    def checkAssignment(self,scheduler,workergroup):
        """return True if the WorkerGroup is already assigned"""
        num = self.objects.filter(scheduler=scheduler,workergroup=workergroup).count()
        if num<workergroup.numberOfWorkers:
            return 0
        else:
            return 1

    def checkAssignmentMinimum(self,scheduler,workergroup):
        """return True if the workergroup minimum requirement is fulfilled"""
        num = self.objects.filter(scheduler=scheduler,workergroup=workergroup).count()
        if num<workergroup.minNumberOfWorkers:
            return 0
        else:
            return 1

    def getAssignmentNumByWorkerGroup(self,scheduler,workergroup):
        """return the number of assignment to a workergroup"""
        return self.objects.filter(scheduler=scheduler,workergroup=workergroup).count()
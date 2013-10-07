"""
This is to define Service Scheduler, which is to assign the services to trainees for each week
"""
from django.db import models
from services.models import *
from django.db.models import Q
from datetime import datetime
from operator import itemgetter
from collections import OrderedDict
from accounts.models import Trainee,TrainingAssistant
from django.db.models import Sum,Max,Count
from services.models import Service

#Define one specific Service Instance such as Monday Break Prep, Monday Guard C, etc
class Instance(models.Model):
    """Define one specific Service Instance such as Monday Break Prep, Monday Guard C, etc"""

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

    # The time the trainee needed to rest after doing a specific service.
    recoveryTime = models.IntegerField('time')

    #Get instances by service period and service
    @staticmethod
    def getInstancesByService(period, service):
        """Get the QuerySet of instances by service"""
        return Instance.objects.filter(service=service, period=period)

    #Get all the instances of current week ordered by time
    @staticmethod
    def getInstancesCurrentWeek():
        """Get the current service period according to current datetime"""

        #Get the current date and get the current period
        _current_date = datetime.now().date()
        period = Period.objects.get(endDate__gte=_current_date, startDate__lte=_current_date)

        #Return the QuerySet of instances of this period ordered by start time
        return Instance.objects.filter(period=period).order_by("startTime")

    #Get the schedule conflicted instances of a certain instance
    @staticmethod
    def getConflictInstances(instance):
        """Get the instances which have time conflict with a certain instance"""
        return  Instance.objects.filter(weekday=instance.weekday,endTime__gte=instance.startTime)

    def __unicode__(self):
        return self.period.name + "  " + self.weekday + "  " +self.service.name

#Define Service group such as Monday Prep Brothers, etc
#From example,Monday Breakfast Prep includes Kitchen Star, Brothers, Sisters.
class WorkerGroup(models.Model):
    """Define the worker groups of each service instance"""

    name = models.CharField(max_length=200)
    instance = models.ForeignKey(Instance,related_name="workergroups")
    numberOfWorkers = models.IntegerField()

    # The minimum number of trainees required for the group.
    minNumberOfWorkers = models.IntegerField(blank=True)
    isActive = models.BooleanField()

    # Whether the worker group is designated or not.
    # Note:Some service instance is not designated,
    # but its service worker group might be designated.
    isDesignated = models.BooleanField(blank=True)

    # If it is Designated,  Many to Many relationship, one trainee might be designated to different worker groups,
    # and one worker group might have different trainees..
    designatedTrainees = models.ManyToManyField(Trainee, related_name="workergroups")

    #Get all the worker groups of current week ordered by time
    @staticmethod
    def getNonDesignateGroupOrderByNumOfWorkers():
        """return the None-Designation Worker Group Order By Time of current week"""

        #Get the current date and get the current period
        _current_date = datetime.now().date()
        period = Period.objects.get(endDate__gte=_current_date, startDate__lte=_current_date)

        #Get the QuerySet of WorkerGroup of non-designated services of current period,
        #ordered by instance startTime
        return WorkerGroup.objects.select_related().filter(~Q(instance__service__category__name="Designated"),
                                                           isActive=1,instance__period=period,isDesignated=0,
                                                           instance__service__isActive=1).order_by("numberOfWorkers")

    #Total workload of non designated services of a trainee throughout the entire term.
    @staticmethod
    def workLoad(trainee):
        """return the workload of non designated services a trainee's designation of this term"""
        pass
	
    #Check the conflict with the designated service.
	#Note: To reduce the possibility of conflicts, add designated related conflict services to exceptions.
    @staticmethod
    def checkConflict(workergroup,trainee):
        """return true if the assigned workergroup has time conflict with the current assignment"""
        return WorkerGroup.objects.filter(isDesignated=1, designatedTrainees=trainee,instance__endTime__gte=workergroup
        .instance.startTime).count()

    def __unicode__(self):
        return self.instance.period.name+"  "+self.instance.service.name+"  "+self.name

# Service Instance Exceptions.
# Some trainees might be not available for certain services because of certain reasons.
class ExceptionRequest(models.Model):
    """Define Service Instance Exceptions"""

    #The title of that exception, or the title of that exception request
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

# Define service filter to build the dynamic django query parameter
class Filters(models.Model):
    """Define service filter to build the dynamic django query parameter"""
    name = models.CharField(max_length=200)

    #django query keyword
    keyword = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

    services = models.ManyToManyField(Service,related_name="filters")
    workerGroups = models.ManyToManyField(WorkerGroup,related_name="filters")

    def __unicode__(self):
        return self.name

# Define Service Scheduler
class Scheduler(models.Model):
    """This is Scheduler class to run the service scheduling algorithm"""

    period = models.ForeignKey(Period)
    startDate = models.DateField()
    modifiedTime = models.DateTimeField()

    # The attendance trainee who created one instance of scheduler for a certain week
    trainee_attendance = models.ForeignKey(Trainee)

    # Main algorithm to schedule all the worker groups
    def RunScheduling(self):
        """Run the Service Scheduler, and store the assignment in the database
        @rtype : null
        """

        # Parameter to indicate that the algorithm just need to assign the minimum number to each worker group
        MIN_REQUIREMENT = 1

        # Get the non designated worker groups of current week
        # TODO Further improvement: order the workerGroup by the ratio of the number of available trainees and the
        # TODO number of the needed trainees.
        workerGroups = WorkerGroup.getNonDesignateGroupOrderByNumOfWorkers()
        print "Total worker groups:" +str(workerGroups.count())

        trainees = Trainee.objects.filter(active=1)
        print "Total trainees:"+ str(trainees.count())

        #--------------------------------------Notes--------------------------------------------------#
        # Method ONE: get user service assignment history, use a list of dicts to store the history
        # trainees[{TraineeId:13, workLoad:10, previousService: 1}, {}, {}]
        # It is very easy to order the list.
        # But if we use this, it is not easy to update a certain trainee's update data. Every time we get a list of
        # available trainees, we have to re-build all the dada. One way to rebuild is to store all the data separately
        # in lists or dicts Then when we rebuild the trainees, we don't have to fetch from the database.

        # Method TWO use OrderDict:
        # for example dict_previousSv{traineeID:svId,...}, dict_thisWeekWork{traineeId:workLoad ..}
        # It is easy to sort and search, but it is hard to sort according to many parameter.
		
		# Method THREE we use the simplest way: trainees[], pre_sv[trainee.count()], tot_hour[], week_hour[],etc
        # this is the most efficient in performance. But have to implement the sorting by ourselves.

        # We use Method One:
        # Use the following variables to update and fetch the history date in a fast way
        #--------------------------------------------------------------------------------------------#

        # Service non-related assignment history: the previous assignment
        pre_assignment = dict()
        # Service non-related assignment history: the total workload
        tot_workload = dict()

        # Service related assignment history: the counts of the same service assigned in past weeks
        same_sv_counts = dict()
        # Service related assignment history: the date of the previous same service assigned in past weeks
        pre_same_sv_date = dict()

        #assignment of current related history including designated assignment
        #TODO concerning the designated assignment history, we can set an initial week load for each trainee
        week_workload = dict()

        #init the history variables
        for trainee in trainees:
            pre_assignment[trainee.id]=0
            tot_workload[trainee.id]=0
            same_sv_counts[trainee.id]=0
            pre_same_sv_date[trainee.id]=0
            week_workload[trainee.id]=0

        #Get the service non-related work history: pre_assignment and tot_workload
        print "Getting assignment history: total workload and previous assignment...."
        for trainee in trainees:
            tot_workload[trainee.id] = Assignment.getTotalWorkLoadByTrainee(trainee)
            pre_assignment[trainee.id] = Assignment.getPreAssignment(trainee)

        print "Non-Designated Worker Groups: " + str(workerGroups.count())


        #Get the same_sv_counts in a quick way
        services = Service.objects.filter(isActive=1)
        for sv in services:
            Assignment.objects.filter(absent=0,workergroup__instance__service=sv).aggregate(Count('trainee'))

        for trainee in trainees:
            print trainee
            for sv in services:
                #This query is very slow. If you use Assignment.objects.all(), it will be super fast.
                #Try raw sql, it might be very fast.
                pre_same_sv_date[trainee.id] = Assignment.getPreAssignmentDateByService(trainee,sv)

        print "Getting the available trainees for each worker group"
        #List of QuerySets to store the available trainees for each worker group
        trainees_wgs=list()

        # Enumerate the worker groups to count the available number of trainees of each workerGroups
        # Sorting according to the ration of the number of available trainees and the number needed for each

        #Exclude the workergroup if its numberOfWorkers is zero.
        workerGroups = workerGroups.filter(~Q(minNumberOfWorkers=0))
        for i in range(workerGroups.count()):
            group = workerGroups[i]
            availableTrainees = self.getAvailableTrainees(group)

            #use a dict to store trainees, workergroup and the ration
            trainee_wg = dict()
            trainee_wg['trainees'] = availableTrainees
            trainee_wg['workergroup'] = group
            if MIN_REQUIREMENT:
                trainee_wg['ratio'] = availableTrainees.count()/group.minNumberOfWorkers
            else:
                trainee_wg['ratio'] = availableTrainees.count()/group.numberOfWorkers

            # A list of dicts for sorting
            trainees_wgs.append(trainee_wg)
            trainees_wgs.sort(key=itemgetter('ratio'),reverse=False)

        # Enumerate the worker groups to assign the services
        listAssignment = list()
        for item in trainees_wgs:
            trainees_wg = item['trainees']
            group = item['workergroup']

            print "Assigning for group:"+str(group)+" Available Trainees:"+str(trainees_wg.count())

            # Get the best candidates for the worker group
            bestCandidates = self.getBestCandidates(trainees_wg, self,group, pre_assignment,
                                                   tot_workload,week_workload,
                                                   same_sv_counts,pre_same_sv_date,MIN_REQUIREMENT)

            print "Assigning "+ str(len(bestCandidates))+" Candidates"+ \
                  "of "+ str(group.minNumberOfWorkers)+ " requirement of this group"

            #print bestCandidates

            # Store the assignment in the database and update the related variables
            for candidate in bestCandidates:
                assignment = Assignment()
                assignment.scheduler = self
                assignment.workerGroup = group
                #assignment.trainee = Trainee.objects.get(id=candidate["traineeId"])
                week_workload[candidate["traineeId"]]+=assignment.workerGroup.instance.service.workload
                #assignment.save()
                listAssignment.append(assignment)

    # Schedule for one worker group
    def RunSchedulingByGroup(self,workergroup):
        """Run a schedule for one specific workergroup"""
        pass

    # Get the list of available trainees
    @staticmethod
    def getAvailableTrainees(workerGroup):
        """Get the available trainee list of workerGroup"""

        instance = workerGroup.instance
        service = instance.service

        #TODO If we want to improve the speed ,we can store the service,instance related trainees in memory.
        #Step 1: filter according to the qualification
        if service.needQualification:
            trainees = service.qualifiedTrainees
        else:
            trainees = Trainee.objects.all()

        #Step 2: Filter trainees according to the filters
        filter_sv = service.filters.all()
        filter_wg = workerGroup.filters.all()

        #creating dynamic filt parameter for filter()
        filters_tot = {}
        for filt in filter_sv:
            filters_tot[str(filt.keyword)]=str(filt.value)
        for filt in filter_wg:
            filters_tot[str(filt.keyword)]=str(filt.value)

        trainees = trainees.filter(**filters_tot)

        #Step 3: Further filter according to the exception
        trainees = trainees.filter(~Q(exceptionrequests__instances=instance))

        #print trainees.count()
        return trainees

    #get the best candidates from available trainees for current group
    @staticmethod
    def getBestCandidates(trainees,scheduler,workergroup,pre_assignment,
                                                   tot_workload,week_workload,
                                                   same_sv_counts,pre_same_sv_date,MIN_REQUIREMENT):
        """Get the list of best candidates of a certain group"""

        #List of dicts to store all the information needed for sorting
        bestCandidates = list()
        service = workergroup.instance.service
        for trainee in trainees:

            same_sv_counts[trainee.id] = Assignment.getPreAssignmentCountsByServices(trainee,service)
            pre_same_sv_date[trainee.id] = Assignment.getPreAssignmentDateByService(trainee,service)
            #TODO It is too slow. To improvement, each trainee can have a dict to track the result,
            #TODO If ti is already have, then no need to query the db
            #TODO Trainee_sv_count{t_id : {sv_id: cont}}
            #TODO or consider using raw SQL

            #build the candidate{}, and bestCandidates[{},{},{}]
            candidate = dict()
            candidate["traineeId"] = trainee.id
            candidate["tot_workload"] = tot_workload[trainee.id]
            candidate["pre_assignment"] = pre_assignment[trainee.id]
            candidate["week_workload"] = week_workload[trainee.id]

            candidate["same_sv_counts"] = same_sv_counts[trainee.id]
            candidate["prev_same_sv_date"] = pre_same_sv_date[trainee.id]

            bestCandidates.append(candidate)

        #TODO sort bestCandidates and choose the best one
        bestCandidates.sort(key=itemgetter('tot_workload','week_workload','same_sv_counts'),reverse=False)

        count_assigned = Assignment.getAssignmentNumByWorkerGroup(workergroup,scheduler)

        #checkConflict is time consuming, therefore not check for all the available trainees.
        num=0
        for candidate in bestCandidates:
            if MIN_REQUIREMENT:
                if num >= workergroup.minNumberOfWorkers-count_assigned:
                    return bestCandidates[0:num]
            else:
                if num >= workergroup.numberOfWorkers-count_assigned:
                    return bestCandidates[0:num]

            #check conflict. if there is conflict, remove the candidate from the bestCandidates
            if Assignment.checkConflict(scheduler,workergroup,candidate["traineeId"]):
                bestCandidates.remove(candidate)
            else:
                num+=1

        #TODO if num is < workergroup.minNumberofWorker-count_assigned, need to free some one from other services.

        return bestCandidates[0:num]

    #---------------------------------------------------------------------------------------------------#
    #following functions are for testing and debugging
    def test(self):
        #self.printService()
        #self.analyseAssignment()
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
        #cgs = Category.objects.all()
        cgs = Category.objects.filter(~Q(name="Designated"))
        for cg in cgs:
            print cg.name
            svs = Service.objects.filter(category=cg,isActive=1)
            for sv in svs:
                print "   " + sv.name
                pds = Period.objects.filter(services=sv,name='FTTA')
                for pd in pds:
                    print "     " + pd.name
                    ins = Instance.objects.filter(period=pd, service=sv)
                    if ins.count() > 0:
                        print "         " + "StarTime:" + str(ins[0].startTime) +\
                              "EndTime:" + str(ins[0].endTime)
                        wgs = ins[0].workergroups.filter(isActive=1, isDesignated=0)
                        for wg in wgs:
                            print ":             "+str(wg.id)+" "+ wg.name
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

    # Analyse the result of assignment solution
    @staticmethod
    def analyseAssignment():

        trainees = Trainee.objects.all()
        cnt_trainees = trainees.count()

        tot_workload = []
        avg_workload = []
        avg_week_workload = []
        max_week_workload = []
        min_week_workload = []

        max_tot_workload = 0
        min_tot_workload = 0

        print cnt_trainees

        print tot_workload
        print avg_workload
        print avg_week_workload
        print max_week_workload
        print min_week_workload
        print max_tot_workload
        print min_tot_workload

        pass

# Service Assignment to record the scheduling solution.
class Assignment(models.Model):
    """Service Assignment"""

    # TODO consider: should we store the designated service assignments into the assignments table? It might be better
    # TODO to store them for attendance purpose.

    trainee = models.ForeignKey(Trainee, related_name="assignments")
    scheduler = models.ForeignKey(Scheduler,related_name="assignments")
    workergroup = models.ForeignKey(WorkerGroup,related_name="assignments")
    absent = models.BooleanField()
    assignment_date = models.DateField('assignment_date')

    #The substitution for that service
    subTrainee = models.ForeignKey(Trainee, related_name="assignments_sub", null=True)

    @staticmethod
    def getTotalWorkLoadByTrainee(trainee):
        """return the total workload of a trainee assigned already this term"""
        return Assignment.objects.filter(trainee=trainee,absent=0).aggregate(Sum(
            'workergroup__instance__service__workload'))[ 'workergroup__instance__service__workload__sum']

    @staticmethod
    def getPreAssignmentCountsByServices(trainee,service):
        """return the times of a trainee already assigned of a service"""
        sql = "select count(a.id) from ss_assignment as a, ss_workergroup as wg,ss_instance as inst,services_service " \
              "as sv where a.workergroup_id=wg.id and wg.instance_id=inst.id and inst.service_id=sv.id and sv.id=" \
        + str(service.id)+" and a.trainee_id="+str(str(trainee.id))
        return Assignment.objects.raw(sql)
        #return Assignment.objects.filter(trainee=trainee,absent=0,workergroup__instance__service=service).count()

    @staticmethod
    def getPreAssignmentDateByService(trainee,service):
        """return the last time the trainee was assigned to this service"""
        sql = "select a.* from ss_assignment as a, ss_workergroup as wg,ss_instance as inst,services_service " \
              "as sv where a.workergroup_id=wg.id and wg.instance_id=inst.id and inst.service_id=sv.id and sv.id=" \
        + str(service.id)+" and a.trainee_id="+str(str(trainee.id))+" order by a.assignment_date"
        return Assignment.objects.raw(sql)
        #return Assignment.objects.filter(trainee=trainee,absent=0,workergroup__instance__service=service).order_by(
        #    "assignment_date")

    #return the previous assignment of a trainee did.
    @staticmethod
    def getPreAssignment(trainee):
        """return the last service instance"""
        return Assignment.objects.filter(trainee=trainee,absent=0).order_by("assignment_date")[:1]

    #return the service assignment of a certain trainee, scheduler
    @staticmethod
    def getAssignmentsByTrainee(trainee, scheduler):
        """return all the set of service instances of a trainee"""
        return Assignment.objects.filter(trainee=trainee, scheduler=scheduler)

    #check whether the workers are assigned to the workergroup
    @staticmethod
    def checkAssignment(scheduler,workergroup):
        """return True if the WorkerGroup is already assigned"""
        num = Assignment.objects.filter(scheduler=scheduler,workergroup=workergroup).count()
        if num<workergroup.numberOfWorkers:
            return 0
        else:
            return 1

    #check whether the min number of workers are assigned to the workergroup
    @staticmethod
    def checkAssignmentMinimum(scheduler,workergroup):
        """return True if the workergroup minimum requirement is fulfilled"""
        num = Assignment.objects.filter(scheduler=scheduler,workergroup=workergroup).count()
        if num<workergroup.minNumberOfWorkers:
            return 0
        else:
            return 1

    #get the number of assignments of a certain workergroup
    @staticmethod
    def getAssignmentNumByWorkerGroup(scheduler,workergroup):
        """return the number of assignment to a workergroup"""
        return Assignment.objects.filter(scheduler=scheduler,workergroup=workergroup).count()

    #check the conflict with the assigned services
    @staticmethod
    def checkConflict(scheduler,workergroup,trainee):
        """Return True if the assigned workergroup has time conflict with the current assignments
        @param scheduler: a scheduler object
        @param workergroup:a workergroup object
        @param trainee:a trainee object
        """
        return Assignment.objects.filter(trainee=trainee,scheduler=scheduler,
                                  workergroup__instance__endTime__gte=workergroup.instance.startTime)
    #Get the missed services of current scheduler
    @staticmethod
    def getMissedAssignmentByTrainee(trainee):
        """return missed services of current scheduler
        @param trainee:trainee object
        """
        return Assignment.objects.filter(trainee=trainee,absent=1)

# Define the configuration for the scheduler
class Configuration(models.Model):
    """Define the configuration for the scheduler"""

    # The Minimum Requirement is to assign the minimum number needed for each workergroup
    # The Standard Requirement is to assign the standard number needed for each workergroup
    MODE = (
        ('Min', 'Minimum Requirement'),
        ('Tue', 'Standard Requirement'),
    )

    mode = models.CharField(max_length=3, choices=MODE)
    max_week_workload = models.IntegerField()
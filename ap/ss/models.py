"""
This is to define Service Scheduler, which is to assign the services to trainees for each week
"""
from django.db import models
from services.models import *
from django.db.models import Q
from datetime import datetime
from operator import itemgetter
#from collections import OrderedDict
from accounts.models import Trainee, TrainingAssistant
from django.db.models import Sum, Max, Count
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

    service = models.ForeignKey(Service, related_name="instances")
    period = models.ForeignKey(Period, related_name="instances")
    weekday = models.CharField(max_length=3, choices=WEEKDAY)
    start_time = models.TimeField('start time', null=True)
    end_time = models.TimeField('end time', null=True)

    # The time the trainee needed to rest after doing a specific service.
    recovery_time = models.IntegerField('time')

    #Get instances by service period and service
    @staticmethod
    def get_instances_by_service(period, service):
        """Get the QuerySet of instances by service
        @rtype : QuerySet of Instance
        @param period: period object
        @param service: service object
        """
        return Instance.objects.filter(service=service, period=period)

    #Get all the instances of current week ordered by time
    @staticmethod
    def get_instances_current_week():
        """Get the current service period according to current datetime
        @rtype : QuerySet of Instance
        """

        #Get the current date and get the current period
        _current_date = datetime.now().date()
        period = Period.objects.get(endDate__gte=_current_date, startDate__lte=_current_date)

        #Return the QuerySet of instances of this period ordered by start time
        return Instance.objects.filter(period=period).order_by("start_time")

    #Get the schedule conflicted instances of a certain instance
    @staticmethod
    def get_conflicted_instances(instance):
        """Get the instances which have time conflict with a certain instance
        @rtype : QuerySet of Instance
        @param instance: instance object
        """
        return Instance.objects.filter(weekday=instance.weekday, end_time__gte=instance.start_time)

    def __unicode__(self):
        return self.period.name + "  " + self.weekday + "  " + self.service.name


#Define Service group such as Monday Prep Brothers, etc
#From example,Monday Breakfast Prep includes Kitchen Star, Brothers, Sisters.
class WorkerGroup(models.Model):
    """Define the worker groups of each service instance"""

    name = models.CharField(max_length=200)
    instance = models.ForeignKey(Instance, related_name="workergroups")
    number_of_workers = models.IntegerField()

    # The minimum number of trainees required for the group.
    min_number_of_workers = models.IntegerField(blank=True)
    active = models.BooleanField()

    # Whether the worker group is designated or not.
    # Note:Some service instance is not designated, but its service worker group might be designated.
    designated = models.BooleanField(blank=True)

    # If it is Designated,  Many to Many relationship
    # one trainee might be designated to different worker groups,and one worker group might have different trainees..
    designated_trainees = models.ManyToManyField(Trainee, related_name="workergroups")

    #Get all the worker groups of current week ordered by time
    @staticmethod
    def get_non_designated_group_order_by_num_of_workers():
        """return the None-Designation Worker Group Order By Time of current week
        @rtype : QuerySet of Groups
        """

        #Get the current date and get the current period
        _current_date = datetime.now().date()
        period = Period.objects.get(endDate__gte=_current_date, startDate__lte=_current_date)

        #Get the QuerySet of WorkerGroup of non-designated services of current period,
        #ordered by number_of_workers
        return WorkerGroup.objects.select_related().filter(~Q(instance__service__category__name="Designated"),
                                                           active=1, instance__period=period, designated=0,
                                                           instance__service__isActive=1).order_by("number_of_workers")

    #Total workload of designated services of a trainee throughout the entire term.
    @staticmethod
    def workload_designated(trainee):
        """return the workload of designated services
        @rtype : int
        @param trainee: workergroup
        """
        #TODO We can add each week's designated service into assignment table to track their attendance
        pass

    #Check the conflict with the designated service.
    #Note: To reduce the possibility of conflicts, add designated related conflict services to exceptions.
    @staticmethod
    def check_conflict_designated(workergroup, trainee):
        """return true if the workergroup has time conflict with the designated services
        @rtype : int
        @param workergroup: workergroup object
        @param trainee: trainee object
        """
        return WorkerGroup.objects.filter(designated=1, designated_trainees=trainee,
                                          instance__end_time__gte=workergroup.instance.start_time).count()

    def __unicode__(self):
        return self.instance.period.name+"  "+self.instance.service.name+"  "+self.name


# Service Instance Exceptions.
# Some trainees might be not available for certain services because of certain reasons.
class ExceptionRequest(models.Model):
    """Define Service Instance Exceptions"""

    #The title of that exception, or the title of that exception request
    name = models.CharField(max_length=200)
    start_date = models.DateField('start time')
    end_date = models.DateField('end time')
    reason = models.TextField()
    approved = models.BooleanField()
    trainee_assistant = models.ForeignKey(TrainingAssistant, related_name="exceptionrequests")

    #The trainees who are exceptional from instances
    trainees = models.ManyToManyField(Trainee, related_name="exceptionrequests")
    instances = models.ManyToManyField(Instance, related_name="exceptionrequests")

    #The trainee who submit the request
    trainee = models.ForeignKey(TrainingAssistant, related_name="submitted_exceptionrequests")

    def __unicode__(self):
        return self.name


# Define service filter to build the dynamic django query parameter
class Filters(models.Model):
    """Define service filter to build the dynamic django query parameter"""
    name = models.CharField(max_length=200)

    #django query keyword
    keyword = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

    services = models.ManyToManyField(Service, related_name="filters")
    workergroups = models.ManyToManyField(WorkerGroup, related_name="filters")

    def __unicode__(self):
        return self.name


# Define Service Scheduler
class Scheduler(models.Model):
    """This is Scheduler class to run the service scheduling algorithm"""

    period = models.ForeignKey(Period)
    start_date = models.DateField()
    modified_time = models.DateTimeField()

    # The attendance trainee who created one instance of scheduler for a certain week
    trainee_attendance = models.ForeignKey(Trainee)

    # Main algorithm to schedule all the worker groups
    def run_scheduling(self):
        """Run the Service Scheduler, and store the assignment in the database
        @rtype : null
        """

        # Parameter to indicate that the algorithm just need to assign the minimum number to each worker group
        min_requirement = 1

        # Get the non designated worker groups of current week
        # TODO Further improvement: order the workerGroup by the ratio of the number of available trainees and the
        # TODO number of the needed trainees.
        workergroups = WorkerGroup.get_non_designated_group_order_by_num_of_workers()
        print "Total worker groups:" + str(workergroups.count())

        trainees = Trainee.objects.filter(active=1)
        print "Total trainees:" + str(trainees.count())

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
            pre_assignment[trainee.id] = 0
            tot_workload[trainee.id] = 0
            same_sv_counts[trainee.id] = 0
            pre_same_sv_date[trainee.id] = 0
            week_workload[trainee.id] = 0

        #Get the service non-related work history: pre_assignment and tot_workload
        print "Getting assignment history: total workload and previous assignment...."
        for trainee in trainees:
            tot_workload[trainee.id] = Assignment.get_total_workload_by_trainee(trainee)
            pre_assignment[trainee.id] = Assignment.get_pre_assignment(trainee)

        print "Non-Designated Worker Groups: " + str(workergroups.count())

        #Get the same_sv_counts in a quick way
        #--------------------------Just for Debug and Test--------------------------#
        #services = Service.objects.filter(isActive=1)
        #for sv in services:
            #Assignment.objects.filter(absent=0,workergroup__instance__service=sv).aggregate(Count('trainee'))

        #for trainee in trainees:
            #print trainee
            #for sv in services:
                #This query is very slow. If you use Assignment.objects.all(), it will be super fast.
                #Try raw sql, it might be very fast.
                #pre_same_sv_date[trainee.id] = Assignment.getPreAssignmentDateByService(trainee,sv)
        #-------------------------------------------------------------------#

        print "Getting the available trainees for each worker group"
        #List of QuerySets to store the available trainees for each worker group
        trainees_wgs = list()

        # Enumerate the worker groups to count the available number of trainees of each workerGroups
        # Sorting according to the ration of the number of available trainees and the number needed for each

        #Exclude the workergroup if its number_of_workers is zero.
        workergroups = workergroups.filter(~Q(min_number_of_workers=0))
        for i in range(workergroups.count()):
            group = workergroups[i]
            available_trainees = self.get_available_trainees(group)

            #use a dict to store trainees, workergroup and the ration
            trainee_wg = dict()
            trainee_wg['trainees'] = available_trainees
            trainee_wg['workergroup'] = group
            if min_requirement:
                trainee_wg['ratio'] = available_trainees.count()/group.min_number_of_workers
            else:
                trainee_wg['ratio'] = available_trainees.count()/group.number_of_workers

            # A list of dicts for sorting
            trainees_wgs.append(trainee_wg)
            trainees_wgs.sort(key=itemgetter('ratio'), reverse=False)

        # Enumerate the worker groups to assign the services
        assignments_list = list()
        for item in trainees_wgs:
            trainees_wg = item['trainees']
            group = item['workergroup']

            print "\n"
            print "Assigning for group:"+str(group)+" Available Trainees:"+str(trainees_wg.count())

            # Get the best candidates for the worker group
            best_candidates = self.get_best_candidates(trainees_wg, self, group, pre_assignment, tot_workload,
                                                       week_workload, same_sv_counts, pre_same_sv_date, min_requirement)

            print "Assigning " + str(len(best_candidates))+" Candidates" + \
                  "of " + str(group.min_number_of_workers) + " requirement of this group"

            #print bestCandidates

            # Store the assignment in the database and update the related variables
            for candidate in best_candidates:
                assignment = Assignment()
                assignment.scheduler = self
                assignment.workergroup = group
                #assignment.trainee = Trainee.objects.get(id=candidate["traineeId"])
                week_workload[candidate["traineeId"]] += assignment.workergroup.instance.service.workload
                #assignment.save()
                assignments_list.append(assignment)

    # Schedule for one worker group
    def run_scheduling_by_group(self, workergroup):
        """Run a schedule for one specific workergroup"""
        print workergroup
        return self

    # Get the list of available trainees
    @staticmethod
    def get_available_trainees(workergroup):
        """Get the available trainee list of workerGroup
        @rtype : lists of trainee objects
        @param workergroup: workergroup object
        """

        instance = workergroup.instance
        service = instance.service

        #TODO If we want to improve the speed ,we can store the service,instance related trainees in memory.
        #Step 1: filter according to the qualification
        if service.needQualification:
            trainees = service.qualifiedTrainees
        else:
            trainees = Trainee.objects.all()

        #Step 2: Filter trainees according to the filters
        filter_sv = service.filters.all()
        filter_wg = workergroup.filters.all()

        #creating dynamic filt parameter for filter()
        filters_tot = {}
        for filt in filter_sv:
            filters_tot[str(filt.keyword)] = str(filt.value)
        for filt in filter_wg:
            filters_tot[str(filt.keyword)] = str(filt.value)

        trainees = trainees.filter(**filters_tot)

        #Step 3: Further filter according to the exception
        _current_date = datetime.now().date()
        trainees = trainees.filter(~Q(exceptionrequests__instances=instance, exceptionrequests__approved=1,
                                   exceptionrequests__end_date__gte=_current_date,
                                   exceptionrequests__start_date__lte=_current_date))

        #print trainees.count()
        return trainees

    #Get the best candidates from available trainees for current group
    @staticmethod
    def get_best_candidates(trainees, scheduler, workergroup, pre_assignment,
                            tot_workload, week_workload,
                            same_sv_counts, pre_same_sv_date, min_requirement):
        """Get the list of best candidates of a certain group
        @rtype : list
        @param trainees: lists of dict
        @param scheduler: scheduler object
        @param workergroup: workergroup object
        @param pre_assignment: array
        @param tot_workload: array
        @param week_workload: array
        @param same_sv_counts: array
        @param pre_same_sv_date: array
        @param min_requirement: int
        """

        #List of dicts to store all the information needed for sorting
        best_candidates = list()
        service = workergroup.instance.service
        for trainee in trainees:

            same_sv_counts[trainee.id] = Assignment.get_pre_assignment_counts_by_services(trainee, service)
            pre_same_sv_date[trainee.id] = Assignment.get_pre_assignment_date_by_service(trainee, service)
            #TODO If it is too slow. To improvement, each trainee can have a dict to track the result,
            #TODO If ti is already have, then no need to query the db
            #TODO Trainee_sv_count{t_id : {sv_id: cont}}

            #Build the candidate{}, and bestCandidates[{},{},{}]
            candidate = dict()
            candidate["traineeId"] = trainee.id
            candidate["tot_workload"] = tot_workload[trainee.id]
            candidate["pre_assignment"] = pre_assignment[trainee.id]
            candidate["week_workload"] = week_workload[trainee.id]

            candidate["same_sv_counts"] = same_sv_counts[trainee.id]
            candidate["prev_same_sv_date"] = pre_same_sv_date[trainee.id]

            best_candidates.append(candidate)

        #TODO sort bestCandidates and choose the best one
        best_candidates.sort(key=itemgetter('tot_workload', 'week_workload', 'same_sv_counts'), reverse=False)

        count_assigned = Assignment.get_assignment_num_by_workergroup(workergroup, scheduler)

        #checkConflict is time consuming, therefore not check for all the available trainees.
        num = 0
        for candidate in best_candidates:
            if min_requirement:
                if num >= workergroup.min_number_of_workers-count_assigned:
                    return best_candidates[0:num]
            else:
                if num >= workergroup.number_of_workers-count_assigned:
                    return best_candidates[0:num]

            #check conflict. if there is conflict, remove the candidate from the bestCandidates
            if Assignment.check_conflict(scheduler, workergroup, candidate["traineeId"]):
                best_candidates.remove(candidate)
            else:
                num += 1

        #TODO if num is < workergroup.min_number_of_worker-count_assigned, need to free some one from other services.
        return best_candidates[0:num]

    def assign_designated(self):
        """Assign the designated worker groups.
        @rtype : null
        """

        workergroups = WorkerGroup.objects.filter(designated=1)
        for workergroup in workergroups:
            trainees = workergroup.designated_trainees.all()
            for trainee in trainees:
                assignment = Assignment()
                assignment.scheduler = self
                assignment.workergroup = workergroup
                assignment.trainee = trainee
                assignment.save()

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
        self.run_scheduling()

    #pring the worker groups by service instances
    @staticmethod
    def print_worker_groups():
        #cgs = Category.objects.all()
        cgs = Category.objects.filter(~Q(name="Designated"))
        for cg in cgs:
            print cg.name
            svs = Service.objects.filter(category=cg, isActive=1)
            for sv in svs:
                print "   " + sv.name
                pds = Period.objects.filter(services=sv, name='FTTA')
                for pd in pds:
                    print "     " + pd.name
                    ins = Instance.objects.filter(period=pd, service=sv)
                    if ins.count() > 0:
                        print "         " + "StarTime:" + str(ins[0].start_time) +\
                              "EndTime:" + str(ins[0].end_time)
                        wgs = ins[0].workergroups.filter(active=1, designated=0)
                        for wg in wgs:
                            print ":             "+str(wg.id) + " " + wg.name
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
    def print_service():
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
                        print "         " + "StarTime:" + str(ins[0].start_time) +\
                              "EndTime:" + str(ins[0].end_time)
                    else:
                        print "         None"

    # Analyse the result of assignment solution
    @staticmethod
    def analyse_assignment():

        trainees = Trainee.objects.all()
        cnt_trainees = trainees.count()

        #The total workload of each trainees
        tot_workload = []

        #The average week workload of each trainees
        avg_week_workload = []

        #The maximum week workload of each trainees
        max_week_workload = []

        #The minimum week workload of each trainees
        min_week_workload = []

        cnt = 0
        week_num = Scheduler.objects.all().count()
        sum_tot_workload = 0
        for trainee in trainees:
            tot_workload[cnt] = Assignment.get_total_workload_by_trainee(trainee)
            sum_tot_workload += tot_workload[cnt]
            avg_week_workload[cnt] = tot_workload[cnt]/week_num
            cnt += 1

        #The average of tot_workload[]
        avg_tot_workload = sum_tot_workload/cnt_trainees

        #The maximum one in tot_workload[]
        max_tot_workload = avg_tot_workload.index(max(avg_tot_workload))

        #The minimum one in tot_workload[]
        min_tot_workload = avg_tot_workload.index(max(avg_tot_workload))

        schedulers = Scheduler.objects.all().count()
        cnt_t = 0
        for trainee in trainees:
            week_workload = []
            cnt_s = 0
            for scheduler in schedulers:
                week_workload[cnt_s] = Assignment.get_week_workload(scheduler, trainee)
                cnt_s += 0

            max_week_workload[cnt_t] = week_workload.index(max(week_workload))
            min_week_workload[cnt_t] = week_workload.index(min(week_workload))
            cnt_t += 1

        print cnt_trainees
        print tot_workload
        print avg_week_workload
        print avg_tot_workload
        print max_tot_workload
        print min_tot_workload
        print max_week_workload
        print min_week_workload


# Service Assignment to record the scheduling solution.
class Assignment(models.Model):
    """Service Assignment"""

    # TODO consider: should we store the designated service assignments into the assignments table? It might be better
    # TODO to store them for attendance purpose.

    trainee = models.ForeignKey(Trainee, related_name="assignments")
    scheduler = models.ForeignKey(Scheduler, related_name="assignments")
    workergroup = models.ForeignKey(WorkerGroup, related_name="assignments")
    absent = models.BooleanField()
    assignment_date = models.DateField('assignment_date')

    #The substitution for that service
    sub_trainee = models.ForeignKey(Trainee, related_name="assignments_sub", null=True)

    @staticmethod
    def get_total_workload_by_trainee(trainee):
        """return the total workload of a trainee assigned already this term
        @rtype : int
        @param trainee: trainee object
        """
        #TODO if we add designated into assignment table, this will be the total workload.
        return Assignment.objects.filter(trainee=trainee, absent=0).aggregate(Sum(
            'workergroup__instance__service__workload'))['workergroup__instance__service__workload__sum']

    @staticmethod
    def get_week_workload(scheduler, trainee):
        """return the total workload of a trainee assigned already this term
        @rtype : int
        @param trainee: trainee object
        @param scheduler: scheduler object
        """
        return Assignment.objects.filter(scheduler=scheduler, trainee=trainee, absent=0).aggregate(Sum(
            'workergroup__instance__service__workload'))['workergroup__instance__service__workload__sum']

    @staticmethod
    def get_total_workload_by_trainee_non_designated(trainee):
        """return the total workload of non designated services of a trainee assigned already this term
        @rtype : int
        @param trainee: trainee object
        """
        #TODO if we add designated into assignment table, this will be the total workload.
        return Assignment.objects.filter(trainee=trainee, absent=0, workergroup__isDesignated=0).aggregate(Sum(
            'workergroup__instance__service__workload'))['workergroup__instance__service__workload__sum']

    @staticmethod
    def get_pre_assignment_counts_by_services(trainee, service):
        """return the times of a trainee already assigned of a service
        @rtype : int
        @param trainee: a trainee object
        @param service: a service object
        """
        sql = "select count(a.id) from ss_assignment as a, ss_workergroup as wg,ss_instance as inst,services_service " \
              "as sv where a.workergroup_id=wg.id and wg.instance_id=inst.id and inst.service_id=sv.id and sv.id=" \
              + str(service.id)+" and a.trainee_id="+str(str(trainee.id))
        return Assignment.objects.raw(sql)
        #return Assignment.objects.filter(trainee=trainee,absent=0,workergroup__instance__service=service).count()

    @staticmethod
    def get_pre_assignment_date_by_service(trainee, service):
        """return the last time the trainee was assigned to this service
        @rtype : QuerySet of Assignment
        @param trainee: trainee object
        @param service: service object
        """

        # Using raw sql is much faster, it seems that using raw sql, the db can't recognize the field with capital
        # letter.
        sql = "select a.* from ss_assignment as a, ss_workergroup as wg,ss_instance as inst,services_service " \
              "as sv where a.workergroup_id=wg.id and wg.instance_id=inst.id and inst.service_id=sv.id and sv.id=" \
              + str(service.id)+" and a.trainee_id="+str(str(trainee.id))+" order by a.assignment_date"
        return Assignment.objects.raw(sql)
        #return Assignment.objects.filter(trainee=trainee,absent=0,workergroup__instance__service=service).order_by(
        #    "assignment_date")

    #Return the previous assignment of a trainee did.
    @staticmethod
    def get_pre_assignment(trainee):
        """return the last service instance
        @rtype : Assignment object
        @param trainee: trainee object
        """
        return Assignment.objects.filter(trainee=trainee, absent=0).order_by("assignment_date")[:1]

    #Check whether the workers are assigned to the workergroup
    @staticmethod
    def check_assignment(scheduler, workergroup):
        """return True if the WorkerGroup is already assigned
        @rtype : Boolean
        @param scheduler: scheduler object
        @param workergroup: workergroup object
        """
        num = Assignment.objects.filter(scheduler=scheduler, workergroup=workergroup).count()
        if num < workergroup.number_of_workers:
            return False
        else:
            return True

    #Check whether the min number of workers are assigned to the workergroup
    @staticmethod
    def check_assignment_minimum(scheduler, workergroup):
        """return True if the workergroup minimum requirement is fulfilled
        @rtype : Boolean
        @param scheduler: scheduler object
        @param workergroup: workergroup object
        """
        num = Assignment.objects.filter(scheduler=scheduler, workergroup=workergroup).count()
        if num < workergroup.min_number_of_workers:
            return False
        else:
            return True

    #check the conflict with the assigned services
    @staticmethod
    def check_conflict(scheduler, workergroup, trainee):
        """Return True if the assigned workergroup has time conflict with the current assignments
        @param scheduler: a scheduler object
        @param workergroup:a workergroup object
        @param trainee:a trainee object
        """
        return Assignment.objects.filter(trainee=trainee, scheduler=scheduler,
                                         workergroup__instance__end_time__gte=workergroup.instance.start_time)

    #Get the number of assignments of a certain workergroup
    @staticmethod
    def get_assignment_num_by_workergroup(scheduler, workergroup):
        """return the number of assignment to a workergroup
        @param scheduler: scheduler object
        @param workergroup: workergroup object
        @rtype : QuerySet of Assignment
        """
        return Assignment.objects.filter(scheduler=scheduler, workergroup=workergroup).count()

    #Return the service assignment of a certain trainee, scheduler
    @staticmethod
    def get_assignments_by_trainee(trainee, scheduler):
        """return all the set of service instances of a trainee
        @param trainee: trainee object
        @param scheduler: scheduler object
        @rtype : QuerySet of Assignment
        """
        return Assignment.objects.filter(trainee=trainee, scheduler=scheduler)

    #Get the missed services of current scheduler
    @staticmethod
    def get_missed_assignment_by_trainee(trainee):
        """return missed services of current scheduler
        @rtype : QuerySet of Assignment
        @param trainee:trainee object
        """
        return Assignment.objects.filter(trainee=trainee, absent=1)


# Define the configuration for the scheduler
class Configuration(models.Model):
    """Define the configuration for the scheduler"""

    # The Minimum Requirement is to assign the minimum number needed for each workergroup
    # The Standard Requirement is to assign the standard number needed for each workergroup
    MODE = (
        ('Min', 'Minimum Requirement'),
        ('Std', 'Standard Requirement'),
    )

    mode = models.CharField(max_length=3, choices=MODE)
    max_week_workload = models.IntegerField()
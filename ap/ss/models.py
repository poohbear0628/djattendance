from django.db import models
#from users.models import UserAccount

#This is for service scheduler .
#Define service and assign service to trainees


#define service category such as Cleaning, Guard etc
class serviceCategory(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField()

    #return services of this category
    def getService(self):
        return service.objects.filter(svCategory=self)


#define service such as Breakfast Cleaning, Dinner Prep, Guard A, etc
class service(models.Model):

    svCategory = models.ForeignKey(serviceCategory)
    name = models.CharField(max_length=1000)
    isActive = models.BooleanField()
    workLoad = models.IntegerField()


#define service Period such as Pre-Training, FTTA regular week, etc
class servicePeriod(models.Model):

    name = models.CharField(max_length=200)

    #which service is on this Period
    service = models.ManyToManyField(service)

    startDate = models.DateField('start date')
    endDate = models.DateField('end date')

    #return the services of this Period
    def getService(self):
        return service.objects.filter(svPeriod=self)


#define one specific service instance such as Monday Break Prep, Monday Guard C, etc
class serviceInstance(models.Model):

    WEEKDAY = (
        ('Sun', 'Sunday'),
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
    )

    service = models.ForeignKey(service)
    svPeriod = models.ForeignKey(servicePeriod)
    weekday = models.CharField(max_length=3, choices=WEEKDAY)
    startTime = models.TimeField('start time')
    endTime = models.TimeField('end time')
    recoveryTime = models.IntegerField('time')


#define service group such as Monday Prep Brothers, etc
class serviceWorkerGroup(models.Model):

    name = models.CharField(max_length=200)
    service = models.ForeignKey(service)
    svPeriod = models.ForeignKey(servicePeriod)
    numberOfWorkers = models.IntegerField()
    isActive = models.BooleanField()


#service scheduler
class serviceScheduler(models.Model):

    svPeriod = models.ForeignKey(servicePeriod)
    startDate = models.DateField()
    modifiedTime = models.DateTimeField()
    #TODO Trainee = models.ForeignKey(Trainee)


#service assignment
class serviceAssignment(models.Model):

    #TODO Trainee=models.ForeignKey(Trainee)
    svScheduler = models.ForeignKey(serviceScheduler)
    svWorkerGroup = models.ForeignKey(serviceWorkerGroup)
    isAbsent = models.BooleanField()
    #subTrainee = models.ForeignKey(Trainee)


#service missed, not necessary
class serviceMissed(models.Model):

    #TODO Trainee = models.ForeignKey(Trainee)
    svScheduler = models.ForeignKey(serviceScheduler)
    svWorkerGroup = models.ForeignKey(serviceWorkerGroup)


from django.core.management.base import BaseCommand
from schedules.models import Event, Schedule
from accounts.models import Trainee
from terms.models import Term
from django.db.models import Q


from datetime import time

class Command(BaseCommand):
  def _create_schedule(self):

    #all trainees
    main_s = Schedule(name='Main', season='All', term=Term.current_term(), priority=1)
    main_s.save()

    main_s.events = Event.objects.filter(Q(type='H')|Q(type='M')|Q(class_type='MAIN'))
    main_s.trainees = Trainee.objects.all()
    main_s.save()

    #1st year    
    oneyear_s = Schedule(name='1st Year', season='All', term=Term.current_term(), priority=2)
    oneyear_s.save()

    oneyear_s.events = Event.objects.filter(class_type='1YR')
    oneyear_s.trainees = Trainee.objects.filter(current_term__lte=2)
    oneyear_s.save()

    #2nd year
    twoyear_s = Schedule(name='2nd Year', season='All', term=Term.current_term(), priority=2)
    twoyear_s.save()

    twoyear_s.events = Event.objects.filter(class_type='2YR')
    twoyear_s.trainees = Trainee.objects.filter(current_term__gte=3)
    twoyear_s.save()

    #campus times
    campus_generic = Schedule(name='Generic Campus', season='All', term=Term.current_term(), priority=3)
    campus_generic.save()

    campus_generic.events = Event.objects.filter(monitor='TM')
    campus_generic.trainees = Trainee.objects.filter(team__type='CAMPUS')
    campus_generic.save()


  def handle(self, *args, **options):
    print("* Populating schedules...")
    self._create_schedule()

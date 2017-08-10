from django.core.management.base import BaseCommand
from schedules.models import Event, Schedule
from accounts.models import Trainee
from terms.models import Term

from datetime import time

class Command(BaseCommand):
  def _create_schedule(self, name):
    events = map(lambda e: e.id, Event.objects.all())
    trainees = map(lambda t: t.id, Trainee.objects.all())
    s = Schedule(name=name, season='All', term=Term.current_term(), priority=1, trainee_select='MC')
    s.save()
    s.events = events
    s.trainees = trainees
    s.save()

  def handle(self, *args, **options):
    print("* Populating schedules...")
    self._create_schedule('Main')
    self._create_schedule('Group Events')

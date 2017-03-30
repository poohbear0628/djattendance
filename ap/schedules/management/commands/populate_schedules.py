from django.core.management.base import BaseCommand
from schedules.models import Event, Schedule
from accounts.models import Trainee
from terms.models import Term

from datetime import time

class Command(BaseCommand):
    def _create_schedule(self):
        s = Schedule(name='Main',  season='All', term=Term.current_term(), priority=1, trainee_select='MC')
        s.save()
        s.events = map(lambda e: e.id, Event.objects.all())
        s.trainees = map(lambda t: t.id, Trainee.objects.all())
        s.save()

    def handle(self, *args, **options):
        self._create_schedule()

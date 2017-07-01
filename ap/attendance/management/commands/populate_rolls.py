from django.core.management.base import BaseCommand
from attendance.models import Roll
from schedules.models import Event
from accounts.models import Trainee
from terms.models import Term
import random

def new_roll(trainees=[], am=[]):
    events = Event.objects.filter(type="C")
    status = ['P', 'A', 'T', 'U', 'L']
    for trainee in trainees:
        if trainee.gender == "B":
            cur_am = random.choice(am.filter(gender="B"))
        elif trainee.gender == "S":
            cur_am = random.choice(am.filter(gender="S"))
        print trainee
        for e in events:
            random.seed()
            for i in range(0, 19):
                trainee_stat = random.choice(status)
                Roll(event=e, trainee=trainee, status=trainee_stat, submitted_by=trainee, date=Term.get_date(Term.current_term(), i, e.weekday)).save()
                if trainee_stat == "P":
                    Roll(event=e, trainee=trainee, status=random.choice(status), submitted_by=cur_am, date=Term.get_date(Term.current_term(), i, e.weekday)).save()
                elif trainee_stat == "A":
                    Roll(event=e, trainee=trainee, status="A", submitted_by=cur_am, date=Term.get_date(Term.current_term(), i, e.weekday)).save()
                else:
                    Roll(event=e, trainee=trainee, status=random.choice(['A', trainee_stat]), submitted_by=cur_am, date=Term.get_date(Term.current_term(), i, e.weekday)).save()


class Command(BaseCommand):
    # to use: python ap/manage.py populate_rolls --settings=ap.settings.dev
    def _create_rolls(self):
        # change the array below to get different trainees
        trainees = Trainee.objects.filter(current_term__gt=2)
        am = Trainee.objects.filter(groups__name="attendance_monitors")
        new_roll(trainees, am)
        print 'rolls added'

    def handle(self, *args, **options):
        self._create_rolls()
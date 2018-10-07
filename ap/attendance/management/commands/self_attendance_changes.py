from django.core.management.base import BaseCommand
from accounts.models import *
from attendance.models import *
from terms.models import *
import datetime

class Command(BaseCommand):
    # to use: python ap/manage.py self_attendance_changes --settings=ap.settings.dev
    def _check_trainees(self):
        sa_trainees = Trainee.objects.filter(self_attendance=True)
        for trainee in sa_trainees:
            roll = trainee.current_rolls().filter(submittted_by=trainee).earliest('date')
            roll_date = roll.date
            idx = (roll_date.weekday() + 1) % 7
            last_sat = roll_date - datetime.timedelta(7+idx-6)
            ct = Term.current_term()
            sap, created = SelfAttendancePool.objects.get_or_create(term=ct, date=last_sat, description='Initial load after AMs submitted it, created via scripts')
            sap.trainees.add(trainee)
            sap.save()


    def handle(self, *args, **options):
        print('* Creating SelfAttendancePool objects assuming that many were put onto self-attendance')
        self._check_trainees()

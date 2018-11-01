from accounts.models import TrainingAssistant
from attendance.models import Roll
from accounts.models import User

from django.core.management.base import BaseCommand

TAS = list(TrainingAssistant.objects.all())
AMS = list(User.objects.filter(groups__name="attendance_monitors").exclude(groups__name="training_assistant").exclude(groups__name="dev"))


class Command(BaseCommand):
  # to use: python ap/manage.py change_to_single_roll_system
  def _change_to_single_roll_system(self):
    rolls = list(Roll.objects.all())
    i = 0
    while rolls:
      roll = rolls[i]
      trainee = roll.trainee
      event = roll.event
      date = roll.date

      duplicates = Roll.objects.filter(trainee=trainee, event=event.id, date=date)
      if duplicates.count() == 1:
        dup = duplicates.first()
        if dup.submitted_by != trainee:
          dup.submitted_by = trainee
          dup.save()
      else:
        for dup in duplicates:
          if dup.submitted_by != dup.trainee and dup.submitted_by in AMS:
            print "deleting", dup.id, dup.submitted_by
            dup.delete()
          if dup.submitted_by != dup.trainee and dup.submitted_by in TAS:
            print dup.id, dup.submitted_by, dup.trainee

      rolls.pop()

  def handle(self, *args, **options):
    print '* Let it begin *'
    self._change_to_single_roll_system()

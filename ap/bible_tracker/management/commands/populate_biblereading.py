from django.core.management.base import BaseCommand
from bible_tracker.models import BibleReading
from accounts.models import Trainee
import random


def randomsequence():
  seq = ""
  for i in range(0, 7):
    seq += random.choice(['C', 'M', 'N'])
  return seq


def randombooks():
  books = list(range(2))
  books[0] = random.sample(range(0, 65), random.randint(0, 64))
  books[1] = random.sample(range(39, 65), random.randint(0, 26))
  s = {}
  for i in books[0]:
    s.update({"1_" + str(i): "Y"})
  for i in books[1]:
    s.update({"2_" + str(i): "Y"})
  return s

class Command(BaseCommand):

  def _create_biblereading(self):

    #remove all existing records of Bible Reading
    BibleReading.objects.all().delete()

    #generate a record of random Bible Reading
    trainees = Trainee.objects.all()
    for t in trainees:
      week = {}
      for i in range(0, 16):
        k = "{\"status\": \"%s\", \"finalized\": \"Y\"}" % randomsequence()
        week.update({"15_" + str(i): str(k)})
      BibleReading.objects.create(trainee=t, weekly_reading_status=week, books_read=randombooks())

  def handle(self, *args, **options):
    print('* Populating BibleReading records...')
    self._create_biblereading()

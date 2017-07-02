from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from bible_tracker.models import BibleReading
from accounts.models import Trainee
from django_hstore import hstore
import json
import random

def randomsequence():
    
    seq = ""
    for i in range(0, 7):
        seq += random.choice(['C', 'M', 'N'])

    return seq

def randombooks():
    books = range(2)
    books[0] = random.sample(range(0, 65), random.randint(0, 64))
    books[1] = random.sample(range(39, 65), random.randint(0, 26))
    s = {}
    for i in books[0]:
        s.update({"1_"+str(i): "Y"})

    for i in books[1]:
        s.update({"2_"+str(i): "Y"})

    return s

def set_booksread():
    return {"1_46": "Y", "1_47": "Y", "1_40": "Y", "1_51": "Y", "1_42": "Y", "1_50": "Y", "1_2": "Y", "2_41": "Y", "2_40": "Y", "2_42": "Y", "2_39": "Y"}


class Command(BaseCommand):
# to use: python ap/manage.py populate_trainees --settings=ap.settings.dev
    def _create_biblereading(self): 

        BibleReading.objects.all().delete()

        trainees = Trainee.objects.all()
        for t in trainees:           
            
            week = {}
            for i in range(0, 16):
                k = "{\"status\": \"%s\", \"finalized\": \"Y\"}" % randomsequence()
                week.update({"15_" + str(i) : str(k)})
                # week = "15_" + str(i)
                # print week

            BRrecord = BibleReading.objects.create(trainee=t, weekly_reading_status=week, books_read=randombooks())

    def handle(self, *args, **options):
        print('* Creating BibleReading records...')
        self._create_biblereading()
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from bible_tracker.models import BibleReading
from accounts.models import Trainee
import random


def set_readingstatus():
    # print random.choice(['C', 'M', 'N'])
    readingstatus = {}
    for i in range(0, 19):
        stat = ""
        
        for k in range(0, 7):
            stat = stat + (random.choice(['C', 'M', 'N']))
        
        readstat = {}
        readstat["status"] = stat
        readstat["finalized"] = "Y"
        readingstatus["15_%i" % i] = readstat


    print str(readingstatus)
    return {"15_17": "{\"status\": \"CCMNMNM\", \"finalized\": \"Y\"}", "15_18": "{\"status\": \"CCMNMNM\", \"finalized\": \"N\"}"}

def set_booksread():
    return {"1_46": "Y", "1_47": "Y", "1_40": "Y", "1_51": "Y", "1_42": "Y", "1_50": "Y", "1_2": "Y", "2_41": "Y", "2_40": "Y", "2_42": "Y", "2_39": "Y"}


class Command(BaseCommand):
# to use: python ap/manage.py populate_trainees --settings=ap.settings.dev
    def _create_biblereading(self): 

        trainees = Trainee.objects.all()

        for t in trainees:           
            BibleReading(trainee=t, weekly_reading_status=set_readingstatus(), books_read=set_booksread()).save()


    def handle(self, *args, **options):
        print('* Creating BibleReading records...')
        self._create_biblereading()
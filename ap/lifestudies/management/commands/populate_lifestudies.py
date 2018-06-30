from django.core.management.base import BaseCommand
from accounts.models import Trainee, User
from lifestudies.models import Discipline
from datetime import date, datetime
import random


class Command(BaseCommand):
  # to use: python ap/manage.py populate_lifestudies --settings=ap.settings.dev
  def _create_lifestudies(self):

    tas = User.objects.filter(type='T')
    infraction_choice = ['AT', 'CI', 'MS', 'S','AN','G','C','M','HI','L','MISC']
    for ta in tas:
        trainees = Trainee.objects.filter(TA=ta)
        if trainees.count() > 0:
            val = random.sample(range(0, trainees.count()-1), 6)
            due_date = datetime.today()
            for v in val[0:2]:
                t = trainees[v]
                ls = Discipline(infraction=random.choice(infraction_choice), quantity=1, due=due_date, offense='RO', trainee=t, note='populated data for sample')
                ls.save()

            for v in val[3:5]:
                t = trainees[v]
                ls = Discipline(infraction='AT', quantity=random.choice(range(1, 20)), due=due_date, offense='MO', trainee=t, note='populated data for sample')
                ls.save()


  def handle(self, *args, **options):
    print("* Populating lifestudies...")
    self._create_lifestudies()

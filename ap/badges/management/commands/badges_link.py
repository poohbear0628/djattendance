from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from accounts.models import *
from .models import Badge

class Command(BaseCommand):
  # to use: python ap/manage.py populate_tas --settings=ap.settings.dev

  def _link_badges(self):
    # change the array below to get different tas
    listofu = User.objects.all()
    for u in listofu:
      b = Badge.objects.get(firstname=u.firstname, lastname=u.lastname)
      if b is not None:
        u.badge = b
        u.save()   

  def handle(self, *args, **options):    
    print('* Linking badges to User...')
    self._link_badges()

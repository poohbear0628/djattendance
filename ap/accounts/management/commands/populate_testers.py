from django.core.management.base import BaseCommand
from accounts.models import User

def new_tester(testers=[], gender = 'B'):
  for tester in testers:
    email = '.'.join(tester["name"].lower().split(' ')) + "@gmail.com"
    password = 'ap'
    firstname = tester["name"].split(' ')[0]
    lastname = tester["name"].split(' ')[1]

    if 'ta_' in firstname:
      date_of_birth = '1974-12-12'
      u = User(is_active=True, email=email, firstname=firstname, lastname=lastname, gender=gender, password=password, type='T', date_of_birth=date_of_birth, is_staff=True, is_admin=True)
    else:
      date_of_birth = '1993-11-12'
      u = User(is_active=True, email=email, firstname=firstname, lastname=lastname, gender=gender, password=password, type='R', date_of_birth=date_of_birth, current_term=tester["term"])
    u.set_password(password)
    u.save()

class Command(BaseCommand):
  # to use: python ap/manage.py populate_testsetup --settings=ap.settings.dev
  def _create_testers(self):
    testers = [{"name": "tester1 trainee", "term": 1},
          {"name": "tester2 trainee", "term": 2},
          {"name": "tester3 trainee", "term": 3},
          {"name": "tester4 trainee", "term": 4},
          {"name":"ta_tester ta"},
          ]
    new_tester(testers)

  def handle(self, *args, **options):
    print('* Populating testers...')
    self._create_testers()

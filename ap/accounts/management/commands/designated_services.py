from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from accounts.models import *


class Command(BaseCommand):
  # to use: python ap/manage.py populate_tas --settings=ap.settings.dev
  # use this script to add people in service groups into the designated group so they can input service hours

  def _designated_services_input(self):
    # change the array below to get different gorups
    des_list = ['attendance_monitors', 'av', 'dev', 'networks', 'facility_maintenance', 'frames', 'linens', 'service_schedulers', 'designated_service', 'special_projects', 'office_support', 'badges', 'health_office', 'kitchen']
    des = Group.objects.get(name='designated_service')
    for d in des_list:
      print "adding people into ", d
      print ' '
      group = Group.objects.get(name=d)
      list_trainees = User.objects.filter(type='R', groups=group)
      for t in list_trainees:
        des.user_set.add(t)
        print "added ", t.full_name, " into ", d

  def handle(self, *args, **options):    
    print('* Adding Users into designated service group so they can input service hours...')
    self._designated_services_input()

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate
import django.contrib.auth
from sets import Set

# Adds all the permissions for the listed models
def model_permissions(group, model_name_list):
  for model_name in model_name_list:
    ct = ContentType.objects.get(model=model_name)
    permission_list = Permission.objects.filter(content_type=ct)
    for permission in permission_list:
      group.permissions.add(permission)

# Adds all the permissions for the listed apps
# Locks down all the models in listed apps to specific group
def app_permissions(group, app_label_list):
  for app_label in app_label_list:
    cts = ContentType.objects.filter(app_label=app_label)
    for ct in cts:
      permission_list = Permission.objects.filter(content_type=ct)
      for permission in permission_list:
        group.permissions.add(permission)

def add_group_permissions(sender, **kwargs):
  print 'Populating Permission Groups...'

  permission_set = Set(Group.objects.all())

  permission_list = [
    'administration',
    'maintenance',
    'absent_trainee_roster',
    'attendance_monitors',
    'av',
    'dev',
    'networks',
    'exam_graders',
    'grad_committee',
    'HC',
    'facility_maintenance_or_frames_or_linens',
    'house_inspectors',
    'semi_annual_testing_group_coordinators',
    'service_schedulers',
    'team_monitors',
    'ypc_monitors',
    'xb_trainees',
    'designated_service',
    'special_projects',
    'office_support',
    'badges',
    'health_office',
    'kitchen',
  ]

  # Add predefined permissions if not in db already
  for p in permission_list:
    group, created = Group.objects.get_or_create(name=p)
    if created:
      print 'Added Permission', group
    if group in permission_set:
      permission_set.remove(group)

  # Delete any permissions in db not declared explicitly here
  for p in permission_set:
    p.delete()
    print 'Deleted Permission', p

  print 'Permissions updated.'

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate
from django.dispatch import receiver
import django.contrib.auth
from sets import Set
# from accounts.models import Trainee, User

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

# @receiver(post_migrate, sender=django.contrib.auth)
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


  # #This permission group includes the permanent Training Assistant (TA) brothers, helper TA brothers, TA sisters, brother Dennis Higashi, and brother Curt Kennard. They can see everything except for developer tools.
  # AdminGroup, created = Group.objects.get_or_create(name="administration")
  # MaintenanceGroup = Group.objects.get_or_create(name="maintenance")
  # #Do I need a general trainee permission group?
  # AbsentTraineeRosterGroup, created = Group.objects.get_or_create(name="absent_trainee_roster")
  # AttendanceMonitorGroup, created = Group.objects.get_or_create(name="attendance_monitors")
  # AVGroup = Group.objects.get_or_create(name="av")
  # DeveloperGroup = Group.objects.get_or_create(name="dev")
  # ExamGraderGroup = Group.objects.get_or_create(name="exam_graders")
  # GradCommitteeGroup = Group.objects.get_or_create(name="grad_committee")
  # HCGroup = Group.objects.get_or_create(name="HC")
  # FFLGroup = Group.objects.get_or_create(name="facility_maintenance_or_frames_or_linens")
  # HouseInsepectorGroup = Group.objects.get_or_create(name="house_inspectors")
  # SATestingGroupsCoordinatorsGroup = Group.objects.get_or_create(name="semi_annual_testing_group_coordinators")
  # ServiceSchedulerGroup = Group.objects.get_or_create(name="service_schedulers")
  # TeamMonitorGroup = Group.objects.get_or_create(name="team_monitors")
  # YPCMonitorGroup = Group.objects.get_or_create(name="ypc_monitors")
  # XBTrainee = Group.objects.get_or_create(name="xb_trainees")
  # DesignatedServiceGroup = Group.objects.get_or_create(name="designated_service")
  # #4th term trainees. Do we need to make a group for that?
  # #2nd year trainees to submit personal attendance. Isn't there a smarter way to check which term a trainee is in?
  # SpecialProjectsGroup = Group.objects.get_or_create(name="special_projects")
  # OfficeSupportGroup = Group.objects.get_or_create(name="office_support")
  # BadgesGroup = Group.objects.get_or_create(name="badges")
  # HealthOfficeGroup = Group.objects.get_or_create(name="health_office")
  # KitchenGroup = Group.objects.get_or_create(name="kitchen")
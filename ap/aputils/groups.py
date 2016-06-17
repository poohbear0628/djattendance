from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate
from django.dispatch import receiver

#Adds all the permissions for the listed models
def model_permissions(group_name, model_name_list):
	for model_name in model_name_list:
		ct = ContentType.objects.get(model=model_name)
		permission_list = Permission.objects.filter(content_type=ct)
		for permission in permission_list:
			group_name.permissions.add(permission)

#Adds all the permissions for the listed apps
def app_permissions(group_name, app_label_list):
	for app_label in app_label_list:
		cts = ContentType.objects.filter(app_label=app_label)
		for ct in cts:
			permission_list = Permission.objects.filter(content_type=ct)
			for permission in permission_list:
				group_name.permissions.add(permission)



@receiver(post_migrate)
def add_group_permissions(sender, **kwargs):
	Group.objects.all().delete()
	#This permission group includes the permanent Training Assistant (TA) brothers, helper TA brothers, TA sisters, brother Dennis Higashi, and brother Curt Kennard. They can see everything except for developer tools. 
	AdminGroup, created = Group.objects.get_or_create(name="administration")
	MaintenanceGroup = Group.objects.get_or_create(name="maintenance")
	#Do I need a general trainee permission group?
	AbsentTraineeRosterGroup, created = Group.objects.get_or_create(name="absent_trainee_roster")
	AttendanceMonitorGroup, created = Group.objects.get_or_create(name="attendance_monitors")
	AVGroup = Group.objects.get_or_create(name="av")
	DeveloperGroup = Group.objects.get_or_create(name="dev")
	ExamGraderGroup = Group.objects.get_or_create(name="exam_graders")
	GradCommitteeGroup = Group.objects.get_or_create(name="grad_committee")
	HCGroup = Group.objects.get_or_create(name="HC")
	FFLGroup = Group.objects.get_or_create(name="facility_maintenance_or_frames_or_linens")
	HouseInsepectorGroup = Group.objects.get_or_create(name="house_inspectors")
	SATestingGroupsCoordinatorsGroup = Group.objects.get_or_create(name="semi_annual_testing_group_coordinators")
	ServiceSchedulerGroup = Group.objects.get_or_create(name="service_schedulers")
	TeamMonitorGroup = Group.objects.get_or_create(name="team_monitors")
	YPCMonitorGroup = Group.objects.get_or_create(name="ypc_monitors")
	XBTrainee = Group.objects.get_or_create(name="xb_trainees")
	DesignatedServiceGroup = Group.objects.get_or_create(name="designated_service")
	#4th term trainees. Do we need to make a group for that? 
	#2nd year trainees to submit personal attendance. Isn't there a smarter way to check which term a trainee is in?
	SpecialProjectsGroup = Group.objects.get_or_create(name="special_projects")
	OfficeSupportGroup = Group.objects.get_or_create(name="office_support")
	BadgesGroup = Group.objects.get_or_create(name="badges")
	HealthOfficeGroup = Group.objects.get_or_create(name="health_office")
	KitchenGroup = Group.objects.get_or_create(name="kitchen")
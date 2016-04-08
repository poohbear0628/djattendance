# from django.contrib import admin
# from django import forms

# #enable manage services in admin panel#
# from ss.models import *


# class WorkerAdminForm(admin.ModelAdmin):
#   # add in qualifications + designated in the future
#   list_display = ('trainee', 'health', 'workload', )
#   # list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
#   search_fields = ('trainee', 'workload', 'services_eligible', 'qualifications')
#   ordering = ('trainee',)
#   # exclude= ('permissions',)

# class InstanceAdminForm(admin.ModelAdmin):
#   # add in qualifications + designated in the future
#   list_display = ('service', 'period', 'start', 'filled', 'workers_needed', )
#   # list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
#   search_fields = ('service__name', 'period', 'start',)
#   ordering = ('service__name',)
#   # exclude= ('permissions',)

# class AssignmentAdminForm(admin.ModelAdmin):
#   # add in qualifications + designated in the future
#   list_display = ('instance', 'worker', 'role',)
#   # list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
#   # search_fields = ('service__name', 'period', 'start',)
#   ordering = ('instance',)
#   # exclude= ('permissions',)

# class ScheduleAdminForm(admin.ModelAdmin):
#   # add in qualifications + designated in the future
#   list_display = ('desc', 'period', 'workload_margin',)
#   # list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
#   # search_fields = ('service__name', 'period', 'start',)
#   ordering = ('desc',)
#   # exclude= ('permissions',)


# admin.site.register(Instance, InstanceAdminForm)
# admin.site.register(WorkerGroup)
# admin.site.register(Worker, WorkerAdminForm)
# admin.site.register(Exception)
# admin.site.register(Qualification)
# admin.site.register(Assignment, AssignmentAdminForm)
# admin.site.register(Schedule, ScheduleAdminForm)
# # admin.site.register(ExceptionRequest)
# # admin.site.register(Filters)

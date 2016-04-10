from django.contrib import admin
from django import forms

from services.models import *


# class ServiceAdminForm(admin.ModelAdmin):
#   list_display = ('name', 'category', 'active', 'designated', 
#                   'gender', 'workers_required', 'weekday')
#   # list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
#   search_fields = ('name', 'category__name',)
#   ordering = ('name',)
#   exclude= ('permissions',)
#   # Allows django admin to duplicate record
#   save_as = True

#   class Meta:
#     model = Service
#     fields = '__all__'


# class ServiceWorkerGroupAdminForm(admin.ModelAdmin):
#   list_display = ('service', 'worker_group', 'workers_required', 'workload', 
#                   'role', 'gender')
#   # list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
#   search_fields = ('service', 'workload',)
#   ordering = ('service',)
#   # exclude= ('permissions',)
#   # Allows django admin to duplicate record
#   save_as = True

#   class Meta:
#     model = Service
#     fields = '__all__'

# from seasonal_service_schedule import *
# from service import *
# from worker import *
# from workergroup import *
# from exception import *
# from assignment import *
# from week_schedule import *

admin.site.register(ScheduleCategory)
admin.site.register(SeasonalServiceSchedule)

admin.site.register(Category)
admin.site.register(Service)
admin.site.register(AssignmentPool)

admin.site.register(Qualification)
admin.site.register(Worker)

admin.site.register(QueryFilter)
admin.site.register(WorkerGroup)

admin.site.register(Exception)

admin.site.register(Assignment)
admin.site.register(WeekSchedule)

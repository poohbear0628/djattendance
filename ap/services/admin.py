from django.contrib import admin
from django import forms

from services.models import *

from django_hstore.widgets import BaseAdminHStoreWidget, GrappelliAdminHStoreWidget, SuitAdminHStoreWidget

from django_hstore.forms import DictionaryField

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

class WorkerAdminForm(admin.ModelAdmin):
  list_display = ('trainee', 'health', 'services_cap')
  # list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
  ordering = ('trainee__account__firstname',)
  # exclude= ('permissions',)
  # Allows django admin to duplicate record
  # save_as = True

  class Meta:
    model = Worker
    fields = '__all__'


class AssignmentPoolAdminForm(admin.ModelAdmin):
  list_display = ('service', 'worker_group', 'workers_required', 'role', 'gender')
  # list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
  ordering = ('service', 'worker_group',)
  # exclude= ('permissions',)
  # Allows django admin to duplicate record
  # save_as = True

  class Meta:
    model = Worker
    fields = '__all__'


from django.contrib.postgres.fields import HStoreField

class QuerySetAdminForm(forms.ModelForm):
  class Meta:
    model = QueryFilter
    fields = '__all__'
  
  query = DictionaryField(widget=SuitAdminHStoreWidget)


class QueryFilterAdminForm(admin.ModelAdmin):
  form = QuerySetAdminForm

  list_display = ('name', 'description', 'query',)
  # list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
  # exclude= ('permissions',)
  # Allows django admin to duplicate record
  # save_as = True



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
admin.site.register(AssignmentPool, AssignmentPoolAdminForm)

admin.site.register(Qualification)
admin.site.register(Worker, WorkerAdminForm)

admin.site.register(QueryFilter)
admin.site.register(WorkerGroup)

admin.site.register(Exception)

admin.site.register(Assignment)
admin.site.register(WeekSchedule)

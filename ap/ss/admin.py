from django.contrib import admin

#enable manage services in admin panel#

from ss.models import *
admin.site.register(Instance)
admin.site.register(WorkerGroup)
admin.site.register(ExceptionRequest)
admin.site.register(Filters)

from django.contrib import admin
from .models import Badge, BadgePrintSettings
from solo.admin import SingletonModelAdmin

admin.site.register(Badge)

admin.site.register(BadgePrintSettings, SingletonModelAdmin)
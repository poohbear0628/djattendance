# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from graduation.models import Testimony, Consideration, Outline, Website, Misc, GradAdmin

# Register your models here.
admin.site.register(Testimony)
admin.site.register(Consideration)
admin.site.register(Outline)
admin.site.register(Website)
admin.site.register(Misc)
admin.site.register(GradAdmin)

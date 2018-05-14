# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import GospelTrip, Section, Instruction, Question, Answer
# Register your models here.

admin.site.register(GospelTrip)
admin.site.register(Section)
admin.site.register(Instruction)
admin.site.register(Question)
admin.site.register(Answer)


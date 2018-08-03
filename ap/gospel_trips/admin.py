# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Answer, AnswerChoice, GospelTrip, Question, Section

admin.site.register(GospelTrip)
admin.site.register(Section)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(AnswerChoice)

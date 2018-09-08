# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import (Answer, AnswerChoice, GospelTrip, NonTrainee, Question,
                     Section)

admin.site.register(GospelTrip)
admin.site.register(Section)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(AnswerChoice)
admin.site.register(NonTrainee)

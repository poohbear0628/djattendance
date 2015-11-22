from django.contrib import admin
from exams.models import Exam, Section, ExamInstance
from django.forms import Textarea
from django.db import models

admin.site.register(Exam)
admin.site.register(Section)
admin.site.register(ExamInstance)
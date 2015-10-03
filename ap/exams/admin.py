from django.contrib import admin
from exams.models import ExamTemplateDescriptor, ExamTemplateSections, Exam
from django.forms import Textarea
from django.db import models

admin.site.register(ExamTemplateDescriptor)
admin.site.register(ExamTemplateSections)
admin.site.register(Exam)
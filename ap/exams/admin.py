from django.contrib import admin
from exams.models import Exam, Section, Session
from django.forms import Textarea
from django.db import models


class ExamAdmin(admin.ModelAdmin):
  readonly_fields = ('total_score', 'section_count',)
  filter = ('training_class', 'term', 'category', 'is_open')
  list_display = ('__unicode__', 'term', 'category', 'is_open', 'duration', 'section_count')


class SessionAdmin(admin.ModelAdmin):
  list_display = ('trainee', 'exam', 'is_submitted_online', 'is_complete', 'is_graded', 'retake_number', 'grade')

admin.site.register(Exam, ExamAdmin)
admin.site.register(Section)
admin.site.register(Session, SessionAdmin)

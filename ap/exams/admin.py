from django.contrib import admin
from exams.models import Exam, Section, Session, Makeup, Responses
from django.forms import Textarea
from django.db import models


class ExamAdmin(admin.ModelAdmin):
  readonly_fields = ('total_score', 'section_count',)
  filter = ('training_class', 'term', 'category', 'is_exam_open', 'is_graded_open')
  list_display = ('__unicode__', 'term', 'category', 'is_exam_open', 'is_graded_open', 'duration', 'section_count')


class ResponsesAdmin(admin.ModelAdmin):
  filter = ('session', 'section')
  list_display = ('pk', 'session', 'section', 'score', 'comments')


class ResponsesInline(admin.StackedInline):
  model = Responses
  extra = 0
  suit_classes = 'suit-tab suit-tab-responses'
  readonly_fields = ('section', )
  fields = ('section', 'score', ('responses', 'comments'), )


class SessionAdmin(admin.ModelAdmin):
  list_display = ('trainee', 'exam', 'is_submitted_online', 'is_graded', 'grade', 'time_started', 'time_finalized')
  fieldsets = (
      (None, {
          'classes': ('suit-tab', 'suit-tab-general',),
          'fields': ('trainee', 'exam', 'is_submitted_online', 'is_graded', 'time_finalized', 'grade')
      }),
  )
  suit_form_tabs = (('general', 'Session'),
                    ('responses', 'Reponses'))
  inlines = (ResponsesInline, )

admin.site.register(Exam, ExamAdmin)
admin.site.register(Section)
admin.site.register(Session, SessionAdmin)
admin.site.register(Responses, ResponsesAdmin)
admin.site.register(Makeup)

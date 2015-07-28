from django.contrib import admin
from exams.models import ExamTemplateDescriptor, ExamTemplateSections
# from exams.models import ExamTemplate, Exam, TextQuestion, TextResponse
from django.forms import Textarea
from django.db import models

# admin.site.register(TextQuestion)
# admin.site.register(TextResponse)

# class TextQuestionInline(admin.StackedInline):
#     model = TextQuestion
#     extra = 1

# class TextResponseInline(admin.StackedInline):
# 	model = TextResponse
# 	formfield_overrides = { models.CharField: {'widget': Textarea(
# 	                   attrs={'rows': 10,
# 	                          'cols': 70})}}

# class ExamTemplateAdmin(admin.ModelAdmin):
#     inlines = [TextQuestionInline]

# class ExamAdmin(admin.ModelAdmin):
# 	inlines = [TextResponseInline]

admin.site.register(ExamTemplateDescriptor)
admin.site.register(ExamTemplateSections)
from django.contrib import admin
from django import forms
from .models import HCSurvey, HCRecommendation, HCTraineeComment


class HCTraineeCommentInline(admin.TabularInline):
  model = HCTraineeComment


class HCSurveyAdmin(admin.ModelAdmin):
  inlines = [
    HCTraineeCommentInline,
  ]


admin.site.register(HCRecommendation)
admin.site.register(HCSurvey, HCSurveyAdmin)

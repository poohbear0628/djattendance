from django.contrib import admin
from .models import HCSurvey, HCRecommendation, HCTraineeComment, HCSurveyAdmin


class HCTraineeCommentInline(admin.TabularInline):
  model = HCTraineeComment


class HCSurveyInline(admin.ModelAdmin):
  inlines = [
    HCTraineeCommentInline,
  ]


admin.site.register(HCRecommendation)
admin.site.register(HCSurveyAdmin)
admin.site.register(HCSurvey, HCSurveyInline)

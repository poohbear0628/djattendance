from django.contrib import admin
from .models import HCSurvey, HCGeneralComment, HCTraineeComment, HCRecommendation

admin.site.register(HCSurvey)
admin.site.register(HCGeneralComment)
admin.site.register(HCTraineeComment)
admin.site.register(HCRecommendation)
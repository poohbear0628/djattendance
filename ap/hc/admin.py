from django.contrib import admin
from django import forms
from .models import HCSurvey, HCRecommendation

admin.site.register(HCSurvey)
admin.site.register(HCRecommendation)

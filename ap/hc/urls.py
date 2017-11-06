from django.conf.urls import url
from hc import views

app_name = 'hc'

urlpatterns = [
  url(r'hc_survey/$', views.create_hc_survey, name='hc_survey'),
  url(r'hc_recommendation/$', views.HCRecommendationCreate.as_view(), name='hc_recommendation'),
]

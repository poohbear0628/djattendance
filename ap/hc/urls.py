from django.conf.urls import url

from hc import views

urlpatterns = [
  url(r'^hc_survey/$', views.create_hc_survey, name='hc-survey'),
]

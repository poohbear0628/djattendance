from django.conf.urls import url

from . import views

app_name = 'audio'

urlpatterns = [
  url(r'^list/$', views.AudioHome.as_view(), name='audio-home'),
  url(r'^list/(?P<week>\d+)$', views.AudioHome.as_view(), name='audio-home-week'),
]

from django.conf.urls import url

from . import views

app_name = 'audio'

urlpatterns = [
  url(r'^list/$', views.AudioHome.as_view(), name='audio-home'),
  url(r'^list/(?P<week>\d+)$', views.AudioHome.as_view(), name='audio-home-week'),
  url(r'^request/$', views.AudioRequestCreate.as_view(), name='audio-request'),
  url(r'^update/(?P<pk>\d+)$', views.AudioRequestUpdate.as_view(), name='audio-update'),
]

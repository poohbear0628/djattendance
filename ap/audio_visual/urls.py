from django.conf.urls import url

from . import views

app_name = 'audio_visual'

urlpatterns = [
  url(r'^list/$', views.AVHome.as_view(), name='av-home'),
  url(r'^list/(?P<week>\d+)$', views.AVHome.as_view(), name='av-home-week'),
]

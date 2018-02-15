from django.conf.urls import url

from . import views

app_name = 'audio'

urlpatterns = [
    url(r'^list/$', views.AudioHome.as_view(), name='audio-home'),
    url(r'^upload/$', views.AudioCreate.as_view(), name='audio-upload'),
    url(r'^ta-list/$', views.TAAudioHome.as_view(), name='ta-audio-home'),
    url(r'^list/(?P<week>\d+)$', views.AudioHome.as_view(), name='audio-home-week'),
    url(r'^request/$', views.AudioRequestCreate.as_view(), name='audio-request'),
    url(r'^update/(?P<pk>\d+)$', views.AudioRequestUpdate.as_view(), name='audio-update'),
    url(r'^(?P<status>[APFDS])/(?P<id>\d+)$', views.modify_status, name='modify-status'),
    url(r'^ta-comment/(?P<pk>\d+)$', views.TAComment.as_view(), name='ta-comment'),
]

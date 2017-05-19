from django.conf.urls import url

from leaveslips import views

urlpatterns = [
    url(r'(?P<classname>individual|group)/(?P<status>[APFDS])/(?P<id>\d+)$', views.modify_status, name='modify-status'),
]

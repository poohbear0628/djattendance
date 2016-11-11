from django.conf.urls import url

from announcements import views

app_name = 'announcements'

urlpatterns = [
    url(r'create/$', views.AnnouncementRequest.as_view(), name='announcement-request')
]

from django.conf.urls import url

from announcements import views

app_name = 'announcements'

urlpatterns = [
    url(r'^detail/(?P<pk>\d+)$', views.AnnouncementDetail.as_view(), name='announcement-detail'),
    url(r'^create/$', views.AnnouncementRequest.as_view(), name='announcement-request'),
    url(r'^$', views.AnnouncementRequestList.as_view(), name='announcement-request-list')
]

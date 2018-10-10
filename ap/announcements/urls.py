from django.conf.urls import url

from announcements import views

app_name = 'announcements'

urlpatterns = [
    url(r'^detail/(?P<pk>\d+)$', views.AnnouncementDetail.as_view(), name='announcement-detail'),
    url(r'^create/$', views.AnnouncementRequest.as_view(), name='announcement-request'),
    url(r'^(?P<status>[APFDS])/(?P<id>\d+)$', views.modify_status, name='modify-status'),
    url(r'^delete/(?P<pk>\d+)$', views.AnnouncementDelete.as_view(), name='announcement-delete'),
    url(r'^update/(?P<pk>\d+)$', views.AnnouncementUpdate.as_view(), name='announcement-update'),
    url(r'^$', views.AnnouncementRequestList.as_view(), name='announcement-request-list'),
    url(r'^announcements-list/$', views.AnnouncementList.as_view(), name='announcement-list'),
    url(r'^announcements-list/(?P<date>\d{2}-\d{2}-\d{4})$', views.AnnouncementList.as_view()),
    url(r'^mark-read/(?P<id>\d+)$', views.mark_read, name='mark-read'),
    url(r'^announcements-read/$', views.AnnouncementsRead.as_view(), name='announcements-read')
]

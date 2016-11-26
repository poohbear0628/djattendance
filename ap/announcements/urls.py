from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy

from announcements import views

app_name = 'announcements'

urlpatterns = [
    url(r'^detail/(?P<pk>\d+)$', views.AnnouncementDetail.as_view(), name='announcement-detail'),
    url(r'^create/$', views.AnnouncementRequest.as_view(), name='announcement-request'),
    url(r'^(?P<status>[APFDS])/(?P<id>\d+)$', views.modify_status, name='modify-status'),
    url(r'^delete/(?P<pk>\d+)$', views.AnnouncementDelete.as_view(success_url=reverse_lazy('announcements:announcement-request-list')), name='announcement-delete'),
    url(r'^update/(?P<pk>\d+)$', views.AnnouncementUpdate.as_view(), name='announcement-update'),
    url(r'^$', views.AnnouncementRequestList.as_view(), name='announcement-request-list')
]

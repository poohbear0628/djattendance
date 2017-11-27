from django.conf.urls import url
from django.conf import settings

from schedules import views

urlpatterns = [
  url(r'event/(?P<pk>\d+)/$', views.EventDetail.as_view(), name='event-detail'),
  url(r'event/(?P<pk>\d+)/delete/$', views.EventDelete.as_view(), name='event-delete'),
  url(r'event/(?P<term>(Fa|Sp)\d{2})/$', views.TermEvents.as_view(), name='term-events'),
]

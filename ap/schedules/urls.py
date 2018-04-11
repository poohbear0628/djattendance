from django.conf.urls import url

from schedules import views

urlpatterns = [
    url(r'event/(?P<pk>\d+)/$', views.EventDetail.as_view(), name='event-detail'),
    url(r'event/(?P<pk>\d+)/delete/$', views.EventDelete.as_view(), name='event-delete'),
    url(r'event/(?P<term>(Fa|Sp)\d{2})/$', views.TermEvents.as_view(), name='term-events'),
    url(r'assign_schedules_to_trainees/$', views.assign_trainees_to_schedules, name='assign-trainees'),
]

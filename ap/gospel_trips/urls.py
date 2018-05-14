from django.conf.urls import url

from gospel_trips import views

urlpatterns = [
  url(r'^admin/$', views.GospelTripView.as_view(), name='admin-create'),
  url(r'^admin/(?P<pk>\d+)$', views.gospel_trip_admin_update, name='admin-update'),
  url(r'^trip/(?P<pk>\d+)$', views.gospel_trip_trainee, name='gospel-trip'),
]

from django.conf.urls import url

from gospel_trips import views

urlpatterns = [
  url(r'^admin/$', views.GospelTripView.as_view(), name='admin-create'),
  url(r'^admin/(?P<pk>\d+)$', views.gospel_trip_admin_update, name='admin-update'),
  url(r'^trip/(?P<pk>\d+)$', views.gospel_trip_trainee, name='gospel-trip'),
  url(r'^report/(?P<pk>\d+)$', views.GospelTripResponseView.as_view(), name='response-report'),
  url(r'^admin/(?P<pk>\d+)/destinations$', views.DestinationEditorView.as_view(), name='destination-edtior'),
  url(r'^admin/(?P<pk>\d+)/destinations$', views.DestinationEditorView.as_view(), name='destination-edtior'),
  url(r'^admin/(?P<pk>\d+)/destinations/add$', views.destination_add, name='destination-add'),
  url(r'^admin/destinations/remove$', views.destination_remove, name='destination-remove'),
  url(r'^admin/destinations/edit$', views.destination_edit, name='destination-edit'),
]

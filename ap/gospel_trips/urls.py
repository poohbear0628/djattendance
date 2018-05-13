from django.conf.urls import url

from gospel_trips import views

urlpatterns = [
  url(r'^admin/(?P<pk>\d+)$', views.gospel_trip_admin_update, name='admin-update'),
  url(r'^admin/$', views.GospelTripAdminView.as_view(), name='admin-create'),
]

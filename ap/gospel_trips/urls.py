from django.conf.urls import url

from gospel_trips import views

urlpatterns = [
  url(r'^create/(?P<pk>\d+)$', views.create_gospel_trip, name='gospel-trip-create'),
]
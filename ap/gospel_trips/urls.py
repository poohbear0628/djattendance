from django.conf.urls import url

from gospel_trips import views

urlpatterns = [
  url(r'^create$', views.create_gospel_trip, name='gospel-trip-create'),
]

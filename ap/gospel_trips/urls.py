from django.conf.urls import url

from gospel_trips import views

urlpatterns = [
  url(r'^admin$', views.GospelTripAdminView.as_view(), name='gospel-trips-admin'),
]

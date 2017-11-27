from django.conf.urls import url

from gospel_trips import views

urlpatterns = [
  url(r'^gospel_admin$', views.create_survey, name='gospel-admin'),
]

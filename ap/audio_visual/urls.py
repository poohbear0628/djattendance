from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.AVHome.as_view(), name='av-home'),
]

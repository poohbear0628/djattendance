from django.conf.urls import url
from classes import views
from classes.models import ELECTIVES

app_name = 'classes'

urlpatterns = [
  url(r'^$', views.class_files, name='index'),
  url(r'^upload$', views.upload, name='upload'),
  url(r'^(?P<classname>' + ELECTIVES + ')$', views.class_files, name='classfiles'),
  url(r'^delete/(?P<pk>\d+)$', views.delete_file, name='delete-file')
]

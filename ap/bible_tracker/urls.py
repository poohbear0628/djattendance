from django.conf.urls import url

from bible_tracker import views

app_name = 'bible_tracker'

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^updateBooks$', views.updateBooks, name='updateBooks'),
  url(r'^changeWeek/$', views.changeWeek, name='changeWeek'),
  url(r'^updateStatus/$', views.updateStatus, name='updateStatus'),
  url(r'^finalizeStatus/$', views.finalizeStatus, name='finalizeStatus'),
  url(r'^report/$', views.report, name='report'),
]

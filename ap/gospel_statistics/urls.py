from django.conf.urls import url

from gospel_statistics import views

urlpatterns = [
  url(r'^$', views.GospelStatisticsView, name='gospel-statistics-view'),
  url(r'^ta$', views.TAGospelStatisticsView, name='ta-gospel-statistics-view'),
  url(r'^save$', views.GospelStatisticsSave, name='gospel-statistics-save'),
  url(r'^weekly_statistics$', views.weekly_statistics, name='weekly-statistics'),
  url(r'^new_pair$', views.new_pair, name='new-pair'),
]

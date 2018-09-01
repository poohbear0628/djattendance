from django.conf.urls import url

from gospel_statistics import views

urlpatterns = [
  url(r'^$', views.GospelStatisticsView.as_view(), name='gospel-statistics-view'),
  url(r'^ta$', views.TAGospelStatisticsView, name='ta-gospel-statistics-view'),
]

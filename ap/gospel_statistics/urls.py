from django.conf.urls import url

from gospel_statistics import views

urlpatterns = [
  url(r'^$', views.GospelStatisticsView.as_view(), name='gospel-statistics-view'),
  url(r'^new_pair/$', views.NewGospelPairView.as_view(), name='new-pair'),
  url(r'^delete$', views.delete_pair, name='delete-pair'),
  #Change following urls
  url(r'^ta$', views.TAGospelStatisticsView, name='ta-gospel-statistics-view'),
]

from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
	url(r'^$', views.ClassnotesListView.as_view(), name='classnotes-list'),
	url(r'^/create/$', views.ClassnotesCreateView.as_view(),
		name='classnotes-create'),
)
from django.conf.urls import url
from form_manager import views

urlpatterns = [
  url(r'form/(?P<form_slug>[-\w]+)$', views.ViewFormView.as_view(), name='form_viewer_base'),
  url(r'^$', views.FormManagerView.as_view(), name='form_manager_base'),
]

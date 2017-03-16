from django.conf.urls import url

from house_requests import views

app_name = 'house_requests'

urlpatterns = [
  url(r'^maintenance_list/$', views.MaintenanceRequestList.as_view(), name='maintenance-list'),
  url(r'^maintenance_request/$', views.MaintenanceRequestCreate.as_view(), name='maintenance-request'),
  url(r'^maintenance_update/(?P<pk>\d+)$', views.MaintenanceRequestUpdate.as_view(), name='maintenance-update'),
  url(r'^linens_list/$', views.LinensRequestList.as_view(), name='linens-list'),
  url(r'^linens_request/$', views.LinensRequestCreate.as_view(), name='linens-request'),
  url(r'^linens_update/(?P<pk>\d+)$', views.LinensRequestUpdate.as_view(), name='linens-update'),
  url(r'^framing_list/$', views.FramingRequestList.as_view(), name='framing-list'),
  url(r'^framing_request/$', views.FramingRequestCreate.as_view(), name='framing-request'),
  url(r'^framing_update/(?P<pk>\d+)$', views.FramingRequestUpdate.as_view(), name='framing-update'),

  url(r'^house_requests/$', views.NewRequestPage, name='house_requests'),
]

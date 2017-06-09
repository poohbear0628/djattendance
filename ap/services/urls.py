from django.conf.urls import patterns,url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns(
  '',
  url(r'^$', views.services_view, name='services_view'),
  url(r'^assign$', views.services_view, {'run_assign': True}, name='services_assign_view'),
  url(r'^generate_leaveslips$', views.services_view, {'generate_leaveslips': True}, name='services_generate_leaveslips'),
  url(r'^print_report$', views.ServiceReportView.as_view(), name='services_print_report'),
  url(r'^generate_report$', views.generate_report, name='services_generate_report')
)

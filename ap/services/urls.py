from django.conf.urls import patterns,url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns(
    '',
    url(r'^$', views.services_view, name='services_view'),
    url(r'^assign$', views.services_view, {'run_assign': True}, name='services_assign_view'),
    url(r'^generate_leaveslips$', views.services_view, {'generate_leaveslips': True}, name='services_generate_leaveslips'),
)

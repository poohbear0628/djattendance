from django.conf.urls import patterns,url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns(
    '',
    url(r'^$', views.services_view, name='services_view'),
    url(r'^assign$', views.services_view, {'run_assign': True}, name='services_assign_view'),
    # url(r'manage/$', views.ExamTemplateListView.as_view(), {'manage': True}, name='manage'),
    # url(r'^print/$', 'badges.views.badgeprintout', name='badges_print'),
)

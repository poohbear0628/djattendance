from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    # url(r'^$', views.___, name='home'),
    # url(r'^template/create$', views.TemplateCreate.as_view(), name='template_create'),
    # url(r'^template/(?P<pk>\d+)$', views.TemplateDetail.as_view(), name='template_detail'),
    # url(r'^template/edit/(?P<pk>\d+)$', views.TemplateEdit.as_view(), name='template-edit'),
    # url(r'^chart/create$', views.___, name='chart-create'),
    # url(r'^chart/(?P<pk>\d+)$', views.___, name='chart-view'),
    # url(r'^chart/edit/(?P<pk>\d+)$', views.___, name='chart-edt'),
    url(r'^chart/create$', views.ChartCreateView.as_view(), name='chart_create'),
)

from django.conf.urls import patterns, url
from exams import views


urlpatterns = patterns(
    '',
    url(r'^$', views.ExamTemplateListView.as_view(), name='list'),
    url(r'new/$', views.ExamCreateView.as_view(), name='submit'),
    url(r'^(?P<pk>\d+)/edit$', views.ExamEditView.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/take$', views.TakeExamView.as_view(), name='take'),
    url(r'^(?P<pk>\d+)/grade$', views.GradeExamView.as_view(), name='grade'),
    url(r'^(?P<pk>\d+)/grades$', views.SingleExamGradesListView.as_view(), name='grades'),
    url(r'^(?P<pk>\d+)/overview$', views.GenerateOverview.as_view(), name='overview'),
    url(r'report/(?P<pk>\d*)$', views.GenerateGradeReports.as_view(), name='report'),
    url(r'report/$', views.GenerateGradeReports.as_view(), name='report-all')
)
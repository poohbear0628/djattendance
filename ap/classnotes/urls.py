from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.ClassnotesListView.as_view(), name='classnotes_list'),
  url(r'^classnotes-assign$', views.ClassnotesAssignView.as_view(), name='classnotes_assign'),
  url(r'^classnotes-report$', views.ClassnotesReportView.as_view(), name='classnotes_report'),
  url(r'^(?P<pk>\d+)/detail-classnotes$', views.ClassnotesUpdateView.as_view(), name='classnotes_detail'),
  url(r'^(?P<pk>\d+)/approve-classnotes$', views.ClassnotesApproveView.as_view(), name='classnotes_approve'),
]

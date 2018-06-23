from django.conf.urls import url

from semiannual import views
urlpatterns = [
  url(r'^rolls/$', views.SemiAnnualView.as_view(), name='semi-rolls'),
  url(r'^rolls/report/$', views.SemiAnnualStudyReport.as_view(), name='semi-study-report'),
] 
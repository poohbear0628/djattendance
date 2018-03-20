from django.conf.urls import url

from graduation import views

urlpatterns = [
    url(r'^grad_admin$', views.GradAdminView.as_view(), name='grad-admin'),
    url(r'testimony$', views.TestimonyView.as_view(), name='testimony-view'),
    url(r'consideration$', views.ConsiderationView.as_view(), name='consideration-view'),
    url(r'website$', views.WebsiteView.as_view(), name='website-view'),
    url(r'outline$', views.OutlineView.as_view(), name='outline-view'),
    url(r'misc$', views.MiscView.as_view(), name='misc-view'),
    url(r'misc_report$', views.MiscReport.as_view(), name='misc-report'),
]

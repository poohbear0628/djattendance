from django.conf.urls import patterns, url
from apimport import views


urlpatterns = patterns(
    '',
    url(r'term-details$', views.CreateTermView.as_view(), name='term_details')
)
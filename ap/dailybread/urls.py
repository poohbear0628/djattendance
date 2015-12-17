from django.conf.urls import patterns, url

from dailybread import views

urlpatterns = patterns('',
    url(r'today/$',
        views.TodaysPortion.as_view(),
        name='today'),
    url(r'submit/$',
        views.CreatePortion.as_view(),
        name='submit'),
    url(r'(?P<pk>\d+)/$',
        views.DetailPortion.as_view(),
        name='detail')
)

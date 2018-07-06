from django.conf.urls import url

from dailybread import views

app_name = 'dailybread'

urlpatterns = [
  url(r'today/$',
    views.TodaysPortion.as_view(),
    name='today'),
  url(r'submit/$',
    views.CreatePortion.as_view(),
    name='submit'),
  url(r'(?P<pk>\d+)/$',
    views.DetailPortion.as_view(),
    name='detail')
]

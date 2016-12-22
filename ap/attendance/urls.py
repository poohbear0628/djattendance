from django.conf.urls import patterns, url
from django.conf import settings

from attendance import views

urlpatterns = patterns('',
    url(r'submit/$', views.AttendancePersonal.as_view(), name='attendance-submit'),
    url(r'rolls/$', views.RollsView.as_view(), name='class-rolls'),
    url(r'rolls/meal/$', views.MealRollsView.as_view(), name='meal-rolls'),
    url(r'rolls/house/$', views.HouseRollsView.as_view(), name='house-rolls'),
    url(r'rolls/team/$', views.TeamRollsView.as_view(), name='team-rolls'),
    url(r'rolls/ypc/$', views.YPCRollsView.as_view(), name='ypc-rolls'),
    url(r'rolls/rfid/(?P<trainee_id>\d+)$', views.rfid_signin, name='rfid-rolls'),
#    url(r'attendance/submit/(?P<pk>\d+)/$', views.AttendanceSubmit.as_view(), name='attendance-submit'),
)

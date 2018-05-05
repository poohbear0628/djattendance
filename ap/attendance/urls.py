from django.conf.urls import url
from django.conf import settings

from attendance import views
urlpatterns = [
  url(r'^submit/$', views.AttendancePersonal.as_view(), name='attendance-submit'),
  url(r'^rolls/$', views.RollsView.as_view(), name='class-rolls'),
  url(r'^rolls/class/$', views.ClassRollsView.as_view(), name='class-table-rolls'),
  url(r'^rolls/meal/$', views.MealRollsView.as_view(), name='meal-rolls'),
  url(r'^rolls/study/$', views.StudyRollsView.as_view(), name='study-rolls'),
  url(r'^rolls/house/$', views.HouseRollsView.as_view(), name='house-rolls'),
  url(r'^rolls/team/$', views.TeamRollsView.as_view(), name='team-rolls'),
  url(r'^rolls/ypc/$', views.YPCRollsView.as_view(), name='ypc-rolls'),
  url(r'^rolls/rfid/$', views.RFIDRollsView.as_view(), name='rfid-rolls'),
  url(r'^api/rolls/finalize/$', views.finalize, name='finalize'),
  url(r'^api/rolls/rfid/(?P<trainee_id>\d+)$', views.rfid_signin),
  url(r'^api/rolls/rfid-finalize/(?P<event_id>\d+)/(?P<event_date>\d{4}-\d{2}-\d{2})$', views.rfid_finalize, name='rfid-roll-finalize'),
  url(r'^api/rolls/rfid-tardy/(?P<event_id>\d+)/(?P<event_date>\d{4}-\d{2}-\d{2})$', views.rfid_tardy, name='rfid-roll-tardy'),
  url(r'^rolls/audit/$', views.AuditRollsView.as_view(), name='audit-rolls'),
]

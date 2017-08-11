from django.conf.urls import url

from room_reservations import views

urlpatterns = [
    url(r'ta$', views.TARoomReservationList.as_view(), name='ta-room-reservation-list'),
    url(r'update/(?P<pk>\d+)$', views.RoomReservationUpdate.as_view(), name='room-reservation-update'),
    url(r'submit/$', views.RoomReservationSubmit.as_view(), name='room-reservation-submit'),
    url(r'(?P<status>[ADF])/(?P<id>\d+)$', views.reservation_modify_status, name='reservation-modify-status'),
    url(r'schedule$', views.RoomReservationSchedule.as_view(), name='room-reservation-schedule'),
]

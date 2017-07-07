from django.conf.urls import url

from room_reservations import views

urlpatterns = [
        url(r'update/(?P<pk>\d+)$', views.RoomReservationUpdate.as_view(), name='room-reservation-update'),
        url(r'reserve/(?P<pk>\d+)$', views.RoomReservationSubmit.as_view(), name='room-reservation-reserve'),
        url(r'submit/$', views.RoomReservationSubmit.as_view(), name='room-reservation-submit'),
    ]

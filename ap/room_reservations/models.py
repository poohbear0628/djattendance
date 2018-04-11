from datetime import datetime

from django.db import models
from django.core.urlresolvers import reverse

from rooms.models import Room
from aputils.utils import RequestMixin
from accounts.models import User

""" ROOM RESERVATIONS models.py

The ROOMS RESERVATIONS app represents reservations that are made for the various
locations of the training. They are made by trainees or TA's and approved by
TA's. Both trainees and TA's use the reservation schedule generated by this app.

Data Models:
  - RoomReservation: a reservation for a particular room at a given time.

"""


class RoomReservation(models.Model, RequestMixin):

  RES_STATUS = (
      ('P', 'Pending'),
      ('A', 'Approved'),
      ('D', 'Denied'),
      ('F', 'Marked for Fellowship'),
  )

  RES_FREQ = (
      ('Once', 'reserve once'),
      ('Term', 'reserve for the entire term'),
  )

  requester = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

  # time of submission
  submitted = models.DateTimeField(auto_now_add=True)

  # time of last update
  last_modified = models.DateTimeField(auto_now=True)

  # time of approved/denied
  finalized = models.DateTimeField(blank=True, null=True)

  # description of the group using the room
  group = models.CharField(max_length=15)

  # date requesting
  date = models.DateField()

  # start time
  start = models.TimeField()

  # end time
  end = models.TimeField()

  # room being requested
  room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)

  # size of group
  group_size = models.IntegerField(default=10)

  # frequency - once or recurring
  frequency = models.CharField(max_length=30, choices=RES_FREQ, default='Once')

  # reservation approval status
  status = models.CharField(max_length=2, choices=RES_STATUS, default='P')

  # reason for reservation
  reason = models.CharField(max_length=100)

  def __init__(self, *args, **kwargs):
    super(RoomReservation, self).__init__(*args, **kwargs)
    self.old_status = self.status

  def save(self, *args, **kwargs):
    # records the datetime when reservation is approved or denied
    if self.status in ['A', 'D'] and self.old_status in ['P', 'F', 'S']:
      self.finalized = datetime.now()
    super(RoomReservation, self).save(*args, **kwargs)
    self.old_status = self.status

  def __unicode__(self):
    return "[%s] %s - %s" % (self.submitted.strftime('%m/%d'), self.room, self.requester)

  def get_absolute_url(self):
    return reverse('room_reservations:room-reservation-update', kwargs={'pk': self.id})

  def get_update_url(self):
    return reverse('room_reservations:room-reservation-update', kwargs={'pk': self.id})

  def get_delete_url(self):
    return reverse('room_reservations:room-reservation-delete', kwargs={'pk': self.id})

  def get_trainee_requester(self):
    return self.requester

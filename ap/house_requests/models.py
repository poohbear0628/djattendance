from django.db import models

from houses.models import House
from accounts.models import Trainee

class HouseRequest(models.Model):
  class Meta:
    abstract = True

  STATUS = (
    ('A', 'Approved'),
    ('P', 'Pending'),
    ('F', 'Fellowship'),
    ('D', 'Denied'),
  )

  status = models.CharField(max_length=1, choices=STATUS, default='P')
  date_requested = models.DateTimeField(auto_now_add=True)
  trainee_author = models.ForeignKey(Trainee, null=True)
  TA_comments = models.TextField(null=True, blank=True)

  def get_category(self):
    return self.type
  def get_status(self):
    return self.get_status_display()
  def get_date_created(self):
    return self.date_requested
  def get_trainee_requester(self):
    return self.trainee_author

class MaintenanceRequest(HouseRequest):
  type = 'Maintenance'
  description = models.TextField()
  house = models.ForeignKey(House, related_name='maintenance_requests')

class LinensRequest(HouseRequest):
  type = 'Linens'
  item = models.TextField()
  quantity = models.PositiveSmallIntegerField()
  reason = models.TextField()
  house = models.ForeignKey(House, related_name='linens_requests')

class FramingRequest(HouseRequest):
  type = 'Framing'
  location = models.TextField()
  frame = models.TextField()
  house = models.ForeignKey(House, related_name='framing_requests')

from django.db import models
from django.core.urlresolvers import reverse

from houses.models import House
from accounts.models import Trainee

class HouseRequest(models.Model):
  class Meta:
    abstract = True

  STATUS = (
    ('C', 'Completed'),
    ('P', 'Pending'),
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

  @staticmethod
  def get_ta_button_template():
    return 'request_list/ta_buttons.html'
  @staticmethod
  def get_button_template():
    return 'request_list/buttons.html'

class MaintenanceRequest(HouseRequest, models.Model):
  type = 'Maintenance'
  description = models.TextField()
  house = models.ForeignKey(House, related_name='maintenance_requests')

  @staticmethod
  def get_create_url():
    return reverse('house_requests:maintenance-request')
  def get_update_url(self):
    return reverse('house_requests:maintenance-update', kwargs={'pk': self.id})
  @staticmethod
  def get_detail_template():
    return 'maintenance/description.html'
  @staticmethod
  def get_table_template():
    return 'maintenance/table.html'

class LinensRequest(HouseRequest, models.Model):
  type = 'Linens'
  item = models.TextField()
  quantity = models.PositiveSmallIntegerField()
  reason = models.TextField()
  house = models.ForeignKey(House, related_name='linens_requests')

  @staticmethod
  def get_create_url():
    return reverse('house_requests:linens-request')
  def get_update_url(self):
    return reverse('house_requests:linens-update', kwargs={'pk': self.id})
  @staticmethod
  def get_detail_template():
    return 'linens/description.html'
  @staticmethod
  def get_table_template():
    return 'linens/table.html'

class FramingRequest(HouseRequest, models.Model):
  type = 'Framing'
  location = models.TextField()
  frame = models.TextField()
  house = models.ForeignKey(House, related_name='framing_requests')

  @staticmethod
  def get_create_url():
    return reverse('house_requests:framing-request')
  def get_update_url(self):
    return reverse('house_requests:framing-update', kwargs={'pk': self.id})
  @staticmethod
  def get_detail_template():
    return 'framing/description.html'
  @staticmethod
  def get_table_template():
    return 'framing/table.html'

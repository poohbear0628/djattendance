import datetime

from django.db import models
from django.db.models import Count, Q
from django.core.urlresolvers import reverse

from accounts.models import Trainee
from house_requests.models import RequestInterface

class Announcement(models.Model, RequestInterface):

  class Meta:
    verbose_name = "announcement"
    ordering = ['-announcement_date']

  ANNOUNCE_STATUS = (
    ('A', 'Approved'),
    ('P', 'Pending'),
    ('F', 'Fellowship'),
    ('D', 'Denied'),
  )

  ANNOUNCE_TYPE = (
    ('CLASS', 'In-class'),
    ('SERVE', 'On the server')
  )

  status = models.CharField(max_length=1, choices=ANNOUNCE_STATUS, default='P')
  type = models.CharField(max_length=5, choices=ANNOUNCE_TYPE, default='CLASS')

  date_requested = models.DateField(auto_now_add=True)
  trainee_author = models.ForeignKey(Trainee, null=True)
  TA_comments = models.TextField(null=True, blank=True)
  trainee_comments = models.TextField(null=True, blank=True)
  is_popup = models.BooleanField(default=False, blank=True)
  announcement = models.TextField()
  announcement_date = models.DateField()
  announcement_end_date = models.DateField(null=True, blank=True)
  trainees_show = models.ManyToManyField(Trainee, related_name="announcement_show", blank=True)
  trainees_read = models.ManyToManyField(Trainee, related_name="announcement_read", blank=True)

  def __unicode__(self):
    return '<Announcement %s ...> by trainee %s' % (self.announcement[:10], self.trainee_author)

  @staticmethod
  def announcements_for_today(trainee, is_popup=False):
    today = datetime.date.today()
    announcements = Announcement.objects \
      .annotate(num_trainees=Count('trainees_show')) \
      .filter(Q(type='SERVE',
        status='A',
        announcement_date__lte=today,
        announcement_end_date__gte=today,
        is_popup=is_popup
      ) & (Q(num_trainees=0) | Q(trainees_show=trainee))) \
      .exclude(trainees_read=trainee)
    return announcements

  @staticmethod
  def get_create_url():
    return reverse('announcements:announcement-request')

  def get_mark_read_url(self):
    return reverse('announcements:mark-read', kwargs={'id': self.id})

  def get_absolute_url(self):
    return reverse('announcements:announcement-detail', kwargs={'pk': self.id})

  def get_update_url(self):
    return reverse('announcements:announcement-update', kwargs={'pk': self.id})

  def get_ta_comments_url(self):
    return reverse('announcements:ta-comment', kwargs={'pk': self.id})

  @staticmethod
  def get_detail_template():
    return 'announcement_list/description.html'

  @staticmethod
  def get_button_template(isTA=False):
    return 'announcement_list/ta_buttons.html' if isTA else 'announcement_list/buttons.html'

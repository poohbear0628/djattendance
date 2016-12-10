from django.db import models
from django.core.urlresolvers import reverse

from accounts.models import Trainee

class Announcement(models.Model):

    class Meta:
        verbose_name = "announcement"

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
    trainee = models.ForeignKey(Trainee, null=True)
    TA_comments = models.TextField(null=True, blank=True)
    trainee_comments = models.TextField(null=True)
    is_popup = models.BooleanField(default=False, blank=True)
    announcement = models.TextField()
    announcement_date = models.DateField()
    announcement_end_date = models.DateField(null=True, blank=True)
    trainees = models.ManyToManyField(Trainee, related_name="announcement_disp", blank=True)
    trainees_read = models.ManyToManyField(Trainee, related_name="announcement_read", blank=True)

    def __unicode__(self):
        return '<Announcement %s ...> by trainee %s' % (self.announcement[:10], self.trainee)

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

from django.db import models

from worker import Worker
from service import Service
from terms.models import Term
from django.core.urlresolvers import reverse
""" SERVICE HOURS models.py

Self-attendance for designated hours.

Data Models:
  - ServiceAttendance: a weekly record of service attendance
  - ServiceRoll: individual service instance

"""
CHOICES = [(i, i) for i in range(20)]


class ServiceAttendance(models.Model):

  worker = models.ForeignKey(Worker, blank=True)  # change to worker

  designated_service = models.ForeignKey(Service)

  term = models.ForeignKey(Term, blank=True)

  week = models.IntegerField(default=0, choices=CHOICES)

  def get_absolute_url(self):
    return reverse('services:designated_service_hours', kwargs={'service_id': self.designated_service.id, 'week': self.week})


class ServiceRoll(models.Model):

  service_attendance = models.ForeignKey(ServiceAttendance, blank=True)

  start_datetime = models.DateTimeField(null=True, blank=True)

  end_datetime = models.DateTimeField(null=True, blank=True)

  task_performed = models.CharField(max_length=140, blank=True)

# -*- coding: utf-8 -*-

from accounts.models import Trainee
from django.contrib.postgres.fields import HStoreField
from django.core.urlresolvers import reverse
from django.db import models


class GospelTripAdmin(models.Model):
  name = models.CharField(max_length=40, blank=True)

  open_time = models.DateTimeField(blank=True)

  close_time = models.DateTimeField(blank=True)

  def get_absolute_url(self):
    return reverse('gospel_trips:admin-update', kwargs={'pk': self.id})


class GospelTrip(models.Model):
  trainee = models.ForeignKey(Trainee, on_delete=models.CASCADE)

  admin = models.ForeignKey(GospelTripAdmin)

  def get_absolute_url(self):
    return reverse('gospel_trips:gospel-trips', kwargs={'pk': self.id})


class Section(models.Model):
  admin = models.ForeignKey(GospelTripAdmin, on_delete=models.CASCADE)

  name = models.CharField(max_length=80, blank=True)

  index = models.SmallIntegerField(default=1)


class Instruction(models.Model):
  section = models.ForeignKey(Section, on_delete=models.CASCADE)

  name = models.CharField(max_length=80, blank=True)

  instruction = models.TextField(null=True, blank=True)

  index = models.SmallIntegerField(default=1)


class Question(models.Model):
  section = models.ForeignKey(Section, on_delete=models.CASCADE)

  instruction = models.TextField(null=True, blank=True)

  index = models.SmallIntegerField(default=1)


class Answer(models.Model):

  question = models.ForeignKey(Question, on_delete=models.CASCADE)

  gospel_trip = models.ForeignKey(GospelTrip)

  response = HStoreField(null=True)

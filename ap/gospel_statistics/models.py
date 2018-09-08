# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from accounts.models import Trainee

# Create your models here.
class GospelStat(models.Model):
  #Which trainees compose this gospel pair
  trainees = models.ManyToManyField(Trainee, related_name="gospel_statistics", blank=True)
  week = models.PositiveSmallIntegerField()
  tracts_distributed = models.PositiveSmallIntegerField()
  bibles_distributed = models.PositiveSmallIntegerField()
  contacted_30_sec = models.PositiveSmallIntegerField()
  led_to_pray = models.PositiveSmallIntegerField()
  baptized = models.PositiveSmallIntegerField()
  second_appointment = models.PositiveSmallIntegerField()
  regular_appointment = models.PositiveSmallIntegerField()
  minutes_on_gospel = models.PositiveSmallIntegerField()
  miniutes_in_appointment = models.PositiveSmallIntegerField()
  bible_study = models.PositiveSmallIntegerField()
  small_group = models.PositiveSmallIntegerField()

  #New students present at the district meeting
  district_meeting = models.PositiveSmallIntegerField()
  confernece = models.PositiveSmallIntegerField()

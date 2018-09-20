# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from accounts.models import Trainee

# Create your models here.
class GospelStat(models.Model):
  #Which trainees compose this gospel pair
  #trainees = models.ManyToManyField(Trainee, related_name="gospel_statistics", blank=True)
  week = models.PositiveSmallIntegerField()
  tracts_distributed = models.PositiveSmallIntegerField()

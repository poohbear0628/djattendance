# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from accounts.models import Trainee


class GospelTrip(models.Model):
  name = models.CharField(max_length=40, blank=True)

  def get_absolute_url(self):
    return reverse('gospel_trips:gospel-trip-create', kwargs={'pk': self.id})


class Section(models.Model):
  gospel_trip = models.ForeignKey(GospelTrip)

  name = models.CharField(max_length=80, blank=True)

  index = models.SmallIntegerField(default=1)


class Instruction(models.Model):
  section = models.ForeignKey(Section)

  name = models.CharField(max_length=80, blank=True)

  instruction = models.TextField(null=True, blank=True)

  index = models.SmallIntegerField(default=1)


class Question(models.Model):
  section = models.ForeignKey(Section)

  instruction = models.TextField(null=True, blank=True)

  ANSWER_TYPES = (
    ('C', 'choice'),  # single choice; select widget
    ('T', 'Text'),  # text input; textarea widget
  )
  answer_type = models.CharField(max_length=1, choices=ANSWER_TYPES, default='T', blank=True)

  index = models.SmallIntegerField(default=1)

  answer_choices = models.CharField(max_length=1000, blank=True)


class Answer(models.Model):

  question = models.ForeignKey(Question)

  trainee = models.ForeignKey(Trainee)

  response = models.CharField(max_length=1000, blank=True)

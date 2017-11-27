# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
from accounts.models import Trainee


class GospelTrip(models.Model):
  name = models.CharField(max_length=40, blank=True)


class Section(models.Model):
  gospel_trip = models.ForeignKey(GospelTrip)

  name = models.CharField(max_length=80, blank=True)

  index = models.SmallIntegerField(default=0)


class Instruction(models.Model):
  section = models.ForeignKey(Section)

  name = models.CharField(max_length=80, blank=True)

  instruction = HTMLField()

  index = models.SmallIntegerField(default=0)


class Question(models.Model):
  section = models.ForeignKey(Section)

  instruction = HTMLField()

  ANSWER_TYPES = (
    ('C', 'choice'),  # single choice; select widget
    ('T', 'Text'),  # text input; textarea widget
  )
  answer_type = models.CharField(max_length=1, choices=ANSWER_TYPES, default='T')

  index = models.SmallIntegerField(default=0)

  answer_choices = models.CharField(max_length=1000, blank=True)


class Answer(models.Model):

  question = models.ForeignKey(Question)

  trainee = models.ForeignKey(Trainee)

  response = models.CharField(max_length=1000, blank=True)

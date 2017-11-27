# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
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

  instruction = models.TextField()  # change this to an htmlfield

  index = models.SmallIntegerField(default=0)


class Question(models.Model):
  section = models.ForeignKey(Section)

  instruction = models.TextField()

  ANSWER_TYPES = (('S', 'Select'), ('T', 'Text'))
  answer_type = models.CharField(max_length=1, choices=ANSWER_TYPES, default='T')

  index = models.SmallIntegerField(default=0)

  answer_choices = models.CharField(max_length=1000, blank=True)


class Answer(models.Model):
  question = models.ForeignKey(Question)

  trainee = models.ForeignKey(Trainee)

  class Meta:
    abstract = True


class AnswerSelect(Answer):
  # This is a choicefield set on the modelform
  response = models.CharField(max_length='120', blank=True)


class AnswerText(Answer):
  response = models.CharField(max_length='120', blank=True)

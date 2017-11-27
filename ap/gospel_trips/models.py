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
  answer_type = models.CharField()  # choices
  index = models.SmallIntegerField(default=0)

# • GTAnswerSelect(GTAnswer):
# o Response: ChoiceField
# ♣ Initial: Choice=null
# ♣ Onsave: Choice = GTQuestion.AnswerChoice


class Answer(models.Model):
  question = models.ForeignKey(Question)
  trainee = models.ForeignKey(Trainee)

  class Meta:
    abstract = True


class AnswerSelect(Answer):
  response = models.CharField()  # choice


class AnswerText(Answer):
  response = models.CharField()

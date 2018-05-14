# -*- coding: utf-8 -*-

from accounts.models import Trainee
from django.contrib.postgres.fields import JSONField
from django.core.urlresolvers import reverse
from django.db import models


class GospelTrip(models.Model):
  name = models.CharField(max_length=40, blank=True)

  open_time = models.DateTimeField(blank=True)

  close_time = models.DateTimeField(blank=True)

  def get_absolute_url(self):
    return reverse('gospel_trips:admin-update', kwargs={'pk': self.id})

  def get_trainee_url(self):
    return reverse('gospel_trips:gospel-trips', kwargs={'pk': self.id})

  def get_report_url(self):
    return reverse('gospel_trips:response-report', kwargs={'pk', self.id})


class Section(models.Model):
  gospel_trip = models.ForeignKey(GospelTrip, on_delete=models.CASCADE)

  name = models.CharField(max_length=80, blank=True)

  order = models.SmallIntegerField(default=1)

  class Meta:
    order_with_respect_to = 'gospel_trip'


class Instruction(models.Model):
  section = models.ForeignKey(Section, on_delete=models.CASCADE)

  name = models.CharField(max_length=80, blank=True)

  instruction = models.TextField(null=True, blank=True)

  order = models.SmallIntegerField(default=1)

  class Meta:
    order_with_respect_to = 'section'


def default_answer_type():
  return {"type": 'text', 'choices': []}


HELP_TEXT = """
  Use the following format:<br>
  <ul>
    <li> {"type": "text", "choices": [])} </li>
    <li> {"type": "choice", "choices": ["Yes", "No"]} </li>
  </ul>
"""


class Question(models.Model):
  section = models.ForeignKey(Section, on_delete=models.CASCADE)

  instruction = models.TextField(null=True, blank=True)

  order = models.SmallIntegerField(default=1)

  answer_type = JSONField(null=True, blank=True, help_text=HELP_TEXT)

  class Meta:
    order_with_respect_to = 'section'


class Answer(models.Model):

  question = models.ForeignKey(Question, on_delete=models.CASCADE)

  gospel_trip = models.ForeignKey(GospelTrip)

  trainee = models.ForeignKey(Trainee, on_delete=models.CASCADE)

  response = models.TextField(null=True, blank=True)

  class Meta:
    order_with_respect_to = 'question'

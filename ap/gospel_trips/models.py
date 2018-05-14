# -*- coding: utf-8 -*-

from accounts.models import Trainee
from django.contrib.postgres.fields import JSONField
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.html import strip_tags


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

  def __unicode__(self):
    try:
      return "[%s]" % (self.name)
    except AttributeError as e:
      return str(self.id) + ": " + str(e)


class Section(models.Model):
  gospel_trip = models.ForeignKey(GospelTrip, on_delete=models.CASCADE)

  name = models.CharField(max_length=80, blank=True)

  order = models.SmallIntegerField(default=1)

  def __unicode__(self):
    try:
      return "%s - %s" % (self.gospel_trip, self.name)
    except AttributeError as e:
      return str(self.id) + ": " + str(e)

  class Meta:
    order_with_respect_to = 'gospel_trip'


class Instruction(models.Model):
  section = models.ForeignKey(Section, on_delete=models.CASCADE)

  name = models.CharField(max_length=80, blank=True)

  instruction = models.TextField(null=True, blank=True)

  order = models.SmallIntegerField(default=1)

  def __unicode__(self):
    try:
      return "[%s] - %s - %s" % (self.section.gospel_trip, self.section, self.name)
    except AttributeError as e:
      return str(self.id) + ": " + str(e)

  class Meta:
    order_with_respect_to = 'section'


def default_answer_type():
  return {"type": 'text', 'choices': []}


HELP_TEXT = """
  Use the following format:<br>
  <ul>
    <li> {"type": "text", "choices": []} </li>
    <li> {"type": "choice", "choices": ["Yes", "No"]} </li>
  </ul>
"""


class Question(models.Model):
  section = models.ForeignKey(Section, on_delete=models.CASCADE)

  instruction = models.TextField(null=True, blank=True)

  order = models.SmallIntegerField(default=1)

  answer_type = JSONField(null=True, blank=True, help_text=HELP_TEXT)

  def __unicode__(self):
    try:
      return "%s - %s" % (self.section, strip_tags(self.instruction)[:20])
    except AttributeError as e:
      return str(self.id) + ": " + str(e)

  class Meta:
    order_with_respect_to = 'section'


class Answer(models.Model):

  question = models.ForeignKey(Question, on_delete=models.CASCADE)

  gospel_trip = models.ForeignKey(GospelTrip)

  trainee = models.ForeignKey(Trainee, on_delete=models.CASCADE)

  response = models.TextField(null=True, blank=True)

  def __unicode__(self):
    try:
      return "%s - %s" % (self.question, self.trainee)
    except AttributeError as e:
      return str(self.id) + ": " + str(e)

  class Meta:
    order_with_respect_to = 'question'

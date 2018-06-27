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


class Destination(models.Model):
  name = models.CharField(max_length=250, blank=True)

  gospel_trip = models.ForeignKey(GospelTrip, on_delete=models.CASCADE)

  team_contact = models.ForeignKey(Trainee, null=True, related_name='team_contact')

  trainees = models.ManyToManyField(Trainee, related_name='destination')

  def set_team_contact(self, trainee, is_contact=True):
    if is_contact:
      self.team_contact = trainee
    else:
      if self.team_contact == trainee:
        self.team_contact = None
    self.save()

  def remove_trainee(self, trainee):
    self.trainees.remove(trainee)
    self.set_team_contact(trainee, False)

  def __unicode__(self):
    try:
      return "%s - %s" % (self.gospel_trip, self.name)
    except AttributeError as e:
      return str(self.id) + ": " + str(e)


class Section(models.Model):
  gospel_trip = models.ForeignKey(GospelTrip, on_delete=models.CASCADE)

  name = models.CharField(max_length=80, blank=True)

  def __unicode__(self):
    try:
      return "%s - %s" % (self.gospel_trip, self.name)
    except AttributeError as e:
      return str(self.id) + ": " + str(e)

  class Meta:
    order_with_respect_to = 'gospel_trip'  # access with _order


class Instruction(models.Model):
  section = models.ForeignKey(Section, on_delete=models.CASCADE)

  name = models.CharField(max_length=80, blank=True)

  instruction = models.TextField(null=True, blank=True)

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
  Use the following format (You may copy and paste):<br>
  <ul>
    <li> {"type": "text"} </li>
    <li> {"type": "choice", "choices": ["Yes", "No"], "required": "True"} </li>
    <li> {"type": "destinations"} </li>
  </ul>
"""


class Question(models.Model):
  section = models.ForeignKey(Section, on_delete=models.CASCADE)

  instruction = models.TextField(null=True, blank=True)

  answer_type = JSONField(null=True, blank=True, help_text=HELP_TEXT)

  def __unicode__(self):
    try:
      return "%s" % (strip_tags(self.instruction))
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


class LocalImage(models.Model):
  file = models.ImageField(upload_to='gospel_trips/uploaded_images/')

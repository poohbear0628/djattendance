from django.db import models
from terms.models import Term
from schedules.models import Event


"""" CLASSES models.py

This is a utility module that will be used by other apps, such as class notes or
class syllabi, A/V requests, etc.

It reprents FTTA classes such as God's Economy, Wed night ministry meeting, or
Greek II and Character.

Each instance of a Class object represents a class *for a given term*

Data Models:
    - Class: a class in the FTTA

"""


class ClassManager(models.Manager):

  def get_queryset(self):
    return super(ClassManager, self).get_queryset().filter(type='C')


class Class(Event):
  class Meta:
    proxy = True
    verbose_name_plural = 'classes'

  def save(self, *args, **kwargs):
    self.type = 'C'
    print 'custom save', self
    super(Class, self).save(*args, **kwargs)

  objects = ClassManager()

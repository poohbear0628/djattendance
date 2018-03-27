from django.db import models
from accounts.models import User, Trainee
from localilties.models import Locality
from houses.models import House, Bunk
from terms.models import Term

""" shortterm models.py
This class represents short-term trainees.
"""

class ShortTermTrainee(User):

  visits = models.ManyToManyField('Visit')

class Visit(models.Model):
  """ a single short-term visit """

  application = models.ForeignKey('Application', on_delete=models.SET_NULL, null=True)

  term = models.ForeignKey(Term, on_delete=models.SET_NULL, null=True)

  arrivalDate = models.DateField()

  departureDate = models.DateField()

  mentor = models.ForeignKey(Trainee, on_delete=models.SET_NULL, null=True)

  house = models.ForeignKey(House, on_delete=models.SET_NULL, null=True)

  bunk = models.ForeignKey(Bunk, on_delete=models.SET_NULL, null=True)

class Application(models.Model):
  """ an application to short term at the FTTA """

  locality = models.ForeignKey(Locality, on_delete=models.SET_NULL, null=True)

  recommendation = models.TextField()

from django.db import models
from houses.models import House
from accounts.models import Trainee
from django.core.urlresolvers import reverse


class HCSurvey(models.Model):

  # many-to-one: The house (has many surveys) this survey concerns
  house = models.ForeignKey(House, null=True)

  # hc submitting the HCSurvey
  hc = models.ForeignKey(Trainee, null=True)

  # atmosphere of the house
  atmosphere = models.TextField(blank=True, null=True)

  # situations of the house
  situations = models.TextField(blank=True, null=True)

  # general comments concerning the house
  comment = models.TextField(blank=True, null=True)

  # period for HCSurvey
  PERIODS = (
    (0, 0), (1, 1), (2, 2), (3, 3), (4, 4),
    (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), )
  period = models.SmallIntegerField(blank=True, null=True, choices=PERIODS)

  def __unicode__(self):
    return "House Survey: " + self.house.name


class HCTraineeComment(models.Model):

  # the corresponding HC Survey
  hc_survey = models.ForeignKey(HCSurvey, null=True)

  # the (resident) trainee this comment concerns
  trainee = models.ForeignKey(Trainee, null=True)

  # the comment concerning the trainee
  assessment = models.TextField(blank=True, null=True)

  def __unicode__(self):
    return "Trainee Comment: " + self.trainee.full_name


class HCRecommendation(models.Model):

  # The recommendation concerning this house
  house = models.ForeignKey(House, null=True)

  # hc writing this recommendation
  hc = models.ForeignKey(Trainee, related_name='hc', null=True)

  # trainee recommended by hc for hc role
  recommended_hc = models.ForeignKey(Trainee, related_name='recommended_hc', null=True)

  # choice - yes or no
  CHOICE = (('YES', 'yes'), ('NO', 'no'))
  choice = models.CharField(max_length=3, choices=CHOICE, blank=True)

  # detailed recommendation for the chosen trainee
  recommendation = models.TextField(blank=True, null=True)

  def get_absolute_url(self):
    return reverse('hc:hc-recommendation-update', kwargs={'pk': self.id})

  def __unicode__(self):
    return "HC Rec.: " + self.house.name

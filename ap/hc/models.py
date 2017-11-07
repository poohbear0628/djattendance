from django.db import models
from django.contrib.postgres.fields import JSONField
from houses.models import House
from accounts.models import Trainee
from django.core.urlresolvers import reverse


# class HCTraineeComment(models.Model):

#   # the corresponding HC Survey
#   hc_survey = models.ForeignKey(HCSurvey)

#   # the (resident) trainee this comment concerns
#   trainee = models.ForeignKey(Trainee)

#   # the comment concerning the trainee
#   assessment = models.TextField(blank=True, null=True)


class HCSurvey(models.Model):

  # many-to-one: The house (has many surveys) this survey concerns
  house = models.ForeignKey(House)

  # hc submitting the HCSurvey
  hc = models.ForeignKey(Trainee)

  # atmosphere of the house
  atmosphere = models.TextField(blank=True, null=True)

  # situations of the house
  situations = models.TextField(blank=True, null=True)

  # general comments concerning the house
  comment = models.TextField(blank=True, null=True)

  trainee_comments = JSONField(default=list)

  def __unicode__(self):
    return "House Survey: " + self.house.name

class HCRecommendation(models.Model):

  # The recommendation concerning this house
  house = models.ForeignKey(House)

  # hc writing this recommendation
  hc = models.ForeignKey(Trainee, related_name='hc')

  # trainee recommended by hc for hc role
  choice = models.ForeignKey(Trainee, related_name='recommended_hc')

  # detailed recommendation for the chosen trainee
  recommendation = models.TextField(blank=True, null=True)

  SCALE = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))

  # the following fields are concerning the recommended trainee

  exercise_of_the_spirit = models.SmallIntegerField(blank=False, choices=SCALE)

  tidiness = models.SmallIntegerField(blank=False, choices=SCALE)

  punctuality = models.SmallIntegerField(blank=False, choices=SCALE)

  even_tempered = models.SmallIntegerField(blank=False, choices=SCALE)

  ability_to_shepherd = models.SmallIntegerField(blank=False, choices=SCALE)

  responsible = models.SmallIntegerField(blank=False, choices=SCALE)

  attitude = models.SmallIntegerField(blank=False, choices=SCALE)

  physical_endurance = models.SmallIntegerField(blank=False, choices=SCALE)

  average = models.SmallIntegerField()

  def get_average(self):

    total = self.exercise_of_the_spirit + self.tidiness + self.punctuality \
        + self.even_tempered + self.ability_to_shepherd + self.responsible \
        + self.attitude + self.physical_endurance

    return total / float(8)

  def get_absolute_url(self):
    return reverse('hc:hc_recommendation-update', kwargs={'pk': self.id})

  def __unicode__(self):
    return "HC Rec.: " + self.house.name

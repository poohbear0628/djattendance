from django.db import models
from houses.models import House
from accounts.models import Trainee


class HCSurvey(models.Model):

  # many-to-one: The house (has many surveys) this survey concerns
  house = models.ForeignKey(House)

  # hc submitting the HCSurvey
  hc = models.ForeignKey(Trainee)

  def __unicode__(self):
    return "House Survey: " + self.house.name


class HCGeneralComment(models.Model):

  # one-to-one: HCSurvey has one HCGenenralComment
  hc_survey = models.OneToOneField(HCSurvey, primary_key=True)

  # atmosphere of the house
  atmosphere = models.TextField(blank=True, null=True)

  # situations of the house
  situations = models.TextField(blank=True, null=True)

  # general comments concerning the house
  comment = models.TextField(blank=True, null=True)

  def __unicode__(self):
    return "HC General Comm.: " + self.hc_survey.house.name


class HCTraineeComment(models.Model):

  # many-to-one: the HCSurvey (has many comments) this comment belongs to
  hc_survey = models.ForeignKey(HCSurvey)

  # the (resident) trainee this comment concerns
  trainee = models.ForeignKey(Trainee)

  # the comment concerning the trainee
  assessment = models.TextField(blank=True, null=True)

  def __unicode__(self):
    return "HC Trainee Comm.: " + self.hc_survey.house.name


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

  def __unicode__(self):
    return "HC Rec.: " + self.house.name

from django.db import models
from houses.models import House
from accounts.models import Trainee

class HCSurvey(models.Model):

  # many-to-one: The house (has many surveys) this survey concerns
  house = models.ForeignKey(House)

  # hc submitting the HCSurvey
  hc = models.ForeignKey(Trainee)

  def __unicode__(self):
    return "House Survey: " + self.house


class HCGeneralComment(models.Model):

  # one-to-one: HCSurvey has one HCGenenralComment
  hc_survey = models.OneToOneField(HCSurvey, primary_key=True)

  # atmosphere of the house
  atmosphere = models.TextField(blank=True, null=True)

  # situations of the house
  situations = models.TextField(blank=True, null=True)

  # general comments concerning the house
  comment = models.TextField(blank=True, null=True)


class HCTraineeComment(models.Model):

  # many-to-one: the HCSurvey (has many comments) this comment belongs to
  hc_survey = models.ForeignKey(HCSurvey)

  # the (resident) trainee this comment concerns
  trainee  = models.ForeignKey(Trainee)

  # the comment concerning the trainee
  comment = models.TextField(blank=True, null=True)


class HCRecommendation(models.Model):

  # The recommendation concerning this house
  house = models.ForeignKey(House)

  # hc writing this recommendation
  hc = models.ForeignKey(Trainee, related_name='hc')

  # terms completed next term for hc
  hc_terms_complete = models.IntegerField()

  # trainee recommended by hc for hc role
  choice = models.ForeignKey(Trainee, related_name='recommended_hc')

  # detailed recommendation for the chosen trainee
  recommendation = models.TextField(blank=True, null=True)

  # the following fields are concerning the recommended trainee

  choice_terms_complete = models.IntegerField()

  age = models.IntegerField()

  exercise_of_the_spirit = models.TextField(blank=True, null=True)

  tidiness = models.TextField(blank=True, null=True)

  punctuality = models.TextField(blank=True, null=True)

  even_tempered = models.TextField(blank=True, null=True)

  ability_to_shepherd = models.TextField(blank=True, null=True)

  responsible = models.TextField(blank=True, null=True)

  attitude = models.TextField(blank=True, null=True)

  physical_endurance = models.TextField(blank=True, null=True)

  average = models.TextField(blank=True, null=True)

  notes = models.TextField(blank=True, null=True)

  def __unicode__(self):
    return "HC Rec.: " + self.house
from django.db import models
from houses.models import House
from accounts.models import Trainee
from terms.models import Term
from django.core.urlresolvers import reverse


class HCSurveyAdmin(models.Model):

  # keeps track of term
  term = models.ForeignKey(Term, null=True, blank=True)

  # 1st, 2nd, 3rd (etc.) survey of the term
  index = models.SmallIntegerField(default=0)

  open_survey = models.BooleanField(default=False)

  open_time = models.DateTimeField(null=True, blank=True)

  close_time = models.DateTimeField(null=True, blank=True)

  def get_update_url(self):
    return reverse('hc:hc-admin-update', kwargs={'pk': self.id})

  def get_delete_url(self):
    return reverse('hc:hc-admin-delete', kwargs={'pk': self.id})


class HCRecommendationAdmin(models.Model):

  term = models.ForeignKey(Term, null=True, blank=True)

  open_survey = models.BooleanField(default=False)

  open_time = models.DateTimeField(null=True, blank=True)

  close_time = models.DateTimeField(null=True, blank=True)


class HCSurvey(models.Model):

  survey_admin = models.ForeignKey(HCSurveyAdmin, null=True, blank=True)

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

  survey_admin = models.ForeignKey(HCRecommendationAdmin, null=True, blank=True)

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

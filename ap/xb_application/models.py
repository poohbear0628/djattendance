from django.db import models
from django.core.urlresolvers import reverse
from accounts.models import Trainee


class XBApplication(models.Model):
  GENDER_CHOICES = (
      ('B', 'Brother'),
      ('S', 'Sister'),
  )

  TERM_CHOICES = (
      (1, 1),
      (2, 2),
      (3, 3),
      (4, 4)
  )

  BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

  MARITAL_CHOICES = (
      ('S', 'Single'),
      ('M', 'Married'),
      ('E', 'Engaged'),
      ('D', 'Divorced'),
  )

  CITIZENSHIP_CHOICES = (
      ('C', 'Citizenship'),
      ('R', 'Resident'),
      ('O', 'Other'),
  )

  ATTITUDE_CHOICES = (
      ('A', 'Agree'),
      ('D', 'Disagree'),
      ('B', 'Burdened'),
  )

  SUPPORT_CHOICES = (
      ('Y', 'Yourself'),
      ('C', 'Church'),
      ('F', 'Family'),
      ('O', 'Other'),
  )

  # applicant
  trainee = models.ForeignKey(Trainee, max_length=500, null=True, blank=True)

  name = models.CharField(max_length=100, null=True, blank=True)

  gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)

  address = models.CharField(max_length=100, null=True, blank=True)

  city = models.CharField(max_length=100, null=True, blank=True)

  state = models.CharField(max_length=30, null=True, blank=True)

  zip_code = models.IntegerField(null=True, blank=True)

  cell_phone = models.CharField(max_length=30, null=True, blank=True)

  home_phone = models.CharField(max_length=30, null=True, blank=True)

  email = models.CharField(max_length=30, null=True, blank=True)

  team = models.CharField(max_length=100, null=True, blank=True)

  loans = models.BooleanField(choices=BOOL_CHOICES, default=False)

  sending_locality = models.CharField(max_length=100, null=True, blank=True)

  birthdate = models.DateField(blank=True, null=True)

  age = models.IntegerField(blank=True, null=True)

  automobile = models.BooleanField(choices=BOOL_CHOICES, default=False)

  seats = models.IntegerField(null=True, blank=True)

  citizenship = models.CharField(max_length=30, choices=CITIZENSHIP_CHOICES, null=True, blank=True)

  citizenship_other = models.CharField(max_length=100, null=True, blank=True)
  
  college1 = models.CharField(max_length=100, null=True, blank=True)

  major1 = models.CharField(max_length=100, null=True, blank=True)

  degree1 = models.CharField(max_length=100, null=True, blank=True)

  college2 = models.CharField(max_length=100, null=True, blank=True)

  major2 = models.CharField(max_length=100, null=True, blank=True)

  degree2 = models.CharField(max_length=100, null=True, blank=True)

  date_saved = models.DateField(null=True, blank=True)

  date_baptized = models.DateField(null=True, blank=True)

  first_church = models.CharField(max_length=150, null=True, blank=True)

  first_church_date = models.DateField(null=True, blank=True)

  ftta_service = models.CharField(max_length=300, null=True, blank=True)

  ftt_location = models.CharField(max_length=300, null=True, blank=True)

  grad_date = models.DateField(null=True, blank=True)

  marital = models.CharField(max_length=1, choices=MARITAL_CHOICES, null=True, blank=True)

  spouse_name = models.CharField(max_length=100, null=True, blank=True)

  spouse_occupation = models.CharField(max_length=150, null=True, blank=True)

  spouse_age = models.IntegerField(null=True, blank=True)

  date_marriage = models.DateField(null=True, blank=True)

  spouse_attitude = models.CharField(max_length=1, choices=ATTITUDE_CHOICES, null=True, blank=True)

  dependents = models.IntegerField(null=True, blank=True)

  support_yourself = models.BooleanField(default=False)

  support_church = models.BooleanField(default=False)

  support_family = models.BooleanField(default=False)

  support_other_explain = models.CharField(max_length=500, null=True, blank=True)

  pertinent_info = models.TextField(max_length=500, null=True, blank=True)

  narrative = models.TextField(max_length=3000, null=True, blank=True)

  submitted = models.BooleanField(default=False)

  date_submitted = models.DateField(null=True, blank=True)

  last_updated = models.DateTimeField(null=True, blank=True)

  def __unicode__(self):
    return "[%s] - [Submitted: %s]" % (self.trainee, self.submitted)

  def get_absolute_url(self):
    return reverse('xb:xb-application')

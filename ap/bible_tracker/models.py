from django.db import models
from django.contrib.postgres.fields import HStoreField
from accounts.models import Trainee

class BibleReading(models.Model):
    trainee = models.ForeignKey(Trainee, null=True)
    weeklyReadingStatus = HStoreField()
    booksRead = HStoreField()
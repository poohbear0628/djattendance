from datetime import datetime, time, date, timedelta
from pytz import timezone
import pytz

from django.db import models
from django.contrib.postgres.fields import HStoreField

from accounts.models import User, Trainee
from classes.models import Class



class Classnotes(models.Model):

	CN_STATUS = (
		('A', 'Approved'),
		('P', 'Pending'),
		('F', 'Fellowship'),
		('U', 'Unsubmitted'),
	)

	CN_TYPE = (
		('R', 'Regular'),
		('S', 'Special')
	)

	status = models.CharField(max_length=1, choices=CN_STATUS, default='U')
	type = models.CharField(max_length=1, choices=CN_TYPE, default='R')
	trainee = models.ForeignKey(Trainee, related_name='%(class)ss')
	classname = models.ForeignKey(Class)
	# the date of the class doing the class notes for
	classdate = models.DateField(blank=True, null=True)

	comments = models.TextField(blank=True, null=True)

	date_assigned = models.DateTimeField(auto_now_add=True)
	date_due = models.DateTimeField(editable=False)
	date_submitted = models.DateTimeField(blank=True, null=True)

    # content of class note
	content = models.TextField(blank=True, null=True)

	# minWord Count
	minimum_words = models.PositiveSmallIntegerField(default=250)
	submitting_paper_copy = models.BooleanField(default=False)

	def clean(self, *args, **kwargs):
		"""Custom validator for word count"""
		wc_list = self.content.split()
		# if len(wc_list) < self.minimum_words and self.submitting_paper_copy is False:
		#     raise ValidationError("Your word count is less than {count}".format(count=self.minimum_words))
		super(Classnotes, self).clean(*args, **kwargs)

	def save(self, **kwargs):
		""" Class notes are due 10 days after assigned """

		# only add days if it's the first time the model is saved
		if not self.id:
			d = timedelta(days=10)
			self.date_due = datetime.now() + d
		self.full_clean()
		super(Classnotes, self).save()

	class Meta:
		ordering = ['-date_assigned']

	def __unicode__(self):
		return "{name}'s class note for {classname} assigned on {date_assigned} Status: {status}".format(
			name=self.trainee.full_name,
			classname=self.classname,
			date_assigned=timezone('US/Pacific').localize(self.date_assigned),
			status=self.status,
		)

class Classnotes_Tracker(models.Model):
	trainee = models.ForeignKey(Trainee, related_name='%(class)ss')

	# classname : number of absences
	# absence_counts only include absence type: sickness, unexcused, other, fellowship
	absence_counts = HStoreField()
	classnotes_owed = HStoreField() # classname : number of classnotes owed
	date_assigned = models.DateField(blank=True, null=True) # might not need this field after all

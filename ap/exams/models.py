import datetime

from django.db import models
from accounts.models import Trainee
from classes.models import Class

from exams.utils import time_in_range



""" exams models.py

This module allows TA's to create, read, update, and delete exams, and view exam statistics, 
and for trainees to take exams.

DATA MODELS:
	- ExamTemplate: the exam created by the TA for a class.
	- Exam: a specific instance of an exam template, linked to a trainees
		consists of responses
	- Question (abstract): the question prompts which belong to an exam template 
	- Response (abstract): a trainee's response to a question prompt, belonging to an exam.
		- TextQuestion
		- TextResponse

"""

class ExamTemplate(models.Model):
	created = models.DateTimeField(auto_now_add=True)

	# note: class includes term
	training_class = models.ForeignKey(Class)

	# an exam is available to be taken by trainees during a given span of time
	opens_on = models.DateTimeField(auto_now=False)
	closes_on = models.DateTimeField(auto_now=False)

	# cut-off percentage; generally 60% but manually definable by TAs
	cutoff = models.IntegerField(default=60)

	def __unicode__(self):
		return "Exam for %s, [%s]" % (self.training_class, self.training_class.term)

	def is_complete(self, trainee_id):
		try:
			Exam.objects.get(exam_template=self, trainee=trainee_id, is_complete=True)
			return True
		except Exam.DoesNotExist:
			return False

	def statistics(self):
		exams = Exam.objects.filter(exam_template=self)
		total = 0
		minimum = 100
		maximum = 0
		for exam in exams:
			total = total + exam.grade
			if exam.grade < minimum:
				minimum = exam.grade
			if exam.grade > maximum:
				maximum = exam.grade
		stats = { 'maximum': 'n/a', 'minimum': 'n/a', 'average': 0 }
		if exams.count() > 0:
			stats['average'] = float(total)/float(exams.count())
			stats['minimum'] = minimum
			stats['maximum'] = maximum
		return stats

	def _is_open(self):
		return time_in_range(self.opens_on, self.closes_on, datetime.datetime.now())
	is_open = property(_is_open)


class Exam(models.Model):
	is_complete = models.BooleanField(default=False)
	is_graded = models.BooleanField(default=False)

	grade = models.IntegerField(default=0)

	# each exam instance is linked to exactly one trainee
	trainee = models.ForeignKey(Trainee)
	exam_template = models.ForeignKey(ExamTemplate)

	def __unicode__(self):
		return "%s's exam" % (self.trainee)


""" The Question and Response classes are abstract so different types of questions
and their corresponding response types can be easily created, i.e.,
MultipleChoiceQuestion, MultipleChoiceResponse, BooleanQuestion, etc. """

class Question(models.Model):
	exam_template = models.ForeignKey(ExamTemplate, related_name="questions")

	class Meta:
		abstract = True

class Response(models.Model):
	exam = models.ForeignKey(Exam, related_name="responses")

	class Meta:
		abstract = True

class TextQuestion(Question):
	body = models.CharField(max_length=500)
	max_score = models.IntegerField(default=1)

class TextResponse(Response):
	body = models.CharField(max_length=5000)
	question = models.ForeignKey(TextQuestion)

class TextResponseGrade(models.Model):
	response = models.ForeignKey(TextResponse)
	score = models.IntegerField()
	comment = models.CharField(max_length=500)
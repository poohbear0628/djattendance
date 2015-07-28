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

class ExamTemplateDescriptor(models.Model):
	training_class = models.ForeignKey(Class)

	# an exam is automatically available to be taken by trainees during a given
	# time frame
	opens_on = models.DateTimeField(auto_now=False)
	closes_on = models.DateTimeField(auto_now=False)

	is_midterm = models.BooleanField()

	# number of section in the exam
	section_count = models.IntegerField(default=1)

	# total score is not user set--this is set as questions are added and point
	# values assigned for each question.
	total_score = models.IntegerField(default=1)

	def __unicode__(self):
		return "Exam for %s, [%s]" % (self.training_class, self.training_class.term)

	def is_complete(self, trainee_id):
		try:
			Exam2.objects.get(exam_template=self, trainee=trainee_id, is_complete=True)
			return True
		except Exam2.DoesNotExist:
			return False

	def statistics(self):
		exams = Exam2.objects.filter(exam_template=self)
		total = 0

		# TODO: This needs to be fixed
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

class ExamTemplateSections(models.Model):
	# This field is formed "{pk of ExamTemplateDescriptor}_{section id, 
	# 1-indexed}".  We will use this to look up rows in this table
	template_section_key = models.CharField(max_length=100, primary_key=True, 
											unique=True)

	question_count = models.IntegerField()
	first_question_index = models.IntegerField(default=1)

	# TODO: this will be replaced by an hstore that will store JSON.
	# This functionality is available in django 1.8+
	questions = models.CharField(max_length=600)

class Exam2(models.Model):
	# each exam instance is linked to exactly one trainee and template
	trainee = models.ForeignKey(Trainee)
	exam_template = models.ForeignKey(ExamTemplateDescriptor)

	# if false, user submitted by paper, so the only meaningful field below
	# this is score.
	is_submitted_online = models.BooleanField(default=True)
	is_complete = models.BooleanField(default=False)
	is_graded = models.BooleanField(default=False)

	# 0 indicates first take.
	retake_number = models.IntegerField(default=0)

	# Calculated and set when grader saves/finalizes exam grading or, if not
	# taken online, set by the grading sister manually.
	grade = models.IntegerField(default=0)

class ExamResponses(models.Model):
	# This field is formed "{pk of Exam}_{pk of trainee}_{question number}"
	response_key = models.CharField(max_length=100, primary_key=True, 
									unique=True)

	# TODO: this will be replaced by an hstore that will store JSON
	# This functionality is available in django 1.8+.
	response = models.CharField(max_length=10000)

	score = models.IntegerField(default=0)

	# TODO: this will be replaced by an hstore that will store JSON.
	# This functionality is available in django 1.8+.
	grader_extra = models.CharField(max_length=1000)

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
	# each exam instance is linked to exactly one trainee and template
	trainee = models.ForeignKey(Trainee)
	exam_template = models.ForeignKey(ExamTemplate)

	is_complete = models.BooleanField(default=False)
	is_graded = models.BooleanField(default=False)

	# Calculated and set when grader saves/finalizes exam grading
	grade = models.IntegerField(default=0)

	def __unicode__(self):
		return "%s's exam" % (self.trainee)


""" The Question and Response classes are abstract so different types of questions
and their corresponding response types can be easily created, i.e.,
MultipleChoiceQuestion, MultipleChoiceResponse, BooleanQuestion, etc. """

class Question(models.Model):
	exam_template = models.ForeignKey(ExamTemplate, related_name="questions")


	# included for future use--when we have different exams on the server, we may wan
	# to have the sections separated a bit better
	section = models.IntegerField(default=1)

	# order of question within this section -- for now unused, just use question id.  This
	# is necessary for when we have multiple types of questions or if we ever want to 
	# provide functionality for reordering the questions.
	question_index = models.IntegerField(null=True)
	point_value = models.IntegerField(default=1)

	class Meta:
		abstract = True

class Response(models.Model):
	exam = models.ForeignKey(Exam, related_name="responses")
	score = models.IntegerField(blank=True, null=True)

	class Meta:
		abstract = True

class TextQuestion(Question):
	body = models.CharField(max_length=500)

class TextResponse(Response):
	body = models.CharField(max_length=5000)
	question = models.ForeignKey(TextQuestion)
	comment = models.CharField(max_length=500)


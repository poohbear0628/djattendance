import datetime

from django.contrib.postgres.fields import HStoreField
from django.db import models
from accounts.models import Trainee
from classes.models import Class

from exams.utils import time_in_range



""" exams models.py

This module allows TA's to create, read, update, and delete exams, and view exam statistics, 
and for trainees to take exams.

DATA MODELS:
	- ExamTemplateDescriptor: Describes a given exam, including what class and
		general information
	- ExamTemplateSections: describes a section of an exam, including the
		questions for the section
	- Exam: a specific instance of an exam template, holds general information 
		pertaining to this take of the exam.
	- ExamResponse: keyed by a combination of exam/question number, holds the 
		a response to a single exam question
"""

class ExamTemplateDescriptor(models.Model):
	training_class = models.ForeignKey(Class)

	# an exam is automatically available to be taken by trainees during a given
	# time frame
	opens_on = models.DateTimeField(auto_now=False)
	closes_on = models.DateTimeField(auto_now=False)
	# TODO: perhaps this should be a length of time instead of hardcoded times?

	is_midterm = models.BooleanField()

	# number of section in the exam
	section_count = models.IntegerField(default=1)

	# total score is not user set--this is set as questions are added and point
	# values assigned for each question.
	total_score = models.IntegerField(default=1)

	def __unicode__(self):
		return "Exam for %s, [%s]" % (self.training_class, self.training_class.term)

	def is_complete(self, trainee_id):
		if Exam.objects.filter(exam_template=self, trainee=trainee_id, is_complete=True).exists():
			return True
		return False

	def statistics(self):
		exams = Exam.objects.filter(exam_template=self)
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
	# JSON should include at minimum: question, point value
	# This functionality is available in django 1.8+
	questions = HStoreField(null=True)

class Exam(models.Model):
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

class ExamResponse(models.Model):
	# This field is formed "{pk of Exam}_{pk of trainee}_{question number}"
	response_key = models.CharField(max_length=100, primary_key=True, 
									unique=True)

	# TODO: this will be replaced by an hstore that will store JSON
	# This functionality is available in django 1.8+.
	response = models.CharField(max_length=10000)

	score = models.IntegerField(blank=True, null=True)

	# TODO: this will be replaced by an hstore that will store JSON.
	# This functionality is available in django 1.8+.
	grader_extra = models.CharField(max_length=1000)

class ExamRetake(models.Model):
	trainee = models.ForeignKey(Trainee)
	exam_template = models.ForeignKey(ExamTemplateDescriptor)
	is_complete = models.BooleanField(default=False)

	# FUTURE: use this to close the exam at the proper time
	time_opened = models.DateTimeField(auto_now_add=True)

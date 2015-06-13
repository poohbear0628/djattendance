import datetime

from django.views.generic.edit import FormView
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse_lazy

from django.views.generic import View
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views.generic.list import ListView
from django.shortcuts import redirect
from django.contrib import messages
from django_select2 import *

from .forms import TraineeSelectForm
from .models import ExamTemplate, Exam, TextQuestion, TextResponse, TextResponseGrade, Trainee

class ExamTemplateListView(ListView):
    template_name = 'exams/exam_template_list.html'
    model = ExamTemplate
    context_object_name = 'exam_templates'

    def get_queryset(self):
    	return ExamTemplate.objects.all()

    def get_context_data(self, **kwargs):
    	context = super(ExamTemplateListView, self).get_context_data(**kwargs)
    	context['taken'] = []
    	for template in ExamTemplate.objects.all():
    		context['taken'].append(template.is_complete(self.request.user.trainee))
    	return context

class SingleExamGradesListView(CreateView, SuccessMessageMixin):
	template_name = 'exams/single_exam_grades.html'
	model = ExamTemplate
	context_object_name = 'exam_grades'
	fields = []
	success_url = reverse_lazy('exams:exam_template_list')
	success_message = 'Exam grades updated.'

	def get_context_data(self, **kwargs):
		context = super(SingleExamGradesListView, self).get_context_data(**kwargs)
		context['exam_template'] = ExamTemplate.objects.get(pk=self.kwargs['pk'])
		try:
			context['exams'] = Exam.objects.filter(exam_template=context['exam_template'], is_complete=True).order_by('trainee__account__lastname')
		except Exam.DoesNotExist:
			context['exams'] = []
		return context

	def post(self, request, *args, **kwargs):
		if request.method == 'POST':
			grades = request.POST.getlist('exam-grade')
			exam_ids = request.POST.getlist('exam-id')
			for index, exam_id in enumerate(exam_ids):
				try:
					exam = Exam.objects.get(id=exam_id)
				except Exam.DoesNotExist:
					exam = False
				if exam:
					exam.grade = grades[index]
					exam.is_graded = True
					exam.save()
			messages.success(request, 'Exam grades saved.')
			return HttpResponseRedirect(reverse_lazy('exams:exam_template_list'))
		else:
			messages.add_message(request, messages.ERROR, 'Nothing saved.')
			return redirect('exams:exams_template_list')
		return HttpResponseRedirect(reverse_lazy('exams:exam_template_list'))

class GenerateGradeReports(CreateView, SuccessMessageMixin):
	model = Exam
	template_name = 'exams/exam_grade_reports.html'
	success_url = reverse_lazy('exams:exam_grade_reports')

	def get_context_data(self, **kwargs):
		context = super(GenerateGradeReports, self).get_context_data(**kwargs)
		context['trainee_select_form'] = TraineeSelectForm()
		context['trainees'] = TraineeSelectForm
		trainee_list = self.request.GET.getlist('trainees')
		exams = {}
		for trainee in trainee_list:
			try:
				exams[Trainee.objects.get(id=trainee)] = Exam.objects.filter(trainee_id=trainee)
			except Exam.DoesNotExist:
				exams[trainee] = {}				
		context['exams'] = exams
		return context

	# def get_queryset(self):
		# print self.kwargs
		# print self.request

	# def post(self, request, *args, **kwargs):
	# 	if request.method == 'POST':
	# 		trainees = request.POST.getlist('trainees')
	# 		request._post = request.POST.copy()
	# 		request._get = request.POST.copy()
	# 		return super(GenerateGradeReports, self).post(self, request, *args, **kwargs)

class GenerateRetakeList(DetailView):
	template_name = 'exams/exam_retake_list.html'
	model = ExamTemplate
	fields = []
	context_object_name = 'exam_template'

	def get_context_data(self, **kwargs):
		context = super(GenerateRetakeList, self).get_context_data(**kwargs)
		context['exam_template'] = ExamTemplate.objects.get(pk=self.kwargs['pk'])
		exam_stats = context['exam_template'].statistics()
		context['exam_max'] = exam_stats['maximum']
		context['exam_min'] = exam_stats['minimum']
		context['exam_average'] = exam_stats['average']
		try:
			context['exams'] = Exam.objects.filter(exam_template=context['exam_template']).order_by('trainee__account__lastname')
		except Exam.DoesNotExist:
			context['exams'] = []
		return context

class TakeExamView(SuccessMessageMixin, CreateView):
	template_name = 'exams/take_single_exam.html'
	model = Exam
	context_object_name = 'exam'
	fields = []

	# context data: template, questions, responses, whether or not the exam is complete
	def get_context_data(self, **kwargs):
		context = super(TakeExamView, self).get_context_data(**kwargs)
		context['exam_template'] = ExamTemplate.objects.get(pk=self.kwargs['pk'])
		context['exam_questions'] = context['exam_template'].questions.all().order_by('id')
		try:
			exam = Exam.objects.get(exam_template=context['exam_template'], trainee=self.request.user.trainee)
			context['exam_responses'] = exam.responses.all().order_by('question')
		except Exam.DoesNotExist:
			context['exam_responses'] = []

		context['exam_is_complete'] = context['exam_template'].is_complete(self.request.user.trainee)
		return context

	def _update_or_add_exam(self, is_complete):
		# todo(haileyl): use update_or_create when we move to Django 1.7+
		template = ExamTemplate.objects.get(pk=self.kwargs['pk'])
		trainee = self.request.user.trainee
		try:
			exam = Exam.objects.get(exam_template = template, trainee = trainee)
			# The only value on exam that can be updated on submit is is_complete.
			# Trainee and template will never change.
			exam.is_complete = is_complete
			exam.save()
		except Exam.DoesNotExist:
			exam = Exam(exam_template = template, trainee = trainee, is_complete = is_complete)
			exam.save()
		return exam

	def _update_or_add_response(self, exam, new_response, question):
		# todo(haileyl): use update_or_create when we move to Django 1.7+
		try:
			response = TextResponse.objects.get(exam = exam, question = question)
			response.body = new_response
			response.save()
		except TextResponse.DoesNotExist:
			response = TextResponse(exam = exam, question = question, body = new_response)
			response.save()

	def post(self, request, *args, **kwargs):
		is_complete = False
		if 'Submit' in request.POST:
			is_complete = True

		# create exam if it doesn't exist and update the is_complete field
		exam = self._update_or_add_exam(is_complete)

		# create or update responses for given exam
		responses = request.POST.getlist('response')
		questions = ExamTemplate.objects.get(pk = self.kwargs['pk']).questions.all().order_by('id')
		for i in range(len(responses)):
			self._update_or_add_response(exam, responses[i], questions[i])

		# if exam is complete, redirect to page listing available exams, otherwise
		# simply refresh the page.
		if (is_complete):
			messages.success(request, 'Exam submitted successfully.')
			return HttpResponseRedirect(reverse_lazy('exams:exam_template_list'))
		else:
			messages.success(request, 'Exam progress saved.')
			return self.get(request, *args, **kwargs)

class GradeExamView(SuccessMessageMixin, CreateView):
	template_name = 'exams/grade_single_exam.html'
	model = Exam
	context_object_name = 'exam'
	fields = []

	# context data: template, questions, responses, whether or not the exam is complete
	def get_context_data(self, **kwargs):
		context = super(GradeExamView, self).get_context_data(**kwargs)
		exam = Exam.objects.get(pk=self.kwargs['pk'])
		context['exam_template'] = exam.exam_template
		exam_questions = context['exam_template'].questions.all().order_by('id')
		exam_responses = exam.responses.all().order_by('question')
		response_scores = []
		grader_comments = []
		for response in exam_responses:
			try:
				text_response = TextResponseGrade.objects.get(response = response)
				if (text_response.score == None):
					response_scores.append("")
				else:
					response_scores.append(text_response.score)
				grader_comments.append(text_response.comment)
			except TextResponseGrade.DoesNotExist:
				response_scores.append("")
				grader_comments.append("")
		context['data'] = zip(exam_questions, exam_responses, response_scores, grader_comments)
		context['total_score'] = exam.grade
		return context

	def _update_or_add_responsegrade(self, response, score, comment):
		# todo(haileyl): use update_or_create when we move to Django 1.7+
		try:
			response_grade = TextResponseGrade.objects.get(response = response)
		except TextResponseGrade.DoesNotExist:
			response_grade = TextResponseGrade(response = response)
			
		if score.isdigit():
			response_grade.score = int(score)
		response_grade.comment = comment
		response_grade.save()

	# error checking for score.  Adds an error message if we run into any problems.  Return value is True if no errors found,
	# False otherwise.
	def _score_valid(self, is_graded, score, max_score, question_id, request):
		has_error = False

		# check if inputed score is valid
		if (not score.isdigit() and len(score) > 0) or (score.isdigit() and int(score) > max_score):
			messages.add_message(request, messages.ERROR, "Invalid score for question " + str(question_id) + ". Input provided: " + score)
			has_error = True

		# if we're finalizing the score, the inputed score _has_ to be valid
		if is_graded and not score.isdigit():
			messages.add_message(request, messages.ERROR, "Cannot finalize, invalid or empty score for question " + str(question_id) + ".")
			has_error = True

		return not has_error

	# returns the grade for the exam.
	def _total_exam_score(self, exam):
		exam_responses = exam.responses.all()
		total = 0

		for response in exam_responses:
			try:
				text_response = TextResponseGrade.objects.get(response = response)
				total = total + text_response.score
			except TextResponseGrade.DoesNotExist:
				pass

		return total

	def post(self, request, *args, **kwargs):
		is_graded = False
		has_error = False

		if 'Finalize' in request.POST:
			is_graded = True

		exam = Exam.objects.get(pk=self.kwargs['pk'])

		# create or update response grades for given exam
		scores = request.POST.getlist('question-score')
		comments = request.POST.getlist('grader-comment')
		questions = exam.exam_template.questions.all().order_by('id')

		for i in range(len(scores)):
			response = TextResponse.objects.get(exam = exam, question = questions[i])
			
			if self._score_valid(is_graded, scores[i], questions[i].max_score, i + 1, request):
				self._update_or_add_responsegrade(response, scores[i], comments[i])
			else:
				has_error = True

		exam.grade = self._total_exam_score(exam)
		exam.save()

		# short cut success messages if there are errors
		if has_error:
			return self.get(request, *args, **kwargs)

		# if grading is complete, go back, otherwise refresh page.
		if (is_graded):
			exam.is_graded = True
			exam.save()

			messages.success(request, 'Exam grading finalized.')
			return HttpResponseRedirect(reverse_lazy('exams:single_exam_grades', kwargs={'pk': exam.exam_template.id}))
		else:
			messages.success(request, 'Exam grading progress saved.')
			return self.get(request, *args, **kwargs)
import datetime
from collections import namedtuple

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
from .models import ExamTemplate, Exam, TextQuestion, TextResponse, Trainee
from .models import ExamTemplateDescriptor, ExamTemplateSections, Exam2, ExamResponses

from exams.exam_helpers import get_response_grader_extras, get_exam_questions
# PDF generation
import cStringIO as StringIO

from django.template.loader import get_template
from django.http import HttpResponse
import xhtml2pdf.pisa as pisa
from cgi import escape


class ExamTemplateListView(ListView):
    template_name = 'exams/exam_template_list.html'
    model = ExamTemplateDescriptor
    context_object_name = 'exam_templates'

    def get_queryset(self):
    	return ExamTemplateDescriptor.objects.all()

    def get_context_data(self, **kwargs):
    	context = super(ExamTemplateListView, self).get_context_data(**kwargs)
    	context['taken'] = []
    	for template in ExamTemplateDescriptor.objects.all():
    		context['taken'].append(template.is_complete(self.request.user.trainee))
    		print "Taken:" + str(template.is_complete(self.request.user.trainee))
    	return context

class SingleExamGradesListView(CreateView, SuccessMessageMixin):
	template_name = 'exams/single_exam_grades.html'
	model = ExamTemplateDescriptor
	context_object_name = 'exam_grades'
	fields = []
	success_url = reverse_lazy('exams:exam_template_list')
	success_message = 'Exam grades updated.'

	def get_context_data(self, **kwargs):
		context = super(SingleExamGradesListView, self).get_context_data(**kwargs)
		context['exam_template'] = ExamTemplateDescriptor.objects.get(pk=self.kwargs['pk'])
		try:
			context['exams'] = Exam2.objects.filter(exam_template=context['exam_template'], is_complete=True).order_by('trainee__account__lastname')
		except Exam2.DoesNotExist:
			context['exams'] = []
		return context

	def post(self, request, *args, **kwargs):
		if request.method == 'POST':
			grades = request.POST.getlist('exam-grade')
			exam_ids = request.POST.getlist('exam-id')
			for index, exam_id in enumerate(exam_ids):
				try:
					exam = Exam2.objects.get(id=exam_id)
				except Exam2.DoesNotExist:
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

class GenerateOverview(DetailView):
	template_name = 'exams/exam_overview.html'
	model = ExamTemplateDescriptor
	fields = []
	context_object_name = 'exam_template'

	def get_context_data(self, **kwargs):
		context = super(GenerateOverview, self).get_context_data(**kwargs)
		context['exam_template'] = ExamTemplateDescriptor.objects.get(pk=self.kwargs['pk'])
		exam_stats = context['exam_template'].statistics()
		context['exam_max'] = exam_stats['maximum']
		context['exam_min'] = exam_stats['minimum']
		context['exam_average'] = exam_stats['average']
		try:
			context['exams'] = Exam.objects.filter(exam_template=context['exam_template']).order_by('trainee__account__lastname')
		except Exam.DoesNotExist:
			context['exams'] = []
		return context

class ExamRetakeView(DetailView):
	model = ExamTemplateDescriptor
	context_object_name = 'exam_template'

	def get_context_data(self, **kwargs):
		context = super(ExamRetakeView, self).get_context_data(**kwargs)
		context['exam_template'] = ExamTemplateDescriptor.objects.get(pk=self.kwargs['pk'])
		try:
			context['exams'] = Exam2.objects.filter(exam_template=context['exam_template']).order_by('trainee__account__lastname')
		except Exam2.DoesNotExist:
			context['exams'] = []
		return context

	# pip install pisa, html5lib, pypdf, pdf
	def get(self, request, *args, **kwargs):
		template = get_template('exams/exam_retake_list.html')
		self.object = self.get_object()
		context = super(ExamRetakeView, self).get_context_data(**kwargs)
		html = template.render(context)
		result = StringIO.StringIO()
		
		pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
		if not pdf.err:
			return HttpResponse(result.getvalue(), mimetype = 'application/pdf')
		return HttpResponse('There were some errors<pre>%s</pre>' %escape(html))

class TakeExamView(SuccessMessageMixin, CreateView):
	template_name = 'exams/take_single_exam.html'
	model = Exam2
	context_object_name = 'exam'
	fields = []

	QuestionData = namedtuple("QuestionData", "question_number question answer grader_comment")

	def _most_recent_exam(self, exam_template):
		try:
			exams_taken = Exam2.objects.filter(
				exam_template=exam_template, 
				trainee=self.request.user.trainee).order_by('-id')
			exam = exams_taken[0]
		except Exam2.DoesNotExist:
			exam = None

		return exam

	# returns true if exam should be available for this trainee
	def _exam_available(self, most_recent_exam):
		# TODO: missing a lot of cases.  Need to think about this logic
		# quite a bit more.

		# if the exam is in progress or doesn't exist, we're in business
		if (most_recent_exam == None) or (not most_recent_exam.is_complete):
			return True

		# if the exam is not in progress but exists, then the exam is only
		# available if the user is on the retake list for this exam.
		# TODO: Retake functionality NYI.
		return False

	# context data: template, questions, responses, whether or not the exam is complete
	def get_context_data(self, **kwargs):
		context = super(TakeExamView, self).get_context_data(**kwargs)
		exam_template_pk = self.kwargs['pk']
		context['exam_template'] = ExamTemplateDescriptor.objects.get(pk=exam_template_pk)

		exam = self._most_recent_exam(context['exam_template'])

		# Can this user take this exam right now?  If not, shortcut the rest of
		# the processing
		context['exam_available'] = self._exam_available(exam);
		if not context['exam_available']:
			return context

		if exam:
			exam_pk = exam.id
		else:
			exam_pk = None

		questions = get_exam_questions(exam_template_pk)
		responses, grader_extras = get_response_grader_extras(exam_template_pk, 
			exam_pk, self.request.user.trainee.id)

		context['data'] = zip(questions, responses, grader_extras)
		return context

	# Returns the exam that we're using
	def _update_or_add_exam(self, is_complete):
		template = ExamTemplateDescriptor.objects.get(pk=self.kwargs['pk'])
		trainee = self.request.user.trainee
		exam = self._most_recent_exam(template)

		if exam == None or exam.is_complete:
			# Create new exam
			retake_count=exam.retake_number + 1 if exam != None else 0
			exam = Exam2(exam_template=template, trainee=trainee, 
							 is_complete=is_complete, is_submitted_online=True, 
							 retake_number=retake_count)
			exam.save()
		else:
			# Update existing exam
			exam.is_complete=is_complete
			exam.save()

		return exam

	def _update_or_add_response(self, exam_pk, trainee_pk, question_number, post_response):
		# TODO: use update_or_create when we move to Django 1.7+
		response_key = "_".join([str(exam_pk), str(trainee_pk), str(question_number)])
		try:
			response = ExamResponses.objects.get(pk=response_key)
			response.response = post_response
			response.save()
		except ExamResponses.DoesNotExist:
			response = ExamResponses(pk=response_key, response=post_response)
			response.save()

	def post(self, request, *args, **kwargs):
		is_complete = False
		if 'Submit' in request.POST:
			is_complete = True

		# create exam if it doesn't exist and update the is_complete field
		exam = self._update_or_add_exam(is_complete)

		# create or update responses for given exam
		# TODO: will need to do some consolidation here where we have multiple
		# question types
		responses = request.POST.getlist('response')

		exam_template_pk = self.kwargs['pk']
		print self.request.user.trainee
		for i in range(len(responses)):
			self._update_or_add_response(exam.id, self.request.user.trainee.id, i + 1, responses[i])

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
		#exam_questions = context['exam_template'].questions.all().order_by('id')
		#exam_responses = exam.responses.all().order_by('question')
		context['data'] = zip(exam_questions, exam_responses)
		context['total_score'] = exam.grade
		return context

	def _update_or_add_responsegrade(self, response, score, comment):
		if score.isdigit():
			response.score = int(score)
		response.comment = comment
		response.save()

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
			if (response.score != None):
				total = total + response.score

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
			
			if self._score_valid(is_graded, scores[i], questions[i].point_value, i + 1, request):
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

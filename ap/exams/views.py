import abc
from collections import namedtuple
import datetime

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import redirect
from django_select2 import *
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .forms import TraineeSelectForm
from .models import Trainee
from .models import ExamTemplateDescriptor, ExamTemplateSections, Exam, ExamResponse

from exams.exam_helpers import get_response_tuple, get_exam_questions

# PDF generation
import cStringIO as StringIO

from django.template.loader import get_template
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

		# TODO: This needs further filtering by class.
		available_trainees = Trainee.objects.filter(Active=True)

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
			context['exams'] = Exam.objects.filter(exam_template=context['exam_template']).order_by('trainee__account__lastname')
		except Exam.DoesNotExist:
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

class SingleExamBaseView(SuccessMessageMixin, CreateView):
	"""This class is the base view for taking and grading an exam."""

	template_name = 'exams/exam.html'
	model = Exam
	context_object_name = 'exam'
	fields = []

	@abc.abstractmethod
	def _is_taking_exam(self):
		"""Return true if the action is to take the exam"""

	@abc.abstractmethod
	def _get_exam_template(self):
		"""Returns the applicable exam template"""

	@abc.abstractmethod
	def _get_exam(self):
		"""Returns the exam to be operated on, creating if applicable"""

	@abc.abstractmethod
	def _exam_available(self):
 		"""Return true if this page should be available for the given user"""

 	@abc.abstractmethod
 	def _visibility_matrix(self):
 		"""Return matrix of form [bool, bool, bool] to indicate visibility of 
 		the response, score, and grader comment fields, respectively"""

 	@abc.abstractmethod
 	def _permissions_matrix(self):
 		"""Return matrix of form [bool, bool, bool] to indicate editability of 
 		the response, score, and grader comment fields, respectively"""

 	@abc.abstractmethod
 	def _action_complete(self, post):
 		"""Returns true if the action for given page is complete (i.e. 
 		Submitted or Finalized)"""

 	@abc.abstractmethod
 	def _process_post_data(self, responses, grader_extras, scores):
 		"""Processes the post data according to purpose of page"""

 	@abc.abstractmethod
 	def _complete(self):
 		"""On action complete, do some validation as necessary.  A return value
 		of False indicates that an error was encountered and complete action 
 		was canceled."""

 	@abc.abstractmethod
 	def _redirect(self, action_complete, has_error, request, *args, **kwargs):
 		"""Returns a redirect request according to parameters. action_complete 
 		is true if the user has either submitted (in case of taking exam) or 
 		finalized (in case of grading)"""

	# context data: template, questions, responses, whether or not the exam is complete
	def get_context_data(self, **kwargs):
		context = super(SingleExamBaseView, self).get_context_data(**kwargs)

		context['taking'] = self._is_taking_exam()
		exam_template = self._get_exam_template()
		context['exam_template'] = exam_template

		if not self._exam_available():
			context['exam_available'] = False
			return context

		context['exam_available'] = True

		exam = self._get_exam()
		if exam:
			exam_pk = exam.id
		else:
			exam_pk = None

		context['permissions'] = self._permissions_matrix
		context['visibility'] = self._visibility_matrix

		# TODO: this shouldn't take pks, but the exam/template themselves
		# TODO2: This should take the visibility matrix to determine whether
		# to send the data at all
		questions = get_exam_questions(exam_template.id)
		responses, grader_extras, scores = get_response_tuple(exam_template.id, 
			exam_pk, self.request.user.trainee.id)

		context['data'] = zip(questions, responses, grader_extras, scores)
		return context

	def post(self, request, *args, **kwargs):
		action_complete = self._action_complete(request.POST)

		# Get exam object that we should operate on
		exam = self._get_exam()

		# Process post data
		responses = request.POST.getlist('response')
		comments = request.POST.getlist('grader-comment')
		scores = request.POST.getlist('question-score')

		is_successful = self._process_post_data(responses, comments, scores, 
			exam.id, self.request.user.trainee.id)

		# Action cannot be completed if inputed data has errors
		if (not is_successful):
			action_complete = False

		# Validate and complete (submit/finalize) submission
		if (action_complete and (not self._complete())):
			is_successful = False
			action_complete = False

		# Redirect
		return self._redirect(action_complete, not is_successful, request, 
			*args, **kwargs)

	class Meta:
		abstract = True

class TakeExamView(SingleExamBaseView):
	def _is_taking_exam(self):
		return True

	def _get_exam_template(self):
		return ExamTemplateDescriptor.objects.get(pk=self.kwargs['pk'])

	def _get_most_recent_exam(self):
		try:
			exams_taken = Exam.objects.filter(
				exam_template=self._get_exam_template(), 
				trainee=self.request.user.trainee).order_by('-id')
			if exams_taken:
				return exams_taken[0]
		except Exam.DoesNotExist:
			pass

		return None

	def _get_exam(self):
		exam = self._get_most_recent_exam()

		# Create a new exam if there's no editable exam, currently
		if exam == None or exam.is_complete:
			retake_count = exam.retake_number + 1 if exam != None else 0
			exam = Exam(exam_template=self._get_exam_template(), 
				trainee=self.request.user.trainee,
				is_complete=False,
				is_submitted_online=True,
				retake_number=retake_count)
			exam.save()

		return exam

	def _exam_available(self):
		# TODO: Check that this exam is applicable to given trainee and is
		# active

		# if the exam is in progress or doesn't exist, we're in business
		most_recent_exam = self._get_most_recent_exam()

		if (most_recent_exam == None or not most_recent_exam.is_complete):
			return True

		# TODO: check if open for retake
		return False

	def _visibility_matrix(self):
		return [True, False, False]

	def _permissions_matrix(self):
		return [True, False, False]

	def _action_complete(self, post):
		return True if 'Submit' in post else False

	def _process_post_data(self, responses, grader_extras, scores, exam_pk, trainee_pk):
		# in take exam view, it is only possible to make changes to responses
		for i in range(len(responses)):
			response_key = "_".join([str(exam_pk), str(trainee_pk), str(i + 1)])
			try:
				response = ExamResponse.objects.get(pk=response_key)
				response.response = responses[i]
			except ExamResponse.DoesNotExist:
				response = ExamResponse(pk=response_key, response=responses[i])
			
			response.save()

		return True

 	def _complete(self):
 		exam = self._get_exam()
 		exam.is_complete = True
 		exam.save()

 		return True

	def _redirect(self, action_complete, has_error, request, *args, **kwargs):
		if (action_complete):
			messages.success(request, 'Exam submitted successfully.')
			return HttpResponseRedirect(reverse_lazy('exams:exam_template_list'))
		else:
			messages.success(request, 'Exam progress saved.')
			return self.get(request, *args, **kwargs)		

class GradeExamView(SingleExamBaseView):
	def _is_taking_exam(self):
		return False

	def _get_exam_template(self):
		exam = Exam.objects.get(pk=self.kwargs['pk'])
		return ExamTemplateDescriptor.objects.get(pk=exam.exam_template.id)

	def _get_exam(self):
		return Exam.objects.get(pk=self.kwargs['pk'])

	def _exam_available(self):
		# TODO: should sanity check that user has grader/TA permissions
		return True

	def _visibility_matrix(self):
		return [True, True, True]

	def _permissions_matrix(self):
		return [False, True, True]
	
	def _action_complete(self, post):
		# TODO: This should be finalize in the grade view
		return True if 'Submit' in post else False

	def _process_post_data(self, responses, grader_extras, scores, exam_pk, trainee_pk):
		is_successful = True
		total_score = 0
		for i in range(len(grader_extras)):
			response_key = "_".join([str(exam_pk), str(trainee_pk), str(i + 1)])
			try:
				response = ExamResponse.objects.get(pk=response_key)
				response.grader_extra = grader_extras[i]

				if (scores[i].isdigit()):
					# TODO: verify valid score inputed--within valid range

					response.score = int(scores[i])
					total_score += int(scores[i])
				else:
					# TODO: verify that either 
					if (response.score != None):
						total_score += response.score

				response.save()
			except ExamResponse.DoesNotExist:
				# TODO: this should never happen.  Is there a NotReached in python?
				pass

		# Save total score
		exam = self._get_exam()
		exam.grade = total_score
		exam.save()
		return is_successful

	# Validate that all questions have been graded and mark grade as finalized
	def _complete(self):
		exam = self._get_exam()

		# FUTURE: Validate that all questions have been assigned a valid 
		# score and that a comment is available for incomplete scores
		exam.is_graded = True
		exam.save()
 		return True

	def _redirect(self, action_complete, has_error, request, *args, **kwargs):
		if (has_error):
			return self.get(request, *args, **kwargs)

		if (action_complete):
			messages.success(request, 'Exam grading finalized.')
			return HttpResponseRedirect(
				reverse_lazy('exams:single_exam_grades', 
					kwargs={'pk': self._get_exam_template().id}))
		else:
			messages.success(request, 'Exam grading progress saved.')
			return self.get(request, *args, **kwargs)

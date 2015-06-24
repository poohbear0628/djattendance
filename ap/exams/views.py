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
from .models import ExamTemplate, Exam, TextQuestion, TextResponse, Trainee

# PDF generation
import cStringIO as StringIO

from django.template.loader import get_template
from django.http import HttpResponse
import xhtml2pdf.pisa as pisa
from cgi import escape



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
			context['exams'] = Exam.objects.filter(exam_template=context['exam_template']).order_by('trainee__account__lastname')
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
	model = ExamTemplate
	fields = []
	context_object_name = 'exam_template'

	def get_context_data(self, **kwargs):
		context = super(GenerateOverview, self).get_context_data(**kwargs)
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

class ExamRetakeView(DetailView):
	model = ExamTemplate
	context_object_name = 'exam_template'

	def get_context_data(self, **kwargs):
		context = super(ExamRetakeView, self).get_context_data(**kwargs)
		context['exam_template'] = ExamTemplate.objects.get(pk=self.kwargs['pk'])
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

	# review (haileyl): static?  doesn't use self
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

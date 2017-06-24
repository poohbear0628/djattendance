import datetime
import json

from braces.views import LoginRequiredMixin, GroupRequiredMixin
from collections import namedtuple
from datetime import timedelta
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.postgres.fields import HStoreField
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django_select2 import *
from django.shortcuts import redirect
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.db.models import Prefetch, Q


from aputils.trainee_utils import trainee_from_user
from ap.forms import TraineeSelectForm
from terms.models import Term

from .forms import ExamCreateForm
from .models import Class
from .models import Trainee
from .models import Exam, Section, Session, Responses, Retake
from decimal import Decimal

from django.contrib.postgres.fields import HStoreField
from exams.utils import get_responses, get_exam_questions, get_edit_exam_context_data, \
  save_exam_creation, get_exam_context_data, retake_available, save_responses, \
  get_exam_section, trainee_can_take_exam

# PDF generation
import cStringIO as StringIO
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
from cgi import escape

import ast

class ExamCreateView(LoginRequiredMixin, GroupRequiredMixin, FormView):

  template_name = 'exams/exam_form.html'
  form_class = ExamCreateForm
  success_url = reverse_lazy('exams:manage')

  group_required = [u'exam_graders', u'administration']

  def get_context_data(self, **kwargs):
    context = super(ExamCreateView, self).get_context_data(**kwargs)
    classes = Class.objects.filter(schedules__term=Term.current_term())
    context['exam_not_available'] = True
    context['classes'] = classes
    context['terms'] = Term.objects.all()
    return context

  def get_form(self, form_class=ExamCreateForm):
    return form_class(**self.get_form_kwargs())

  def form_valid(self, form):
    context = self.get_context_data()
    formset = context['formset']

    if formset.is_valid():
      self.object = form.save()

      for section_form in formset.forms:
        section = Section(exam=self.object, question_count=0)
        section.save()
    else:
      pass
    return super(ExamCreateView, self).form_valid(form)

  def post(self, request, *args, **kwargs):
    # -1 value indicates exam is newly created
    save_exam_creation(request, -1)
    messages.success(request, 'Exam created.')
    return HttpResponseRedirect(reverse_lazy('exams:manage'))

class ExamDelete(DeleteView):
    model = Exam
    def delete_new(request,id):
      u = Exam.objects.get(pk=id).delete()

class ExamEditView(ExamCreateView, GroupRequiredMixin, FormView):

  template_name = 'exams/exam_form.html'
  form_class = ExamCreateForm
  success_url = reverse_lazy('exams:manage')
  group_required = [u'exam_graders', u'administration']

  def get_context_data(self, **kwargs):
    context = super(ExamEditView, self).get_context_data(**kwargs)
    exam = Exam.objects.get(pk=self.kwargs['pk'])
    training_class = Class.objects.get(id=exam.training_class.id)

    return get_edit_exam_context_data(context, exam, training_class)

  def get_form(self, form_class=ExamCreateForm):
    return super(ExamCreateView, self).get_form(form_class)

  def form_valid(self, form):
    return super(ExamCreateView, self).form_valid(form)

  def post(self, request, *args, **kwargs):
    pk=self.kwargs['pk']
    save_exam_creation(request, pk)
    messages.success(request, 'Exam saved.')
    return HttpResponseRedirect(reverse_lazy('exams:manage'))


class ExamTemplateListView(ListView):
  template_name = 'exams/exam_template_list.html'
  model = Exam
  context_object_name = 'exams'

  def get_queryset(self):
    user = self.request.user
    is_manage = 'manage' in self.kwargs
    if is_manage:
      exams = Exam.objects.all()
    else:
      exams = Exam.objects.filter(is_open=True)
    retakes = Retake.objects.filter(trainee=user,
                      is_complete=False)
    exams = list(exams)
    for exam in exams:
      exam.visible = True if exam.is_open and trainee_can_take_exam(user, exam) else False

      # Don't show to exam service manage page
      if not is_manage and not exam.visible:
        exams.remove(exam)
        continue

      exam.completed = True if exam.has_trainee_completed(user) else False
      exam.retake = True if self.exam_in_retakes(retakes, exam) else False
      exam.available = True if not exam.completed or exam.retake else False

    return exams

  def exam_in_retakes(self, retakes, exam):
    for retake in retakes:
      if retake.exam == exam and not retake.is_complete:
        return True
    return False

  def get_context_data(self, **kwargs):
    ctx = super(ExamTemplateListView, self).get_context_data(**kwargs)
    user = self.request.user
    is_manage = 'manage' in self.kwargs
    ctx['exam_service'] = is_manage and user.groups.filter(Q(name='administration') | Q(name='exam_graders')).exists()
    ctx['classes'] = [c['name'].encode("utf8") for c in Class.objects.values('name')]
    ctx['terms'] = [ys['season'].encode("utf8") + ' ' + str(ys['year']) for ys in Term.objects.values('year', 'season')]
    return ctx

class SingleExamGradesListView(CreateView, GroupRequiredMixin, SuccessMessageMixin):
  template_name = 'exams/single_exam_grades.html'
  model = Exam
  context_object_name = 'exam_grades'
  fields = []
  success_url = reverse_lazy('exams:manage')
  success_message = 'Exam grades updated.'

  group_required = [u'exam_graders', u'administration']

  def get_context_data(self, **kwargs):
    context = super(SingleExamGradesListView, self).get_context_data(**kwargs)
    exam = Exam.objects.get(pk=self.kwargs['pk'])
    context['exam'] = exam

    first_sessions = []
    second_sessions = []

    trainees = Trainee.objects.filter(is_active=True)

    if exam.training_class.class_type == 'MAIN':
      trainees = trainees.order_by('lastname')
    elif exam.training_class.class_type == '1YR':
      trainees = trainees.filter(current_term__lte=2)
    elif exam.training_class.class_type == '2YR':
      trainees = trainees.filter(current_term__gte=3)

    trainees = trainees.prefetch_related('exam_sessions', Prefetch('exam_sessions', queryset=Session.objects.filter(exam=exam, is_complete=True).order_by('retake_number'), to_attr='current_sessions'))

    context['data'] = trainees
    return context

  def post(self, request, *args, **kwargs):
    P = request.POST
    # User Error?
    if request.method != 'POST':
      messages.add_message(request, messages.ERROR, 'Nothing saved.')
      return redirect('exams:exams_template_list')

    if 'delete-session-id' in P:
      session_id = int(P['delete-session-id'])
      Session.objects.filter(id=session_id).delete()
      messages.success(request, 'Exam deleted')

    elif 'unfinalize-session-id' in P:
      session_id = int(P['unfinalize-session-id'])
      try:
        session = Session.objects.get(id=session_id)
        session.is_graded = False
        session.save()

        if session.is_submitted_online:
          return HttpResponseRedirect(
            reverse_lazy('exams:grade', kwargs={'pk': session.id}))
      except Session.DoesNotExist:
        pass
    elif 'retake-trainee-id' in P:
      trainee_id = int(P['retake-trainee-id'])
      try:
        trainee = Trainee.objects.get(id=trainee_id)
        exam = Exam.objects.get(pk=self.kwargs['pk'])
        Retake.objects.get_or_create(trainee=trainee, exam=exam)
      except Trainee.DoesNotExist:
        pass
    else:
      exam = Exam.objects.get(pk=self.kwargs['pk'])

      grades = P.getlist('new-grade')
      trainee_ids = P.getlist('trainee-id')
      # trainees = Trainee.objects.filter(id__in=trainee_ids)
      trainees = Trainee.objects.filter(id__in=trainee_ids).prefetch_related('exam_sessions', Prefetch('exam_sessions', queryset=Session.objects.filter(exam=exam, is_complete=True).order_by('retake_number'), to_attr='current_sessions'))
      # Reorder to id order
      trainees_tb = dict([(str(t.id), t) for t in trainees])
      trainees = [trainees_tb[id] if id in trainees_tb else None for id in trainee_ids]

      for index, trainee in enumerate(trainees):
        if trainee == None:
          continue
        if grades[index] == "":
          continue

        if not grades[index].isdigit():
          messages.add_message(request, messages.ERROR,
            'Invalid input for trainee ' + str(trainee))
          continue

        sessions = trainee.current_sessions
        if (len(sessions) == 0):
          retake_number = 0
        else:
          retake_number = sessions[0].retake_number + 1

        session = Session(exam=exam,
          trainee=trainee,
          is_submitted_online=False,
          is_complete=True,
          is_graded=True,
          retake_number=retake_number,
          grade=int(grades[index]))
        session.save()

      grades2 = P.getlist('session-id-grade')
      session_ids = P.getlist('session-id')
      sessions = Session.objects.filter(id__in=session_ids)
      sessions_tb = dict([(str(s.id), s) for s in sessions])
      sessions = [sessions_tb[id] if id in sessions_tb else None for id in session_ids]

      for index, session in enumerate(sessions):
        if session == None:
          continue
        grade = int(grades2[index]) if grades2[index].isdigit() else 0
        session.grade = grade
        session.save()
      messages.success(request, 'Exam grades saved.')

    return self.get(request, *args, **kwargs)

class GenerateGradeReports(CreateView, GroupRequiredMixin, SuccessMessageMixin):
  model = Session
  fields = []
  template_name = 'exams/exam_grade_reports.html'
  success_url = reverse_lazy('exams:exam_grade_reports')

  group_required = [u'exam_graders', u'administration']

  def get_context_data(self, **kwargs):
    pk = self.kwargs['pk']
    ctx = super(GenerateGradeReports, self).get_context_data(**kwargs)
    ctx['trainee_select_form'] = TraineeSelectForm()
    trainees = Trainee.objects.all()
    ctx['trainees'] = trainees
    trainee_list = self.request.GET.getlist('trainees')
    sessions = {}
    # for trainee in trainee_list:
    #   try:
    #     sessions[Trainee.objects.get(id=trainee)] = \
    #       Session.objects.filter(trainee_id=trainee)
    #   except Session.DoesNotExist:
    #     sessions[trainee] = {}

    for trainee in trainees:
      sessions[trainee] = trainee.exam_sessions.all()
    ctx['sessions'] = sessions
    if pk:
      # Get only the exam provided
      sessions = Session.objects.filter(exam__pk=pk)
    else:
      # Get all the exams
      sessions = Session.objects.all()


    ctx['sessions'] = sessions.prefetch_related('exam', 'trainee').order_by('trainee__lastname')

    ctx['exams'] = Exam.objects.all()

    return ctx

class GenerateOverview(DetailView, GroupRequiredMixin):
  template_name = 'exams/exam_overview.html'
  model = Exam
  fields = []
  context_object_name = 'exam'

  group_required = [u'exam_graders', u'administration']

  def get_context_data(self, **kwargs):
    context = super(GenerateOverview, self).get_context_data(**kwargs)
    context['exam'] = Exam.objects.get(pk=self.kwargs['pk'])
    exam_stats = context['exam'].statistics()
    context['exam_max'] = exam_stats['maximum']
    context['exam_min'] = exam_stats['minimum']
    context['exam_average'] = exam_stats['average']
    try:
      context['sessions'] = Session.objects.filter(exam=context['exam']).order_by('trainee__lastname')
    except Session.DoesNotExist:
      context['sessions'] = []
    return context

class ExamRetakeView(DetailView):
  model = Exam
  context_object_name = 'exam'

  def get_context_data(self, **kwargs):
    context = super(ExamRetakeView, self).get_context_data(**kwargs)
    context['exam'] = Exam.objects.get(pk=self.kwargs['pk'])
    try:
      context['sessions'] = Session.objects.filter(exam=context['exam']).order_by('trainee__lastname')
    except Session.DoesNotExist:
      context['sessions'] = []
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
  template_name = 'exams/exam.html'
  model = Session
  context_object_name = 'exam'
  fields = []

  def _get_exam(self):
    return Exam.objects.get(pk=self.kwargs['pk'])

  def _get_most_recent_session(self):
    try:
      sessions = Session.objects.filter(
        exam=self._get_exam(),
        trainee=self.request.user).order_by('-id')
      if sessions:
        return sessions[0]
    except Session.DoesNotExist:
      pass

    return None

  def _get_session(self):
    if not self._exam_available():
      return None

    session = self._get_most_recent_session()
    # Create a new exam session if there is no editable exam session
    if session == None or session.is_complete:
      retake_count = session.retake_number + 1 if session != None else 0
      new_session = Session(exam=self._get_exam(),
        trainee=trainee_from_user(self.request.user),
        is_complete=False,
        is_submitted_online=True,
        retake_number=retake_count)
      if session != None:
        new_session.grade = session.grade
      new_session.save()

      # copy over previous responses
      if session != None:
        responses = Responses.objects.filter(session=session)
        for response in responses:
          response.pk = None
          response.session = new_session
          response.save()

    return session

  def _exam_available(self):
    exam = self._get_exam()
    user = self.request.user

    if not trainee_can_take_exam(user, exam):
      return False

    # if the exam is in progress or doesn't exist, we're in business
    most_recent_session = self._get_most_recent_session()

    if (most_recent_session == None or not most_recent_session.is_complete):
      return True

    return retake_available(exam, user)

  def _is_retake(self):
    return self._get_session().retake_number > 0

  def get_context_data(self, **kwargs):
    context = super(TakeExamView, self).get_context_data(**kwargs)

    exams = Exam.objects.prefetch_related('sections').get(pk=self.kwargs['pk'])

    return get_exam_context_data(context,
                   self._get_exam(),
                   self._exam_available(),
                   self._get_session(),
                   "Retake" if self._is_retake() else "Take", False)

  def post(self, request, *args, **kwargs):
    is_successful = True
    finalize = False
    #print "request.POST is " + str(request.POST)
    #if 'Submit' in request.POST:
    #  print "i reach here"
    #  finalize = True

    trainee = self.request.user
    exam = self._get_exam()
    session = self._get_session()

    try:
      body_unicode = request.body.decode('utf-8')
      body = json.loads(body_unicode)
    except ValueError:
      print "No answers submitted yet..."
      body = []

    for key in body:
      print "key: " + str(key) + "; value: " + str(body[key])
      if key == "Submit":
        if body[key] == 'true':
          finalize = True
      else:
        try:
          section = Section.objects.get(id=int(key))
          save_responses(session, section, body[key])
        except Section.DoesNotExist:
          is_successful = False

    #to be placed in "if finalize:" section
    total_session_score = 0
    for key in body:
      if key != "Submit":
        try:
          section = Section.objects.get(id=int(key))
          if section.section_type != 'E':
            resp_obj_to_grade = Responses.objects.filter(section=section)[0]
            responses_to_grade = resp_obj_to_grade.responses
            print "RESPONSES TO GRADE: " + str(responses_to_grade)
            score_for_section = 0
            for i in range(1, len(responses_to_grade) + 1):
              print "response: " + responses_to_grade[str(i)].replace('\"','')
              print "answer: " + ast.literal_eval(section.questions[str(i)])["answer"]
              question_data = ast.literal_eval(section.questions[str(i)])
              #see if response of trainee equals answer; if it does assign point
              if section.section_type == 'FB':
                responses_to_blanks = responses_to_grade[str(i)].replace('\"','').lower().split(';')
                answers_to_blanks = str(question_data["answer"]).lower().split(';')
                total_blanks = len(responses_to_blanks)
                number_correct = 0
                for i in range(0, total_blanks):
                  if responses_to_blanks[i] == answers_to_blanks[i]:
                    number_correct += 1
                print "number correct: " + str(number_correct)
                #TODO: convert to decimal
                print "score: " + str(number_correct/float(total_blanks))
                score_for_section += (number_correct/float(total_blanks))
              elif (responses_to_grade[str(i)].replace('\"','').lower() == str(question_data["answer"]).lower()):
                #print "Correct answer to question: " + str(i)
                score_for_section += int(question_data["points"])
            resp_obj_to_grade.score = score_for_section
            total_session_score += score_for_section
            resp_obj_to_grade.save()
        except Section.DoesNotExist:
          is_successful = False

    print "finalize is: " + str(finalize)
    if finalize:
      session = self._get_session()
      session.is_complete = True
      session.grade = total_session_score
      session.save()

      #if section.section_type == 'E':
      #  responses = request.POST.getlist('response')
      #elif section.section_type == 'MC':
      #  responses = request.POST.getlist('mc-a')
      #elif section.section_type == 'M':
      #  responses = request.POST.getlist('matching_answer_field')
      #elif section.section_type == 'TF':
      #  responses = request.POST.getlist('true')
      #  responses = request.POST.getlist('false')
      #print 'initial responses: ' + str(responses)
      #responses = [{'response': r} for r in responses]
      #print "RESPONSES IN SECTION: " + str(key) + " - " + str(responses)
      #save_responses(session, section, responses)
      # Grader's request is that eventually this would be displayed as a list for
      # their reference, so instead of deleting, just mark as complete
      # try:
      #   retake = Retake.objects.filter(exam=exam, trainee=trainee)
      #   if retake:
      #     retake[0].is_complete = True
      #     retake[0].save()
      # except Retake.DoesNotExist:
      #   pass

      try:
        retake = Retake.objects.filter(exam=exam, trainee=trainee).delete()
      except Retake.DoesNotExist:
        pass

      messages.success(request, 'Exam submitted successfully.')
      print "exam submitted successfully"
      return HttpResponseRedirect(reverse_lazy('exams:manage'))
    else:
      messages.success(request, 'Exam progress saved.')
      print "exam progress saved"
      return self.get(request, *args, **kwargs)

class GradeExamView(SuccessMessageMixin, GroupRequiredMixin, CreateView):
  template_name = 'exams/exam.html'
  model = Session
  context_object_name = 'exam'
  fields = []
  group_required = [u'exam_graders', u'administration']

  def _get_exam(self):
    session = Session.objects.get(pk=self.kwargs['pk'])
    return Exam.objects.get(pk=session.exam.id)

  def _get_session(self):
    return Session.objects.get(pk=self.kwargs['pk'])

  def _exam_available(self):
    # TODO: should sanity check that user has grader/TA permissions
    return True

  def get_context_data(self, **kwargs):
    context = super(GradeExamView, self).get_context_data(**kwargs)
    return get_exam_context_data(context,
                   self._get_exam(),
                   self._exam_available(),
                   self._get_session(),
                   "Grade", True)

  # Returns true if every score has a valid value
  def calculate_score(self, request, responses, session, section):
    total_score = 0
    can_finalize = True
    for index, response in enumerate(responses):
      response_parsed = response;
      if (response_parsed["score"].isdigit()):
        total_score += int(response_parsed["score"])
      else:
        can_finalize = False
        if response_parsed["score"] != "":
          messages.add_message(request, messages.ERROR,
            "Invalid grade value for question" + str(index + 1) + ".")

    try:
      responses_obj = Responses.objects.get(session=session, section=section)
    except Responses.DoesNotExist:
      responses_obj = Responses(session=session, section=section, score=0)

    if (responses_obj.score != total_score):
      session.grade = session.grade - responses_obj.score + total_score
      session.save()

      responses_obj.score = total_score;
      responses_obj.save()

    return can_finalize

  def post(self, request, *args, **kwargs):
    is_successful = True
    finalize = False
    if 'Submit' in request.POST:
      finalize = True

    session = Session.objects.get(pk=self.kwargs['pk'])
    exam = Exam.objects.get(pk=session.exam.id)

    # TODO: for now, only supporting 1-sectioned exams
    try:
      section = Section.objects.get(exam=exam, section_index=0)
    except Section.DoesNotExist:
      is_successful = False

    P = request.POST
    scores = P.getlist('question-score')
    r_len = len(scores)
    comments = P.getlist('grader-comment')
    responses = session.responses.all()

    resp_s = []

    for i, r in enumerate(responses):
      resp = r.responses
      for i in range(r_len):
        resp_i = eval(resp[str(i+1)])
        #TODO
        print str(scores[i])
        print str(type(scores[i]))
        resp_i['score'] = Decimal(str(scores[i]))
        resp_i['comment'] = comments[i]

        resp_s.append(resp_i)

    print 'resps', resp_s
    save_responses(session, section, resp_s)

    # responses = request.POST.getlist('response_json')

    if (not self.calculate_score(request, resp_s, session, section)) and finalize:
      finalize = False
      messages.add_message(request, messages.ERROR,
        "Cannot finalize grading: at least one invalid grade value.")

    if finalize:
      session = self._get_session()
      session.is_graded = True
      session.save()

      messages.success(request, 'Exam grading submitted successfully.')
      return HttpResponseRedirect(reverse_lazy('exams:grades',
                      kwargs={'pk': exam.id}))
    else:
      messages.success(request, 'Exam grading progress saved.')
      return self.get(request, *args, **kwargs)

class GradedExamView(SuccessMessageMixin, GroupRequiredMixin, CreateView):
  template_name = 'exams/exam_graded.html'
  model = Session
  context_object_name = 'exam'
  fields = []
  group_required = [u'exam_graders', u'administration']

  def _get_exam(self):
    session = Session.objects.get(pk=self.kwargs['pk'])
    return Exam.objects.get(pk=session.exam.id)

  def _get_session(self):
    return Session.objects.get(pk=self.kwargs['pk'])

  def _exam_available(self):
    # TODO: should sanity check that user has grader/TA permissions
    return True

  def get_context_data(self, **kwargs):
    context = super(GradedExamView, self).get_context_data(**kwargs)

    return get_exam_context_data(context,
                   self._get_exam(),
                   self._exam_available(),
                   self._get_session(),
                   "Grade", True)

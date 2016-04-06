import abc
import datetime
import json

from collections import namedtuple
from datetime import timedelta
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.forms.models import formset_factory
from django.shortcuts import redirect
from django_select2 import *
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView

from braces.views import LoginRequiredMixin

from .models import Class
from terms.models import Term
from .models import Trainee
from .models import Exam, Section, Session, Responses, Retake
from .forms import TraineeSelectForm, ExamCreateForm, SectionFormSet

from django.contrib.postgres.fields import HStoreField
from exams.utils import get_responses, get_exam_questions, get_exam_context_data, retake_available

# PDF generation
import cStringIO as StringIO

from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
from cgi import escape

class ExamCreateView(LoginRequiredMixin, FormView):
    """TODO: be able to dynamically add a section """

    template_name = 'exams/exam_form.html'
    form_class = ExamCreateForm
    success_url = reverse_lazy('exams:exam_template_list')

    def get_context_data(self, **kwargs):
        # TODO -- load existing data
        context = super(ExamCreateView, self).get_context_data(**kwargs)

        if self.request.POST:
            context['formset'] = SectionFormSet(self.request.POST)
        else:
            context['formset'] = SectionFormSet()

        # examInfo contains:
        #     - the name of the class
        #     - is_open
        #     - is_midterm
        #     - questions object
        #context['examInfo'] = zip(class_id, is_open, is_midterm, questions)

        # class = class.get....
        # might be better to pass the class object?
        # to get pk -> class.id

        classes = Class.objects.filter(term=Term.current_term())

        context['data'] = classes
        return context

    def get_form(self, form_class):
        """
        TODO--load already existing data.
        """

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

        training_class = Class.objects.get(id=request.POST.get('training-class'))
        exam_name = request.POST.get('exam-name', '')
        # bool(request.POST.get('exam-category')=='1')
        exam_category = request.POST.get('exam-category','')
        
        is_open = request.POST.get('is-open','')
        duration = timedelta(minutes=int(request.POST.get('duration','')))
        
        # questions are saved in an array
        questions = request.POST.getlist('questions')
        question_count = len(questions)

        '''
        TODO code up section_index and description
        '''
        section_index = 0
        description = "Place Holder"
        # section_index = int(request.POST.get('section-index', ''))
        # description = request.POST.get('description', '')

        exam = Exam(training_class=training_class,
            name=exam_name,
            is_open=is_open,
            duration=duration,
            category=exam_category)
        exam.save()

        section = Section(exam=exam,
            description=description,
            section_index=section_index,
            question_count=question_count)
        for question in questions:
            section.questions = {question : '1'}
        section.save()

        session = Session(exam=exam, 
                trainee=self.request.user.trainee,
                is_complete=False,
                is_submitted_online=True,
                retake_number=1)
        session.save()

        '''
        TODO getting total_score for the exam.
             Not user set...is the value assigned for each
             question stored with the questions variable?
             How are exams graded?
        '''

        return self.get(request, *args, **kwargs)

class ExamTemplateListView(ListView):
    template_name = 'exams/exam_template_list.html'
    model = Exam
    context_object_name = 'exam_templates'

    def get_queryset(self):
        return Exam.objects.all()

    def exam_in_retakes(self, retakes, exam):
        for retake in retakes:
            if retake.exam == exam and not retake.is_complete:
                return True
        return False

    def get_context_data(self, **kwargs):
        # TODO: there's gotta be a better way of doing this
        context = super(ExamTemplateListView, self).get_context_data(**kwargs)
        context['available'] = []
        retakes = Retake.objects.filter(trainee=self.request.user.trainee, 
                                            is_complete=False)
        for exam in Exam.objects.all():
            if (not exam.is_complete(self.request.user.trainee)) or \
                       (self.exam_in_retakes(retakes, exam)):
                   context['available'].append(True)
            else:
                context['available'].append(False)
        return context

class SingleExamGradesListView(CreateView, SuccessMessageMixin):
    template_name = 'exams/single_exam_grades.html'
    model = Exam
    context_object_name = 'exam_grades'
    fields = []
    success_url = reverse_lazy('exams:exam_template_list')
    success_message = 'Exam grades updated.'

    def get_context_data(self, **kwargs):
        context = super(SingleExamGradesListView, self).get_context_data(**kwargs)
        exam = Exam.objects.get(pk=self.kwargs['pk'])
        context['exam'] = exam

        # TODO: This needs further filtering by class.
        # TODO: Is there a more efficient way of doing this?  Prefetch_related,
        # maybe?  Is there a way to apply a filter to prefetch related?
        # annotate????
        first_sessions = []
        second_sessions = []
        trainees = Trainee.objects.filter(active=True).order_by('account__lastname')
        for trainee in trainees:
            try:
                sessions = Session.objects.filter(exam=exam, is_complete=True, 
                    trainee=trainee).order_by('trainee__account__lastname')
                if sessions.count() > 0:
                    first_sessions.append(sessions[0])
                else:
                    first_sessions.append(None)

                if sessions.count() > 1:
                    second_sessions.append(sessions[sessions.count() - 1])
                else:
                    second_sessions.append(None)
            except Session.DoesNotExist:
                first_sessions.append(None)
                second_sessions.append(None)

        context['data'] = zip(trainees, first_sessions, second_sessions)

        try:
            context['sessions'] = Session.objects.filter(exam=context['exam'], is_complete=True, trainee=trainee).order_by('trainee__account__lastname')
        except Session.DoesNotExist:
            context['sessions'] = []
        return context

    def post(self, request, *args, **kwargs):
        # User Error?
        if request.method != 'POST':
            messages.add_message(request, messages.ERROR, 'Nothing saved.')
            return redirect('exams:exams_template_list')

        # TODO: helper functions?
        if 'delete-session-id' in request.POST:
            session_id = int(request.POST['delete-session-id'])
            try:
                Session.objects.get(id=session_id).delete()
            except Session.DoesNotExist:
                pass
            messages.success(request, 'Exam deleted')
        elif 'unfinalize-session-id' in request.POST:
            session_id = int(request.POST['unfinalize-session-id'])

            # TODO: probably should handle the non-submitted-online cases as a javascript
            # popup on the page.  For now, it will unfinalize the grade, but the next time
            # a grader presses save it will get finalized whether or not the value was 
            # changed.

            try:
                session = Session.objects.get(id=session_id)
                session.is_graded = False
                session.save()

                if session.is_submitted_online:
                    return HttpResponseRedirect(
                        reverse_lazy('exams:grade_exam', kwargs={'pk': session.id}))
            except Session.DoesNotExist:
                pass
        elif 'retake-trainee-id' in request.POST:
            # TODO: need a way to see the retake list
            # TODO: check to see if one is already existing
            trainee_id = int(request.POST['retake-trainee-id'])
            try:
                trainee = Trainee.objects.get(id=trainee_id)
                exam = Exam.objects.get(pk=self.kwargs['pk'])
                exam_retake = Retake(trainee=trainee, exam=exam)
                exam_retake.save()
            except Trainee.DoesNotExist:
                pass
        else:
            grades = request.POST.getlist('new-grade')
            trainee_ids = request.POST.getlist('trainee-id')
            for index, trainee_id in enumerate(trainee_ids):
                if not grades[index].isdigit():
                    continue

                try:
                    trainee = Trainee.objects.get(id=trainee_id)
                    exam = Exam.objects.get(pk=self.kwargs['pk'])

                    try:
                        sessions = Session.objects.filter(exam=exam, is_complete=True, trainee=trainee).order_by('-retake_number')
                        if (sessions.count() == 0):
                            retake_number = 0
                        else:
                            retake_number = sessions[0].retake_number + 1
                    except Session.DoesNotExist:
                        retake_number = 0

                    session = Session(exam=exam, 
                        trainee=trainee,
                        is_submitted_online=False,
                        is_complete=True,
                        is_graded=True,
                        retake_number=retake_number,
                        grade=int(grades[index])
                        )
                    session.save()
                except Trainee.DoesNotExist:
                    # TODO: error message
                    pass

            grades2 = request.POST.getlist('session-id-grade')
            session_ids = request.POST.getlist('session-id')

            for index, session_id in enumerate(session_ids):
                try:
                    session = Session.objects.get(id=session_id)
                    grade = int(grades2[index]) if grades2[index].isdigit() else 0
                    session.grade = grade
                    session.save()
                except Session.DoesNotExist:
                    #TODO: error message
                    pass
            messages.success(request, 'Exam grades saved.')

        return self.get(request, *args, **kwargs)

class GenerateGradeReports(CreateView, SuccessMessageMixin):
    model = Session
    template_name = 'exams/exam_grade_reports.html'
    success_url = reverse_lazy('exams:exam_grade_reports')

    def get_context_data(self, **kwargs):
        context = super(GenerateGradeReports, self).get_context_data(**kwargs)
        context['trainee_select_form'] = TraineeSelectForm()
        context['trainees'] = TraineeSelectForm
        trainee_list = self.request.GET.getlist('trainees')
        sessions = {}
        for trainee in trainee_list:
            try:
                sessions[Trainee.objects.get(id=trainee)] = Session.objects.filter(trainee_id=trainee)
            except Session.DoesNotExist:
                sessions[trainee] = {}                
        context['sessions'] = sessions
        return context

class GenerateOverview(DetailView):
    template_name = 'exams/exam_overview.html'
    model = Exam
    fields = []
    context_object_name = 'exam'

    def get_context_data(self, **kwargs):
        context = super(GenerateOverview, self).get_context_data(**kwargs)
        context['exam'] = Exam.objects.get(pk=self.kwargs['pk'])
        exam_stats = context['exam'].statistics()
        context['exam_max'] = exam_stats['maximum']
        context['exam_min'] = exam_stats['minimum']
        context['exam_average'] = exam_stats['average']
        try:
            context['sessions'] = Session.objects.filter(exam=context['exam']).order_by('trainee__account__lastname')
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
            context['sessions'] = Session.objects.filter(exam=context['exam']).order_by('trainee__account__lastname')
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

    def _is_taking_exam(self):
        return True

    def _get_exam(self):
        return Exam.objects.get(pk=self.kwargs['pk'])

    def _get_most_recent_session(self):
        try:
            sessions = Session.objects.filter(
                exam=self._get_exam(), 
                trainee=self.request.user.trainee).order_by('-id')
            if sessions:
                return sessions[0]
        except Session.DoesNotExist:
            pass

        return None

    def _get_session(self):
        session = self._get_most_recent_session()
        # Create a new exam session if there is no editable exam session
        if session == None or session.is_complete:
            retake_count = session.retake_number + 1 if session != None else 0
            session = Session(exam=self._get_exam(), 
                trainee=self.request.user.trainee,
                is_complete=False,
                is_submitted_online=True,
                retake_number=retake_count)
            session.save()

        return session

    def _exam_available(self):
        # TODO: Check that this exam is applicable to given trainee and is
        # active

        # if the exam is in progress or doesn't exist, we're in business
        most_recent_session = self._get_most_recent_session()

        if (most_recent_session == None or not most_recent_session.is_complete):
            return True

        return retake_availale(self._get_exam(), self.request.user.trainee)

    def _is_retake(self):
        return retake_available(self._get_exam(), self.request.user.trainee)

    def _action_complete(self, post):
        return True if 'Submit' in post else False

    def _prepost_processing(self):
        trainee = self.request.user.trainee
        exam = self._get_exam()

        try:
            retake = Retake.objects.get(trainee=trainee,
                        exam=exam,
                        is_complete=False)
        except Retake.DoesNotExist:
            return False

        return True

    def get_context_data(self, **kwargs):
        context = super(TakeExamView, self).get_context_data(**kwargs)

        return get_exam_context_data(context, 
                                     self._get_exam(), 
                                     self._exam_available(), 
                                     self._get_session(), 
                                     self.request.user.trainee, 
                                     "Retake" if self._is_retake() else "Take")

    def post(self, request, *args, **kwargs):
        is_successful = True
        finalize = False
        if 'Submit' in request.POST:
            finalize = True

        trainee = self.request.user.trainee
        exam = self._get_exam()
        session = self._get_session()

        # TODO: for now, only supporting 1-sectioned exams
        try:
            section = Section.objects.get(exam=exam, section_index=0)
        except Section.DoesNotExist:
            is_successful = False

        responses = request.POST.getlist('response')
        comments = request.POST.getlist('grader-comment')
        scores = request.POST.getlist('question-score')

        try:
            responses_obj = Responses.objects.get(session=session, trainee=trainee, section=section)
        except Responses.DoesNotExist:
            responses_obj = Responses(session=session, trainee=trainee, section=section, score=0)

        responses_hstore = responses_obj.responses
        if responses_hstore is None:
            responses_hstore = {}

        for index, response in enumerate(responses):
            response_pkg = {}
            response_pkg["response"] = response
            responses_hstore[str(index+1)] = json.dumps(response_pkg)

        responses_obj.responses = responses_hstore
        responses_obj.save()

        if finalize:
            session = self._get_session()
            session.is_complete = True
            session.save()

            #todo delete retake

            messages.success(request, 'Exam submitted successfully.')
            return HttpResponseRedirect(reverse_lazy('exams:exam_template_list'))
        else:
            messages.success(request, 'Exam progress saved.')
            return self.get(request, *args, **kwargs)        

    def _complete(self):
        session = self._get_session()
        session.is_complete = True
        session.save()

        try:
            Retake.objects.filter(trainee=self.request.user.trainee,
                exam=self._get_exam()).delete()

            # TODO: Graders prefer a retake list over deleting this... so when
            # that's done, switch in this code for the code above.  :)
            #retake = Retake.objects.get(trainee=self.request.user.trainee,
            #            exam_template=self._get_exam_template())
            #retake.is_complete = True
            #retake.save()
        except Retake.DoesNotExist:
            pass

        return True


class GradeExamView(SuccessMessageMixin, CreateView):
    template_name = 'exams/exam.html'
    model = Session
    context_object_name = 'exam'
    fields = []

    def _is_taking_exam(self):
        return False

    def _get_exam(self):
        session = Session.objects.get(pk=self.kwargs['pk'])
        return Exam.objects.get(pk=session.exam.id)

    def _get_session(self):
        return Session.objects.get(pk=self.kwargs['pk'])

    def _exam_available(self):
        # TODO: should sanity check that user has grader/TA permissions
        return True

    def _action_complete(self, post):
        # TODO: This should be finalize in the grade view
        return True if 'Submit' in post else False

    def _prepost_processing(self):
        return True

    def _process_post_data(self, responses, grader_extras, scores, session_pk, trainee_pk):
        is_successful = True
        total_score = 0
        for i in range(len(grader_extras)):
            response_key = "_".join([str(session_pk), str(trainee_pk), str(i + 1)])
            try:
                response = Response.objects.get(pk=response_key)
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
            except Response.DoesNotExist:
                # TODO: this should never happen.  Is there a NotReached in python?
                pass

        # Save total score
        session = self._get_session()
        session.grade = total_score
        session.save()
        return is_successful

    def get_context_data(self, **kwargs):
        context = super(GradeExamView, self).get_context_data(**kwargs)

        return get_exam_context_data(context, 
                                     self._get_exam(), 
                                     self._exam_available(), 
                                     self._get_session(), 
                                     self.request.user.trainee, 
                                     "Grade")

    def post(self, request, *args, **kwargs):
        is_successful = True
        finalize = False
        if 'Finalize' in request.POST:
            finalize = True

        session = Session.objects.get(pk=self.kwargs['pk'])
        exam = Exam.objects.get(pk=session.exam.id)
        trainee = session.trainee

        # TODO: for now, only supporting 1-sectioned exams
        try:
            section = Section.objects.get(exam=exam, section_index=0)
        except Section.DoesNotExist:
            is_successful = False

        responses = request.POST.getlist('response')
        comments = request.POST.getlist('grader-comment')
        scores = request.POST.getlist('question-score')

        try:
            responses_obj = Responses.objects.get(session=session, trainee=trainee, section=section)
        except Responses.DoesNotExist:
            is_successful = False
            # TODO: Need a graceful fail here

        responses_hstore = responses_obj.responses
        if responses_hstore is None:
            is_successful = False
            # TODO: Need a graceful fail here
            responses_hstore = {}

        index = 1
        for comment, score in zip(comments, scores):
            response_pkg = json.loads(responses_hstore[str(index)])
            response_pkg["comment"] = comment
            response_pkg["score"] = score
            responses_hstore[str(index)] = json.dumps(response_pkg)
            index += 1

        responses_obj.responses = responses_hstore
        responses_obj.save()

        if finalize:
            session = self._get_session()
            session.is_graded = True
            session.save()

            #todo delete retake

            messages.success(request, 'Exam submitted successfully.')
            return HttpResponseRedirect(reverse_lazy('exams:exam_template_list'))
        else:
            messages.success(request, 'Exam progress saved.')
            return self.get(request, *args, **kwargs)

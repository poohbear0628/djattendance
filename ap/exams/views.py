import abc
from collections import namedtuple
import datetime

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

from .models import Trainee
from .models import Exam, Section, Session, Responses, Retake
from .forms import TraineeSelectForm, ExamCreateForm, SectionFormSet


from exams.utils import get_response_tuple, get_exam_questions

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

class SingleExamBaseView(SuccessMessageMixin, CreateView):
    """This class is the base view for taking and grading an exam."""

    template_name = 'exams/exam.html'
    model = Session
    context_object_name = 'exam'
    fields = []

    @abc.abstractmethod
    def _is_taking_exam(self):
        """Return true if the action is to take the exam"""

    @abc.abstractmethod
    def _get_exam(self):
        """Returns the applicable exam"""

    @abc.abstractmethod
    def _get_session(self):
        """Returns the exam session to be operated on, creating if applicable"""

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
    def _prepost_processing(self):
        """Does any pre-post processing.  Returns False if the post should not
        continue"""

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

    # context data: exam, questions, responses, whether or not the session is complete
    def get_context_data(self, **kwargs):
        context = super(SingleExamBaseView, self).get_context_data(**kwargs)

        context['taking'] = self._is_taking_exam()
        exam = self._get_exam()
        context['exam'] = exam

        if not self._exam_available():
            context['exam_available'] = False
            return context

        context['exam_available'] = True

        session = self._get_session()
        if session:
            session_pk = session.id
        else:
            session_pk = None

        context['permissions'] = self._permissions_matrix
        context['visibility'] = self._visibility_matrix

        # TODO: this shouldn't take pks, but the exam/template themselves
        # TODO2: This should take the visibility matrix to determine whether
        # to send the data at all
        questions = get_exam_questions(exam.id)
        responses, grader_extras, scores = get_response_tuple(exam.id, 
            session_pk, self.request.user.trainee.id)

        context['data'] = zip(questions, responses, grader_extras, scores)
        return context

    def post(self, request, *args, **kwargs):
        action_complete = self._action_complete(request.POST)

        if self._prepost_processing():
            # Get exam session object that we should operate on
            session = self._get_session()

            # Process post data
            responses = request.POST.getlist('response')
            comments = request.POST.getlist('grader-comment')
            scores = request.POST.getlist('question-score')

            is_successful = self._process_post_data(responses, comments, scores, 
                session.id, self.request.user.trainee.id)

            # Action cannot be completed if inputed data has errors
            if (not is_successful):
                action_complete = False

            # Validate and complete (submit/finalize) submission
            if (action_complete and (not self._complete())):
                is_successful = False
                action_complete = False
        else:
            is_successful = False

        # Redirect
        return self._redirect(action_complete, not is_successful, request, 
            *args, **kwargs)

    class Meta:
        abstract = True

class TakeExamView(SingleExamBaseView):
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

        try:
            retake = Retake.objects.get(
                        exam=self._get_exam(),
                        trainee=self.request.user.trainee,
                        is_complete=False)
            if retake != None:
                return True
        except Retake.DoesNotExist:
            pass

        return False

    def _visibility_matrix(self):
        return [True, False, False]

    def _permissions_matrix(self):
        return [True, False, False]

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

    def _process_post_data(self, responses, grader_extras, scores, session_pk, trainee_pk):

        # in take exam view, it is only possible to make changes to responses
        for i in range(len(responses)):
            response_key = "_".join([str(session_pk), str(trainee_pk), str(i + 1)])
            try:
                response = Response.objects.get(pk=response_key)
                response.response = responses[i]
            except Response.DoesNotExist:
                response = Response(pk=response_key, response=responses[i])
            
            response.save()

        return True

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

    def _get_exam(self):
        session = Session.objects.get(pk=self.kwargs['pk'])
        return Exam.objects.get(pk=session.exam.id)

    def _get_session(self):
        return Session.objects.get(pk=self.kwargs['pk'])

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

    # Validate that all questions have been graded and mark grade as finalized
    def _complete(self):
        session = self._get_session()

        # FUTURE: Validate that all questions have been assigned a valid 
        # score and that a comment is available for incomplete scores
        session.is_graded = True
        session.save()
        return True

    def _redirect(self, action_complete, has_error, request, *args, **kwargs):
        if (has_error):
            return self.get(request, *args, **kwargs)

        if (action_complete):
            messages.success(request, 'Exam grading finalized.')
            return HttpResponseRedirect(
                reverse_lazy('exams:single_exam_grades', 
                    kwargs={'pk': self._get_exam().id}))
        else:
            messages.success(request, 'Exam grading progress saved.')
            return self.get(request, *args, **kwargs)

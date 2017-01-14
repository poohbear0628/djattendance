import datetime
from datetime import date

from aputils.trainee_utils import trainee_from_user, is_trainee
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy, reverse

from rest_framework import viewsets
from rest_framework.decorators import detail_route

from accounts.models import Trainee
from terms.models import Term
from .models import Classnotes
from .forms import NewClassnotesForm, EditClassnotesForm, ApproveClassnotesForm
from .serializers import ClassnotesSerializer

from attendance.utils import Period
from classnotes.utils import assign_classnotes, approve_classnotes

class EditView(SuccessMessageMixin, FormView):
	template_name = 'classnotes/classnotes_form.html'
	form_class = NewClassnotesForm
	success_url = reverse_lazy('classnotes:classnotes-list')
	success_message = "Class notes saved Successfully!"

	def get_context_data(self, **kwargs):
		context = super(ClassnotesEditView, self).get_context_data(**kwargs)
		classnotes = Classnotes.objects.get(pk=self.kwargs['pk'])
		context['classname'] = classnotes.classname
		context['classdate'] = classnotes.classdate
		context['content'] = classnotes.content
		context['comments'] = classnotes.TA_comment
		return context		

	# def get_form(self, form_class):
	# 	return form_class(**kargs)

	# def form_valid(self, form):
 #        return super(ClassnotesEditView, self).form_valid(form)

	def post(self, request, *args, **kwargs):
		pk = self.kwargs['pk']
		P = request.post	
		content = P.get('content', '')

		classnotes = Classnotes.objects.get(pk=pk)
		classnotes.content = content
		classnotes.date_submitted = datetime.now()
		classnotes.status = 'P'
		classnotes.save()

class ApproveView(EditView, SuccessMessageMixin, FormView):
	template_name = 'classnotes/classnotes_approve.html'
	form_class = ApproveClassnotesForm
	success_url = reverse_lazy('classnotes:classnotes-list')
	success_message = 'Class notes Reviewed!'

	# def get_context_data(self, **kwargs):
	# 	context = super(EditView, self).get_context_data(**kwargs)
	# 	return context

	# def get_form(self, form_class):
	# 	return super(ClassnotesEditView, self).get_form(form_class)
	
	# def form_valid(self, form):
	# 	return super(ClassnotesEditView, self).form_valid(form)

	def post(self, request, *args, **kwargs):
		pk = self.kwargs['pk']
		P = request.post	
		comments = P.get('comments', '')
		status = P.get('status', '')

		classnotes = Classnotes.objects.get(pk=pk)
		classnotes.TA_comment = comments
		if status == 'A':
			classnotes.status = 'A'
		if status == 'F':
			classnotes.status = 'F'
		classnotes.save()		

class ClassnotesListView(ListView):
	template_name = 'classnotes/classnotes_list.html'
	model = Classnotes
	def post(self, request, *args, **kwargs):
		"""
		'approve' when an approve button is pressed 'delete' when a delete
		button is pressed 'assign_classnotes' when assgning classnotes
		"""
		if 'approve' in request.POST:
			for value in request.POST.getlist('selection'):
				classnotes = Classnotes.objects.get(pk=value)
				approve_classnotes(classnotes)
			messages.success(request, "Checked Classnotes(s) Approved!")
		if 'delete' in request.POST:
			for value in request.POST.getlist('selection'):
				Classnotes.objects.get(pk=value).delete()
			messages.success(request, "Checked Classnotes(s) Deleted!")
		if 'assign_classnotes' in request.POST:
			# trainee = trainee_from_user(self.request.user)
			term = Term.current_term()
			period = Period(term).period_of_date(date.today())
			assign_classnotes(period)
			messages.success(request, "Classnotes Assigned According to Attendance!")
		return self.get(request, *args, **kwargs)

    #profile is the user that's currently logged in
	def get_context_data(self, **kwargs):
		context = super(ClassnotesListView, self).get_context_data(**kwargs)
		try:
			context['current_period'] = Period(Term.current_term()).period_of_date(datetime.datetime.now().date())
		except ValueError:
			# ValueError thrown if current date is not in term (interim)
			# return last period of previous period
			context['current_period'] = Period.last_period()
		return context



class ClassnotesCreateView(SuccessMessageMixin, CreateView):
	"""
		From ClassnotesListView.
		gets: classname and classdate to display on form template
		post: classname, classdate, content
		Creates a new Classnotes object
	"""

	model = Classnotes
	form_class = NewClassnotesForm
	success_url = reverse_lazy('classnotes:classnotes-list')
	success_message = "Class notes saved Successfully!"
	template_name = 'classnotes/classnotes_form.html'

	def get_initial(self):
		"""
		Returns the initial data to use for forms on this view.
		"""
		initial = super(ClassnotesCreateView, self).get_initial()
		initial['trainee'] = trainee_from_user(self.request.user)
		initial['classname'] = classnotes.classname
		initial['classdate'] = classnotes.classdate
		return initial

	def get_context_data(self, **kwargs):
		context = super(ClassnotesCreateView, self).get_context_data(**kwargs)
		# classnotes = Classnotes.objects.get(pk=self.kwargs['pk'])
		# context['classname'] = classnotes.classname
		# context['classdate'] = classnotes.classdate
		return context

	def get_form(self, form_class):
		"""
		Returns an instance of the form to be used in this view.
		"""
		kargs = self.get_form_kwargs()
		kargs['trainee'] = trainee_from_user(self.request.user)
		return form_class(**kargs)

	def form_valid(self, form):
		# classnotes = form.save(commit=False)
		
		classnotes = Classnotes.objects.get(pk=self.kwargs['pk'])
		# Check if minimum words are met
		if form.is_valid:
			# data = form.cleaned_data
			# classnotes.content = data['content']
			classnotes.date_submitted = datetime.datetime.now()
			classnotes.save()
		return super(ClassnotesCreateView, self).form_valid(form)


# class ClassnotesListView(ListView):
# 	model = Classnotes
# 	template_name = 'classnotes/classnotes_list.html'
# 	context_object_name = 'classnotes'

# 	def get_queryset(self):
# 		user = self.request.user
# 		if is_trainee(self.request.user):
# 			trainee = trainee_from_user(self.request.user)
# 			return Classnotes.objects.filter(trainee=trainee)
# 		else:
# 			return Classnotes.objects.filter(status__in=['P', 'F']).order_by('-date_assigned')

    # def get_template_names(self):
    #     if is_trainee(self.request.user):
    #         return ['classnotes/classnotes_list.html']
    #     else:
    #         return ['classnotes/classnotes_list.htmll']

class ClassNoteViewSet(viewsets.ModelViewSet):
    queryset = Classnotes.objects.all()
    serializer_class = ClassnotesSerializer

    @detail_route(methods=['post'])
    def save_note(self, request, pk=None):
        instance = self.get_object()
        if instance.status == 'U':
            instance.content = request.data.get('content')
            instance.save()
            status = 'Saved at %s!' % time.strftime('%I:%M:%S %p')
        else:
            status = 'Class note is already submitted'
        return Response({'status': status})

    @detail_route(methods=['post'])
    def submit_note(self, request, pk=None):
        instance = self.get_object()
        if instance.status == 'U':
            instance.content = request.data.get('content')
            instance.status = 'P'
            instance.submitting_paper_copy = request.data.get('submitting_paper_copy') == 'true'
            instance.date_submitted = datetime.now()
            instance.save()
            status = 'Submitted at %s!' % time.strftime('%I:%M:%S %p')
        else:
            status = 'Class note is already submitted'
        return Response({'status': status})

    @detail_route(methods=['post'])
    def approve_note(self, request, pk=None):
        instance = self.get_object()
        if instance.status != 'A':
            instance.status = 'A'
            instance.TA_comment = request.data.get('TA_comment')
            instance.save()
            status = 'Approved!'
        else:
            status = 'Class note is already approved'
        return Response({'status': status})

    @detail_route(methods=['post'])
    def mark_note(self, request, pk=None):
        instance = self.get_object()
        if instance.status != 'F':
            instance.status = 'F'
            instance.TA_comment = request.data.get('TA_comment')
            instance.save()
            status = 'Marked for fellowship!'
        else:
            status = 'Class note is already marked for fellowship'
        return Response({'status': status})
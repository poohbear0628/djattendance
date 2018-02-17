from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import DetailView, UpdateView, ListView, TemplateView, FormView

from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from .models import User, Trainee, TrainingAssistant
from .forms import UserForm, EmailForm, SwitchUserForm
from .serializers import BasicUserSerializer, UserSerializer, TraineeSerializer, TrainingAssistantSerializer

from braces.views import GroupRequiredMixin

from aputils.auth import login_user

from aputils.trainee_utils import trainee_from_user

class UserDetailView(DetailView):
  model = User
  context_object_name = 'user'
  template_name = 'accounts/user_detail.html'

class UserUpdateView(UpdateView):
  model = User
  form_class = UserForm
  template_name = 'accounts/update_user.html'

  def get_success_url(self):
    messages.success(self.request,
             "User Information Updated Successfully!")
    return reverse_lazy('user_detail', kwargs={'pk': self.kwargs['pk']})


class EmailUpdateView(UpdateView):
  model = User
  form_class = EmailForm
  template_name = 'accounts/email_change.html'

  def get_success_url(self):
    messages.success(self.request, "Email Updated Successfully!")
    return reverse_lazy('user-detail', kwargs={'pk': self.kwargs['pk']})


# class SwitchUserView(GroupRequiredMixin, TemplateView):
class SwitchUserView(SuccessMessageMixin, FormView):
  template_name = 'accounts/switch_user.html'
  context_object_name = 'context'
  form_class = SwitchUserForm
  success_url = reverse_lazy('home')
  success_message = "Successfully switched to %(user_id)s"

  def form_valid(self, form):
    user = form.cleaned_data['user_id']
    logout(self.request)
    login_user(self.request, user)
    return super(SwitchUserView, self).form_valid(form)

class AllTrainees(ListView):
  model = Trainee
  template_name = 'accounts/trainees_table.html'

  def get_context_data(self, **kwargs):
    context = super(AllTrainees, self).get_context_data(**kwargs)
    context['list_of_trainees'] = User.objects.filter(is_active=True).prefetch_related('locality', 'house')
    return context


""" API Views """
class UserViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer


class TraineeViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Trainee.objects.filter(is_active=True).prefetch_related('groups', 'terms_attended', 'locality')
  serializer_class = TraineeSerializer


class TrainingAssistantViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = TrainingAssistant.objects.filter(is_active=True)
  serializer_class = TrainingAssistantSerializer


class TraineesByGender(generics.ListAPIView):
  serializer_class = TraineeSerializer
  model = Trainee

  def get_queryset(self):
    gender = self.kwargs['gender']
    return Trainee.objects.filter(gender=gender).prefetch_related('groups', 'terms_attended', 'locality')


class TraineesByTerm(APIView):
  model = Trainee

  def get(self, request, format=None, **kwargs):
    term = int(kwargs['term'])
    trainees = [trainee for trainee in list(Trainee.objects.all().prefetch_related('groups', 'terms_attended', 'locality')) if trainee.current_term==term]
    serializer = TraineeSerializer(trainees, many=True)
    return Response(serializer.data)


class TraineesByTeam(generics.ListAPIView):
  serializer_class = TraineeSerializer
  model = Trainee

  def get_queryset(self):
    team = self.kwargs['pk']
    return Trainee.objects.filter(team__id=team).prefetch_related('groups', 'terms_attended', 'locality')


class TraineesByTeamType(generics.ListAPIView):
  serializer_class = TraineeSerializer
  model = Trainee

  def get_queryset(self):
    type = self.kwargs['type'].upper()
    return Trainee.objects.filter(team__type=type).prefetch_related('groups', 'terms_attended', 'locality')


class TraineesByHouse(generics.ListAPIView):
  serializer_class = TraineeSerializer
  model = Trainee

  def get_queryset(self):
    house = self.kwargs['pk']
    return Trainee.objects.filter(house__id=house).filter(is_active=True)


class TraineesByLocality(generics.ListAPIView):
  serializer_class = TraineeSerializer
  model = Trainee

  def get_queryset(self):
    locality = self.kwargs['pk']
    return Trainee.objects.filter(locality__id=locality).filter(is_active=True)


class TraineesHouseCoordinators(generics.ListAPIView):
  serializer_class = TraineeSerializer
  model = Trainee

  def get_queryset(self):
    trainees = Trainee.objects.filter(is_active=True)
    return filter(lambda x: x.HC_status(), trainees)

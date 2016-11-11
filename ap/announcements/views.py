from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin

from bootstrap3_datetime.widgets import DateTimePicker

from aputils.trainee_utils import trainee_from_user

from .models import Announcement
from .forms import AnnouncementForm

class AnnouncementRequest(SuccessMessageMixin, generic.edit.CreateView):
    template_name = 'announcement_request.html'
    form_class = AnnouncementForm
    success_url = '/'
    success_message = 'Announcement requested successfully'

class AnnouncementRequestList(generic.ListView):
    model = Announcement
    template_name = 'announcement_list.html'

    def get_queryset(self):
        trainee = trainee_from_user(self.request.user)
        if trainee:
            return Announcement.objects.filter(trainee=trainee).order_by('status')
        else:
            return Announcement.objects.filter().order_by('status')


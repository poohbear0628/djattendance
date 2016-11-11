from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from bootstrap3_datetime.widgets import DateTimePicker

from .models import Announcement
from .forms import AnnouncementForm

class AnnouncementRequest(SuccessMessageMixin, CreateView):
    template_name = 'announcement_request.html'
    form_class = AnnouncementForm
    success_url = '/'
    success_message = 'Announcement requested successfully'

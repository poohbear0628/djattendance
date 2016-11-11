from django.shortcuts import render
from django.views.generic.edit import CreateView

from bootstrap3_datetime.widgets import DateTimePicker

from .models import Announcement
from .forms import AnnouncementForm

class AnnouncementRequest(CreateView):
    template_name = 'announcement_request.html'
    form_class = AnnouncementForm

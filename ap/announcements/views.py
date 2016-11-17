from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin

from bootstrap3_datetime.widgets import DateTimePicker

from aputils.trainee_utils import trainee_from_user

from .models import Announcement
from .forms import AnnouncementForm, TraineeSelectForm

class AnnouncementRequest(SuccessMessageMixin, generic.edit.CreateView):
    model = Announcement
    template_name = 'announcement_request.html'
    form_class = AnnouncementForm

    def get_context_data(self, **kwargs):
        context = super(AnnouncementRequest, self).get_context_data(**kwargs)
        context['trainee_select_form'] = TraineeSelectForm()
        return context

    def form_valid(self, form):
        req = form.save(commit=False)
        req.trainee = trainee_from_user(self.request.user)
        req.save()
        return super(AnnouncementRequest, self).form_valid(form)

class AnnouncementRequestList(generic.ListView):
    model = Announcement
    template_name = 'announcement_list.html'

    def get_queryset(self):
        trainee = trainee_from_user(self.request.user)
        if trainee:
            return Announcement.objects.filter(trainee=trainee).order_by('status')
        else:
            return Announcement.objects.filter().order_by('status')

class AnnouncementDetail(generic.DetailView):
    model = Announcement
    template_name = 'announcement_detail.html'
    context_object_name = 'announcement'

class AnnouncementDelete(generic.DeleteView):
    model = Announcement

class AnnouncementUpdate(generic.UpdateView):
    model = Announcement
    template_name = 'announcement_update.html'
    form_class = AnnouncementForm

    def get_context_data(self, **kwargs):
        context = super(AnnouncementUpdate, self).get_context_data(**kwargs)
        context['trainee_select_form'] = TraineeSelectForm()
        return context


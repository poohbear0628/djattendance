from django.shortcuts import render
from django.views import generic

from bootstrap3_datetime.widgets import DateTimePicker

from aputils.trainee_utils import is_TA, trainee_from_user
from aputils.groups_required_decorator import group_required

from .models import Announcement
from .forms import AnnouncementForm, TraineeSelectForm

class AnnouncementRequest(generic.edit.CreateView):
    model = Announcement
    template_name = 'announcement_request.html'
    form_class = AnnouncementForm

    def get_form_kwargs(self):
        kwargs = super(AnnouncementRequest, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

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

    def get_context_data(self, **kwargs):
        context = super(AnnouncementRequestList, self).get_context_data(**kwargs)
        context['item_name'] = Announcement._meta.verbose_name
        context['create_url'] = Announcement.get_create_url()
        context['detail_template'] = 'announcement_list/description.html'
        if is_TA(self.request.user):
            context['item_title_template'] = 'announcement_list/ta_title.html'
        else:
            context['item_title_template'] = 'announcement_list/title.html'
        if is_TA(self.request.user):
            context['item_buttons'] = 'announcement_list/ta_buttons.html'
        else:
            context['item_buttons'] = 'announcement_list/buttons.html'
        return context

    def get_queryset(self):
        trainee = trainee_from_user(self.request.user)
        if is_TA(self.request.user):
            return Announcement.objects.filter().order_by('status')
        else:
            return Announcement.objects.filter(trainee=trainee).order_by('status')

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

    def get_form_kwargs(self):
        kwargs = super(AnnouncementUpdate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(AnnouncementUpdate, self).get_context_data(**kwargs)
        context['trainee_select_form'] = TraineeSelectForm()
        return context

@group_required(('administration',), raise_exception=True)
def modify_status(request, status, id):
    announcement = get_object_or_404(Announcement, pk=id)
    announcement.status = status
    announcement.save()
    announcement = get_object_or_404(Announcement, pk=id)
    name = announcement.trainee
    message = "%s's %s web request was " % (name, announcement.get_type_display())
    if status == 'A':
        message += 'approved.'
    if status == 'D':
        message += 'denied.'
    if status == 'F':
        message += 'marked for fellowship.'
    messages.add_message(request, messages.SUCCESS, message)

    return redirect('announcements:announcement-request-list')

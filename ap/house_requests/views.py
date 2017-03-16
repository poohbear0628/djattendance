from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse_lazy

from aputils.trainee_utils import is_TA, trainee_from_user
from .models import MaintenanceRequest, LinensRequest, FramingRequest

def NewRequestPage(request):
  return render(request, 'new_request_page.html')

class RequestCreate(generic.edit.CreateView):
  model = MaintenanceRequest
  template_name = 'create_request.html'
  success_url = reverse_lazy('house_requests:house_requests')
  def form_valid(self, form):
    req = form.save(commit=False)
    req.trainee_author = trainee_from_user(self.request.user)
    req.house = req.trainee_author.house
    req.save()
    return super(RequestCreate, self).form_valid(form)

class LinensRequestCreate(RequestCreate, generic.edit.CreateView):
  model = LinensRequest
  fields = ['item', 'quantity', 'reason']

class FramingRequestCreate(RequestCreate, generic.edit.CreateView):
  model = FramingRequest
  fields = ['location', 'frame']

class MaintenanceRequestCreate(RequestCreate, generic.edit.CreateView):
  model = MaintenanceRequest
  fields = ['description']

class MaintenanceRequestUpdate(MaintenanceRequestCreate, generic.edit.UpdateView):
  template_name = 'update_request.html'

class FramingRequestUpdate(FramingRequestCreate, generic.edit.UpdateView):
  template_name = 'update_request.html'

class LinensRequestUpdate(LinensRequestCreate, generic.edit.UpdateView):
  template_name = 'update_request.html'

class MaintenanceRequestDetail(generic.DetailView):
  model = MaintenanceRequest
  template_name = 'detail_request.html'

class FramingRequestDetail(generic.DetailView):
  model = FramingRequest
  template_name = 'detail_request.html'

class LinensRequestDetail(generic.DetailView):
  model = LinensRequest
  template_name = 'detail_request.html'

class RequestList(generic.ListView):
  template_name = "house_request_list.html"
  def get_context_data(self, **kwargs):
    context = super(RequestList, self).get_context_data(**kwargs)
    context.update({
      'item_name': self.model._meta.verbose_name,
      'create_url': self.model.get_create_url(),
       'is_TA': is_TA(self.request.user),
    })
    return context
  def get_queryset(self):
    user_has_service = self.request.user.groups.filter(name='facility_maintenance_or_frames_or_linens').exists()
    if is_TA(self.request.user) or user_has_service:
      return self.model.objects.filter().order_by('status')
    else:
      trainee = trainee_from_user(self.request.user)
      return self.model.objects.filter(trainee_author=trainee).order_by('status')

class MaintenanceRequestList(RequestList):
  model = MaintenanceRequest

class LinensRequestList(RequestList):
  model = LinensRequest

class FramingRequestList(RequestList):
  model = FramingRequest

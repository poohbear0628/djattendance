from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.core.urlresolvers import reverse_lazy

from aputils.trainee_utils import is_TA, trainee_from_user
from .models import MaintenanceRequest, LinensRequest, FramingRequest
from .forms import MaintenanceRequestForm

def NewRequestPage(request):
  return render(request, 'new_request_page.html')

def modify_status(request_type):
  def modify(request, status, id):
    request = get_object_or_404(request_type, pk=id)
    request.status = status
    request.save()
    return redirect('house_requests:house_requests')
  return modify

modify_maintenance_status = modify_status(MaintenanceRequest)
modify_linens_status = modify_status(LinensRequest)
modify_framing_status = modify_status(FramingRequest)

class MaintenanceRequestTAComment(generic.UpdateView):
  model = MaintenanceRequest
  fields = ['TA_comments']
  template_name = 'ta_comment.html'

class LinensRequestTAComment(generic.UpdateView):
  model = LinensRequest
  fields = ['TA_comments']
  template_name = 'ta_comment.html'

class FramingRequestTAComment(generic.UpdateView):
  model = FramingRequest
  fields = ['TA_comments']
  template_name = 'ta_comment.html'

class MaintenanceRequestDelete(generic.DeleteView):
  model = MaintenanceRequest
  success_url = reverse_lazy('house_requests:house_requests')

class LinensRequestDelete(generic.DeleteView):
  model = LinensRequest
  success_url = reverse_lazy('house_requests:house_requests')

class FramingRequestDelete(generic.DeleteView):
  model = FramingRequest
  success_url = reverse_lazy('house_requests:house_requests')

class RequestCreate(generic.edit.CreateView):
  model = MaintenanceRequest
  template_name = 'requests/request_form.html'
  success_url = reverse_lazy('house_requests:house_requests')
  def form_valid(self, form):
    req = form.save(commit=False)
    req.trainee_author = trainee_from_user(self.request.user)
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
  form_class = MaintenanceRequestForm

# the following view classes get everything they need from inheritance
class MaintenanceRequestUpdate(MaintenanceRequestCreate, generic.edit.UpdateView):
  pass

class FramingRequestUpdate(FramingRequestCreate, generic.edit.UpdateView):
  pass

class LinensRequestUpdate(LinensRequestCreate, generic.edit.UpdateView):
  pass

class MaintenanceRequestDetail(generic.DetailView):
  model = MaintenanceRequest
  template_name = 'requests/detail_request.html'

class FramingRequestDetail(generic.DetailView):
  model = FramingRequest
  template_name = 'requests/detail_request.html'

class LinensRequestDetail(generic.DetailView):
  model = LinensRequest
  template_name = 'requests/detail_request.html'

class RequestList(generic.ListView):
  template_name = 'requests/request_list.html'

  def get_queryset(self):
    user_has_service = self.request.user.groups.filter(name='facility_maintenance_or_frames_or_linens').exists()
    if is_TA(self.request.user) or user_has_service:
      return self.model.objects.filter().order_by('status')
    else:
      trainee = trainee_from_user(self.request.user)
      return self.model.objects.filter(trainee_author=trainee).order_by('status')

class MaintenanceRequestList(RequestList):
  model = MaintenanceRequest
  modify_status_url = 'house_requests:maintenance-modify-status'
  ta_comment_url = 'house_requests:maintenance-tacomment'

class LinensRequestList(RequestList):
  model = LinensRequest
  modify_status_url = 'house_requests:linens-modify-status'
  ta_comment_url = 'house_requests:linens-tacomment'

class FramingRequestList(RequestList):
  model = FramingRequest
  modify_status_url = 'house_requests:framing-modify-status'
  ta_comment_url = 'house_requests:framing-tacomment'

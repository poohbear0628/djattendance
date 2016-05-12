from django.views.generic import TemplateView, DetailView, ListView
from django.views import generic


from .models import Template, Chart


class TemplateCreate(TemplateView):
    template_name = "seating/template_create.html"


class TemplateDetail(DetailView):
    queryset = Template.objects.all()
    template_name = "seating/template_detail.html"



# viewing the leave slips
class SeatView(generic.ListView):
    # model = Chart
    template_name = 'seating/seat_view.html'

    # def get_queryset(self):
    #      individual=IndividualSlip.objects.filter(trainee=self.request.user.trainee.id).order_by('status')
    #      group=GroupSlip.objects.filter(trainee=self.request.user.trainee.id).order_by('status') #if trainee is in a group leaveslip submitted by another user
    #      queryset= chain(individual,group) #combines two querysets
    #      return queryset


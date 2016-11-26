from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from meal_seating.models import Table, TraineeExclusion
from accounts.models import Trainee
from datetime import date, timedelta
from meal_seating.forms import TableFormSet, TraineeExclusionFormSet, TraineeExclusionForm
from django.views.generic import TemplateView, DetailView, ListView
from django.views import generic
from terms.models import Term
from accounts.models import Trainee
from .serializers import TableSerializer, TraineeExclusionSerializer
from accounts.serializers import TraineeSerializer, BasicUserSerializer

from rest_framework import viewsets, filters
from rest_framework.renderers import JSONRenderer
from rest_framework_bulk import BulkModelViewSet


@csrf_protect
def editinfo(request):
  test = request.POST.getlist('to')
  print test
  isChecked = [int(x) for x in request.POST.getlist('to[]')]
  print set(isChecked)
  exclude_list = TraineeExclusion.objects.values_list('trainee', flat=True)
  difference = set(exclude_list) - set(isChecked)
  addition = set(isChecked) - set(exclude_list)
  TraineeExclusion.objects.all().filter(trainee__in=list(difference)).delete()
  trainee_exclusions = [TraineeExclusion(trainee=val) for val in addition]
  TraineeExclusion.objects.bulk_create(trainee_exclusions)
  
  return HttpResponse(difference)

def seattables(request):
    filterchoice = request.POST['Filter']
    genderchoice = request.POST['Gender']
    startdate = request.POST['startdate']
    enddate = request.POST['enddate']

    exclude_list = TraineeExclusion.objects.values_list('trainee', flat=True)
    trainees = Trainee.objects.all().filter(is_active=1, gender=genderchoice).order_by(filterchoice).exclude(id__in=exclude_list)
    seating_list = Table.seatinglist(trainees,genderchoice)

    return render(request, 'meal_seating/detail.html', {'seating_list' : seating_list, 'startdate':startdate, 'enddate': enddate})

def newseats(request):
      form = TraineeExclusionForm()
      exclude_list = TraineeExclusion.objects.values_list('trainee', flat=True)
      trainees_exclude = Trainee.objects.all().filter(pk__in=exclude_list)
      trainees = Trainee.objects.all().filter(is_active=1).exclude(type="S").order_by("lastname")    
      return render(request, 'meal_seating/newseating.html', {'trainees' : trainees,'trainees_exclude':trainees_exclude,})

def signin(request):
    trainees = Trainee.objects.all().filter(is_active=1).order_by("lastname")
    startdate = date.today()
    two_week_datelist = []
    for x in range(0,14):
        mydate = startdate + timedelta(days=x)
        two_week_datelist.append(format(mydate))
    return render(request, 'meal_seating/mealsignin.html', {'trainees' : trainees, 'start_date' : startdate, "two_week_datelist" : two_week_datelist})

class TableListView(generic.ListView):
    model = Table
    template_name = 'meal_seating/table_edit.html'

    context_object_name = 'context'

    def get_context_data(self, **kwargs):
        listJSONRenderer = JSONRenderer()
        l_render = listJSONRenderer.render
        table = Table.objects.all()
        context = super(TableListView, self).get_context_data(**kwargs)
        context['table_bb'] = l_render(TableSerializer(table, many=True).data)

        return context

class TableViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tables to be viewed or edited.
    """
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class TraineeExclusionListView(generic.ListView):
    model = Table
    template_name = 'meal_seating/trainee_edit.html'

    context_object_name = 'context'

    def get_context_data(self, **kwargs):
        listJSONRenderer = JSONRenderer()
        l_render = listJSONRenderer.render
        trainee_exclusions = TraineeExclusion.objects.all()
        trainees = Trainee.objects.filter(is_active=True)
        context = super(TraineeExclusionListView, self).get_context_data(**kwargs)
        context['trainee_exclusions_bb'] = l_render(TraineeExclusionSerializer(trainee_exclusions, many=True).data)
        context['trainees'] = trainees
        context['trainees_bb'] = l_render(BasicUserSerializer(trainees, many=True).data)
        return context

class TraineeExclusionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows trainee exclusions to be viewed or edited.
    """
    queryset = TraineeExclusion.objects.all()
    serializer_class = TraineeExclusionSerializer
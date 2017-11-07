from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponseRedirect
from aputils.decorators import group_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.serializers import serialize

from accounts.models import Trainee
from .models import House, HCSurvey, HCRecommendation
from .forms import HCSurveyForm, HCRecommendationForm

@group_required(['HC'])
def create_hc_survey(request):
  hc = Trainee.objects.get(id=request.user.id)
  house = House.objects.get(id=request.user.house.id)
  residents = Trainee.objects.filter(house=request.user.house).exclude(id=request.user.id)

  if request.method == 'POST':
    data = request.POST
    
    # get forms with POST data
    hc_survey_form = HCSurveyForm(request.POST, instance=HCSurvey(), auto_id=True)
    if hc_survey_form.is_valid():
      hc_survey = hc_survey_form.save(commit=False)
      for trainee_comment in hc_survey.trainee_comments:
        trainee_comment['name'] = residents.get(id=trainee_comment['trainee_id']).full_name
      print hc_survey.trainee_comments
      hc_survey.hc = hc
      hc_survey.house = house
      hc_survey.save()
    
    print 'test 2'  # TODO: Still getting 302 response
    return HttpResponseRedirect('/hc/hc_survey')

  else:
    form = HCSurveyForm(instance=HCSurvey(), auto_id=True)

    ctx = {
      'form': form,
      'trainees': serialize('json', residents),
#      'hc_gen_comment_form': hc_gen_comment_form,
 #     'trainee_form_tuples': trainee_form_tuples,
      'button_label': "Submit",
      'page_title': "HC Survey",
      'house': House.objects.get(id=request.user.house.id),
      'hc': Trainee.objects.get(id=request.user.id)
    }
    return render(request, 'hc/hc_survey.html', context=ctx)



class HCRecommendationCreate(CreateView):
  model = HCRecommendation
  template_name = 'hc/hc_recommendation.html'
  form_class = HCRecommendationForm
  # TODO: Returning 302

  def get_form_kwargs(self):
    kwargs = super(HCRecommendationCreate, self).get_form_kwargs()
    kwargs['user'] = self.request.user
    return kwargs

  def form_valid(self, form):
    hc_recommendation = form.save(commit=False)
    hc_recommendation.hc = self.request.user
    hc_recommendation.house = self.request.user.house
    hc_recommendation.average = hc_recommendation.get_average()
    hc_recommendation.save()
    return super(HCRecommendationCreate, self).form_valid(form)

  def get_context_data(self, **kwargs):
    ctx = super(HCRecommendationCreate, self).get_context_data(**kwargs)
    ctx['button_label'] = 'Submit'
    ctx['page_title'] = 'HC Recommendation'
    ctx['hc'] = Trainee.objects.get(id=self.request.user.id)
    ctx['house'] = House.objects.get(id=self.request.user.house.id)
    return ctx

class HCRecommendationUpdate(HCRecommendationCreate, UpdateView):
  model = HCRecommendation
  template_name = 'hc/hc_recommendation.html'
  form_class = HCRecommendationForm
  success_url = reverse_lazy('home')

  def get_context_data(self, **kwargs):
    ctx = super(HCRecommendationUpdate, self).get_context_data(**kwargs)
    ctx['button_label'] = 'Update'
    ctx['page_title'] = 'Update HC Recommendation'
    return ctx
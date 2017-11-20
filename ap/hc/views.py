from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponseRedirect
from aputils.decorators import group_required
from django.core.urlresolvers import reverse_lazy
from braces.views import GroupRequiredMixin

from accounts.models import Trainee
from .models import House, HCSurvey, HCRecommendation, HCTraineeComment
from .forms import HCSurveyForm, HCRecommendationForm, HCTraineeCommentForm


@group_required(['HC'])
def create_hc_survey(request):
  hc = request.user
  house = House.objects.get(id=hc.house.id)

  residents = Trainee.objects.filter(house=house).exclude(id=hc.id)

  # filters out the co-hc
  for r in residents:
    if r.has_group(['HC']):
      residents.exclude(id=r.id)

  if request.method == 'POST':
    data = request.POST

    # build forms from data
    hc_survey_form = HCSurveyForm(data, instance=HCSurvey(), auto_id=True)
    comment_forms = [
      HCTraineeCommentForm(data, prefix=trainee.id, instance=HCTraineeComment(), auto_id=True)
      for trainee in residents
    ]

    # validate forms & save objects
    if hc_survey_form.is_valid() and all(cf.is_valid() for cf in comment_forms):
      hc_survey = hc_survey_form.save(commit=False)
      hc_survey.hc = hc
      hc_survey.house = house
      hc_survey.save()

      for cf in comment_forms:
        comment = cf.save(commit=False)
        comment.hc_survey = hc_survey
        comment.trainee = residents.get(id=cf.prefix)
        comment.save()

    return HttpResponseRedirect('/hc/hc_survey')

  else:  # GET

    # build forms
    form = HCSurveyForm(instance=HCSurvey(), auto_id=True)
    comment_forms = []
    for trainee in residents:
      comment_forms.append(
        (trainee, HCTraineeCommentForm(prefix=trainee.id, instance=HCTraineeComment()))
      )

    ctx = {
      'form': form,
      'comment_forms': comment_forms,
      'button_label': "Submit",
      'page_title': "HC Survey",
      'house': house,
      'hc': hc
    }
    return render(request, 'hc/hc_survey.html', context=ctx)


class HCRecommendationCreate(GroupRequiredMixin, CreateView):
  model = HCRecommendation
  template_name = 'hc/hc_recommendation.html'
  form_class = HCRecommendationForm
  group_required = ['HC']
  success_url = reverse_lazy('home')
  # TODO: Returning 302

  def get_form_kwargs(self):
    kwargs = super(HCRecommendationCreate, self).get_form_kwargs()
    kwargs['user'] = self.request.user
    return kwargs

  def form_valid(self, form):
    hc_recommendation = form.save(commit=False)
    hc_recommendation.hc = self.request.user
    hc_recommendation.house = self.request.user.house
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

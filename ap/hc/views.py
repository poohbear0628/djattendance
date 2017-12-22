from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect
from aputils.decorators import group_required
from django.core.urlresolvers import reverse_lazy
from braces.views import GroupRequiredMixin

from accounts.models import Trainee
from .models import House, HCSurvey, HCRecommendation, HCTraineeComment
from .forms import HCSurveyForm, HCRecommendationForm, HCTraineeCommentForm
from terms.models import Term
from datetime import date


@group_required(['HC'])
def create_hc_survey(request):
  hc = request.user
  house = House.objects.get(id=hc.house.id)
  period = Term.period_from_date(Term.current_term(), date.today())
  residents = Trainee.objects.filter(house=house).exclude(groups__name='HC')

  if request.method == 'POST':
    data = request.POST

    # build forms from data
    # get_or_create allows you to create/update data
    # HCSurvey -- one per house per period
    temp1, created = HCSurvey.objects.get_or_create(house=house, period=period)

    hc_survey_form = HCSurveyForm(data, instance=temp1, auto_id=True)
    comment_forms = []

    for trainee in residents:
      # Comment -- one per trainee per period
      temp2, created = HCTraineeComment.objects.get_or_create(hc_survey=temp1, trainee=trainee)
      comment_forms.append(
        HCTraineeCommentForm(data, prefix=trainee.id, instance=temp2, auto_id=True)
      )

    # validate forms & save objects
    if hc_survey_form.is_valid() and all(cf.is_valid() for cf in comment_forms):
      hc_survey = hc_survey_form.save(commit=False)
      hc_survey.hc = hc
      hc_survey.house = house
      hc_survey.period = period
      hc_survey.save()

      for cf in comment_forms:
        comment = cf.save(commit=False)
        comment.hc_survey = hc_survey
        comment.trainee = residents.get(id=cf.prefix)
        comment.save()

    return HttpResponseRedirect(reverse_lazy('hc:hc-survey'))

  else:  # GET

    # build forms
    temp1 = HCSurvey.objects.get_or_create(house=house, period=period)[0]
    form = HCSurveyForm(instance=temp1, auto_id=True)
    comment_forms = []
    for trainee in residents:
      temp2 = HCTraineeComment.objects.get_or_create(hc_survey=temp1, trainee=trainee)[0]
      comment_forms.append(
        (trainee, HCTraineeCommentForm(prefix=trainee.id, instance=temp2))
      )

    ctx = {
      'form': form,
      'comment_forms': comment_forms,
      'button_label': "Submit",
      'page_title': "HC Survey",
      'period': period,
      'house': house,
      'hc': hc
    }
    return render(request, 'hc/hc_survey.html', context=ctx)


class HCRecommendationCreate(GroupRequiredMixin, UpdateView):
  model = HCRecommendation
  template_name = 'hc/hc_recommendation.html'
  form_class = HCRecommendationForm
  group_required = ['HC']
  success_url = reverse_lazy('home')

  def get_object(self, queryset=None):
    # get the existing object or created a new one
    print self.request.user.house
    obj, created = HCRecommendation.objects.get_or_create(house=self.request.user.house)
    return obj

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

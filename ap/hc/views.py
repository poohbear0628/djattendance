from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect

from accounts.models import Trainee
from .models import House, HCSurvey, HCGeneralComment, HCTraineeComment, HCRecommendation
from .forms import HCSurveyForm, HCGeneralCommentForm, HCTraineeCommentForm, HCRecommendationForm


def create_hc_survey(request):
  residents = Trainee.objects.filter(house=request.user.house).exclude(id=request.user.id)

  if request.method == 'POST':

    # get forms with POST data
    hc_survey_form = HCSurveyForm(request.POST, instance=HCSurvey())

    hc_gen_comment_form = HCGeneralCommentForm(request.POST, instance=HCGeneralComment())

    hc_tr_comm_forms = [
        HCTraineeCommentForm(request.POST, prefix=str(index), instance=HCTraineeComment())
        for index in range(0, len(residents))
    ]

    # check if all forms are valid
    if (hc_survey_form.is_valid() and hc_gen_comment_form.is_valid() and
        all([frm.is_valid() for frm in hc_tr_comm_forms])):

      # autofill HC Survey with hc
      hc_survey = hc_survey_form.save(commit=False)
      hc_survey_form.hc = request.user
      hc_survey.save()

      # assign HCSurvey to HCGeneralComment
      hc_gen_comment = hc_gen_comment_form.save(commit=False)
      hc_gen_comment.hc_survey = hc_survey

      # assign HCSurvey to HCTraineeComments
      for htcf in hc_tr_comm_forms:
        hc_trainee_comment = htcf.save(commit=False)
        hc_trainee_comment.hc_survey = hc_survey
        hc_trainee_comment.save()

      return HttpResponseRedirect('/hc/hc_survey/')

  else:
    hc_survey_form = HCSurveyForm(instance=HCSurvey())
    hc_survey_form.fields['house'].queryset = House.objects.filter(id=request.user.house.id)

    hc_gen_comment_form = HCGeneralCommentForm(instance=HCGeneralComment())

    trainee_form_tuples = []
    for index, trainee in enumerate(residents):
      hc_tr_comm_form = HCTraineeCommentForm(prefix=str(index), instance=HCTraineeComment())
      trainee_form_tuples.append(
        (trainee, hc_tr_comm_form)
      )

    ctx = {
      'hc_survey_form': hc_survey_form,
      'hc_gen_comment_form': hc_gen_comment_form,
      'trainee_form_tuples': trainee_form_tuples,
      'button_label': "Submit",
      'page_title': "HC Survey"
    }
    return render(request, 'hc/hc_survey.html', context=ctx)


class HCRecommendationCreate(CreateView):
  model = HCRecommendation
  template_name = 'hc/hc_recommendation.html'
  form_class = HCRecommendationForm

  def get_form_kwargs(self):
    kwargs = super(HCRecommendationCreate, self).get_form_kwargs()
    kwargs['user'] = self.request.user
    return kwargs

  def get_context_data(self, **kwargs):
    ctx = super(HCRecommendationCreate, self).get_context_data(**kwargs)
    ctx['button_label'] = 'Submit'
    ctx['page_title'] = 'HC Recommendation'
    return ctx

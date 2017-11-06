from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from aputils.decorators import group_required

from accounts.models import Trainee
from .models import House, HCSurvey, HCGeneralComment, HCTraineeComment, HCRecommendation
from .forms import HCSurveyForm, HCGeneralCommentForm, HCTraineeCommentForm, HCRecommendationForm


@group_required(['HC'])
def create_hc_survey(request):
  hc = Trainee.objects.get(id=request.user.id)
  house = House.objects.get(id=request.user.house.id)
  residents = Trainee.objects.filter(house=request.user.house).exclude(id=request.user.id)

  if request.method == 'POST':
    data = request.POST
    # get forms with POST data
    hc_gen_comment_form = HCGeneralCommentForm(request.POST, instance=HCGeneralComment(), auto_id='gencomment_%s')

    trainee_form_tuples = []
    for index, trainee in enumerate(residents):
      hc_tr_comm_form = HCTraineeCommentForm(data, prefix=str(index), instance=HCTraineeComment(), auto_id='trainee_%s')
      trainee_form_tuples.append(
        (trainee, hc_tr_comm_form)
      )

    # check if all forms are valid
    if (hc_gen_comment_form.is_valid() and
        all([frm.is_valid() for tr, frm in trainee_form_tuples])):

      print 'test 1'
      # autofill HC Survey with hc
      hc_survey, created = HCSurvey.objects.get_or_create(hc=hc, house=house)
      if created:
        hc_survey.hc = hc
        hc_survey.house = house
        hc_survey.save()

      # assign HCSurvey to HCGeneralComment
      hc_gen_comment = hc_gen_comment_form.save(commit=False)
      hc_gen_comment.hc_survey = hc_survey
      hc_gen_comment.save()

      # assign HCSurvey to HCTraineeComments
      for trainee, frm in trainee_form_tuples:
        hc_trainee_comment = frm.save(commit=False)        
        hc_trainee_comment.hc_survey = hc_survey
        hc_trainee_comment.trainee = trainee
        hc_trainee_comment.save()

    print 'test 2'  # TODO: Still getting 302 response
    return HttpResponseRedirect('/')

  else:
    hc_survey_form = HCSurveyForm(instance=HCSurvey(), auto_id=True)
    hc_survey_form.fields['house'].queryset = House.objects.filter(id=request.user.house.id)

    hc_gen_comment_form = HCGeneralCommentForm(instance=HCGeneralComment(), auto_id='gencomment_%s')

    trainee_form_tuples = []
    for index, trainee in enumerate(residents):
      hc_tr_comm_form = HCTraineeCommentForm(prefix=str(index), instance=HCTraineeComment(), auto_id='trainee_%s')
      trainee_form_tuples.append(
        (trainee, hc_tr_comm_form)
      )

    ctx = {
      'hc_survey_form': hc_survey_form,
      'hc_gen_comment_form': hc_gen_comment_form,
      'trainee_form_tuples': trainee_form_tuples,
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

  def get_form_kwargs(self):
    kwargs = super(HCRecommendationCreate, self).get_form_kwargs()
    kwargs['user'] = self.request.user
    return kwargs

  def get_context_data(self, **kwargs):
    ctx = super(HCRecommendationCreate, self).get_context_data(**kwargs)
    ctx['button_label'] = 'Submit'
    ctx['page_title'] = 'HC Recommendation'
    ctx['hc'] = Trainee.objects.get(id=self.request.user.id)
    ctx['house'] = House.objects.get(id=self.request.user.house.id)
    return ctx

from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q

from accounts.models import Trainee
from .models import House, HCSurvey, HCGeneralComment, HCTraineeComment, HCRecommendation
from .forms import HCSurveyForm, HCGeneralCommentForm, HCTraineeCommentForm, HCRecommendationForm

def create_hc_survey(request):
  if request.method == 'POST':
    pass
  else:
    hc_survey_form = HCSurveyForm(instance=HCSurvey())
    hc_survey_form.fields['house'].queryset = House.objects.filter(id=request.user.house.id)

    hc_gen_comment_form = HCGeneralCommentForm(instance=HCGeneralComment())

    residents = Trainee.objects.filter(house=request.user.house).exclude(id=request.user.id)
    hc_trainee_comment_forms = \
      [HCTraineeCommentForm(prefix=str(x), instance=HCTraineeComment) for x in range(0,len(residents))]
    
    ctx = {'hc_survey_form': hc_survey_form,
      'hc_gen_comment_form': hc_gen_comment_form,
      'hc_trainee_comment_forms': hc_trainee_comment_forms,
      'button_label': "Submit",
      }
    return render(request, 'houses/hc_survey.html', context=ctx)

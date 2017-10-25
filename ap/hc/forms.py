from django import forms

from .models import HCSurvey, HCRecommendation, HCGeneralComment, HCTraineeComment

class HCSurveyForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(HCSurveyForm, self).__init__(*args, **kwargs)

  class Meta:
    model = HCSurvey
    fields = ['house', ]


class HCGeneralCommentForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(HCGeneralCommentForm, self).__init__(*args, **kwargs)

  class Meta:
    model = HCGeneralComment
    exclude = ['hc_survey', ]


class HCTraineeCommentForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(HCTraineeCommentForm, self).__init__(*args, **kwargs)

  class Meta:
    model = HCTraineeComment
    fields = ['comment', ]


class HCRecommendationForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(HCRecommendationForm, self).__init__(*args, **kwargs)

    # fields

    class Meta:
      model = HCRecommendation
      exclude = ['house', ]

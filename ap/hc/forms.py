from django import forms
from accounts.models import Trainee
from houses.models import House
from .models import HCSurvey, HCRecommendation


class HCSurveyForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(HCSurveyForm, self).__init__(*args, **kwargs)

  class Meta:
    model = HCSurvey
    exclude = ['hc', 'house', ]
    widgets = {
      'atmosphere': forms.Textarea(attrs={'rows': 4}),
      'situations': forms.Textarea(attrs={'rows': 4}),
      'comment': forms.Textarea(attrs={'rows': 4}),
    }


# class HCTraineeCommentForm(forms.ModelForm):
#   def __init__(self, *args, **kwargs):
#     super(HCTraineeCommentForm, self).__init__(*args, **kwargs)

#   class Meta:
#     model = HCTraineeComment
#     exclude = ['hc_survey', 'trainee', ]
#     widgets = {
#       'assessment': forms.Textarea(attrs={'rows': 4}),
#     }

# ts = t.objects.filter(house__name='2105 Grace Ct.')
# form = hcsf(instance=hcs(), residents=ts)
class HCRecommendationForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    user = kwargs.pop('user')
    super(HCRecommendationForm, self).__init__(*args, **kwargs)
    house = House.objects.filter(id=user.house.id)
    self.fields['choice'].queryset = Trainee.objects.filter(house=house).exclude(id=user.id)

  class Meta:
    model = HCRecommendation
    exclude = ['hc', 'house', 'average', ]
    widgets = {
      'recommendation': forms.Textarea(attrs={'rows': 3}),
    }

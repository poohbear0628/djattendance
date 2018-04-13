from terms.models import Term
from hc.models import HCSurvey, HCRecommendation, HCSurveyAdmin, HCRecommendationAdmin


def hc_surveys():
  ret = False
  term = Term.current_term()
  admins = HCSurveyAdmin.objects.filter(open_survey=True).filter(term=term)
  if admins.count() > 0:
    ret = True
  return ret


def hc_recommendations():
  ret = False
  term = Term.current_term()
  admins = HCRecommendationAdmin.objects.filter(open_survey=True).filter(term=term)
  if admins.count() > 0:
    ret = True
  return ret

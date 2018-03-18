from accounts.models import TrainingAssistant


def is_trainee(user):
  t = user.type
  return t in ('R', 'C', 'S')


def is_TA(user):
  t = user.type
  return t == 'T'


def ta_from_user(user):
  try:
    return TrainingAssistant.objects.get(id=user.id)
  except TrainingAssistant.DoesNotExist:
    return None

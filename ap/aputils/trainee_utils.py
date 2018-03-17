from accounts.models import Trainee, TrainingAssistant


def is_trainee(user):
  t = user.type
  return t in ('R', 'C', 'S')


def is_TA(user):
  t = user.type
  return t == 'T'


def trainee_from_user(user):
  try:
    return Trainee.objects.get(id=user.id)
  except Trainee.DoesNotExist:
    from raven.contrib.django.raven_compat.models import client
    client.captureException()


def ta_from_user(user):
  try:
    return TrainingAssistant.objects.get(id=user.id)
  except TrainingAssistant.DoesNotExist:
    return None

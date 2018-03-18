from accounts.models import Trainee


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
    return None

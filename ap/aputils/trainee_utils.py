from accounts.models import Trainee, TrainingAssistant
from django.contrib.auth.models import Group

groups = Group.objects.all()
GROUP_CHOICES = (('a', 'all'),)
GROUP_DICT = {'a':'all'}
alpha = 'abcdefghijklmnopqrstuvwxyz'
for i in range(1,len(groups)):
  GROUP_CHOICES += ((alpha[i], groups[i].name.encode('ascii','ignore')),)
  GROUP_DICT[alpha[i]] = groups[i].name.encode('ascii','ignore')

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

def ta_from_user(user):
  try:
    return TrainingAssistant.objects.get(id=user.id)
  except TrainingAssistant.DoesNotExist:
    return None

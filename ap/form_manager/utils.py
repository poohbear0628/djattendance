from aputils.trainee_utils import is_trainee
from accounts.models import Trainee
import json  # fobi user json for form_elements not Django models
import ast

TRAINEE_CHOICES = ((-1, 'all'), )
trainee_qs = Trainee.objects.all()
for t in trainee_qs:
  TRAINEE_CHOICES += ((t.id, t.full_name), )


def get_form_access(form_entry):
  form_elements = form_entry.formelemententry_set.all()
  for el in form_elements:
    data = json.loads(el.plugin_data)
    if data['name'] == 'Access':
      x = ast.literal_eval(data['initial'])  # unicode list to list of strings
      list_of_ids = map(int, x)  # list of ints
      return list_of_ids  # list of trainee.id
  return [-1]  # if form_access doesn't exists, retunr -1 (all)


def user_can_see_form(user, form_entry):
  trainee_ids = get_form_access(form_entry)
  if is_trainee(user) and -1 in trainee_ids:
    return True
  return user.id in trainee_ids

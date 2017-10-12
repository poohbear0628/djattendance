from aputils.trainee_utils import is_trainee
from accounts.models import Trainee
import json  # fobi user json for form_elements not Django models


TRAINEE_CHOICES = ((-1, 'all'), )
trainee_qs = Trainee.objects.all()
for t in trainee_qs:
  TRAINEE_CHOICES += ((t.id, t.full_name), )

def get_form_access(form_entry):
  form_elements = form_entry.formelemententry_set.all()
  for el in form_elements:
    data = json.loads(el.plugin_data)
    if data['name'] == 'Access':
      return int(data['initial']) # trainee.id, only one trainee for now
  return -1 # if form_access doesn't exists, retunr -1 (all)

def user_can_see_form(user, form_entry):
  trainee_id = get_form_access(form_entry)
  if is_trainee(user) and trainee_id == -1:
    return True
  return user.id == trainee_id

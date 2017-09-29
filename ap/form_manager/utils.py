from aputils.trainee_utils import is_trainee
from aputils.groups import GROUP_LIST
import json # fobi user json for form_elements not Django models

GROUP_CHOICES =  (('all', 'all'),)
groups = GROUP_LIST
for i in range(1,len(groups)):
  GROUP_CHOICES += ((groups[i], groups[i]),)

def get_form_group(form_entry):
  form_elements = form_entry.formelemententry_set.all()
  for el in form_elements:
    data = json.loads(el.plugin_data)
    if data['name'] == 'Groups':
      return data['initial'] # a-w, only one group for now
  return 'all' # Form Access doesn't exist, return all

def user_can_see_form(user, form_entry):
  group = get_form_group(form_entry)
  if is_trainee(user) and group == 'all':
    return True
  return user.has_group([group])

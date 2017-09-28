from aputils.trainee_utils import is_trainee
from django.contrib.auth.models import Group
import json #fobi user json for form_elements not Django models

groups = Group.objects.all()
GROUP_CHOICES = (('a', 'all'),)
GROUP_DICT = {'a':'all'}
alpha = 'abcdefghijklmnopqrstuvwxyz'
for i in range(1,len(groups)):
  GROUP_CHOICES += ((alpha[i], groups[i].name.encode('ascii','ignore')),)
  GROUP_DICT[alpha[i]] = groups[i].name.encode('ascii','ignore')

def get_form_permission(form_entry):
  form_elements = form_entry.formelemententry_set.all()
  for el in form_elements:
    data = json.loads(el.plugin_data)
    if data['name'] == 'Groups':
      return data['initial'] #a-w
  return 'a' #Form Access doesn't exist, return all

def user_can_see_form(user, form_entry):
  group_key = get_form_permission(form_entry)
  if is_trainee(user) and group_key == 'a':
    return True
  group = GROUP_DICT[group_key]
  return user.has_group([group])

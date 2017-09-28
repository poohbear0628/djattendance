from aputils.trainee_utils import is_trainee
from django.contrib.auth.models import Group
import json # fobi user json for form_elements not Django models

class FormGroups():
  
  def __init__(self):
    self.choices = (('a', 'all'),)
    self.choices_dict = {'a':'all'}
    self._generateValues()

  def _generateValues(self):
    groups = Group.objects.all()
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(1,len(groups)):
      self.choices += ((alpha[i], groups[i].name.encode('ascii','ignore')),)
      self.choices_dict[alpha[i]] = groups[i].name.encode('ascii','ignore')

def get_form_group(form_entry):
  form_elements = form_entry.formelemententry_set.all()
  for el in form_elements:
    data = json.loads(el.plugin_data)
    if data['name'] == 'Groups':
      return data['initial'] # a-w, only one group for now
  return 'a' # Form Access doesn't exist, return all

def user_can_see_form(user, form_entry):
  form_groups = FormGroups()
  group_key = get_form_group(form_entry)
  if is_trainee(user) and group_key == 'a':
    return True
  group = form_groups.choices_dict[group_key]
  return user.has_group([group])

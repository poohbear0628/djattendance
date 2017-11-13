import json  # fobi user json for form_elements not Django models


def get_form_access(form_entry):
  form_elements = form_entry.formelemententry_set.all()
  for el in form_elements:
    data = json.loads(el.plugin_data)
    if data['name'] == 'Access':
      return data['initial']


def user_can_see_form(user, form_entry):
  trainee_ids = get_form_access(form_entry)
  return str(user.id) in str(trainee_ids)

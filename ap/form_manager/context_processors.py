#This file is not used, but it can be by adding 
#TEMPLATES[0]['OPTIONS']['context_processors'].append("form_manager.context_processors.forms_available")
#to settings.base
from fobi.models import FormEntry
from .utils import user_can_see_form
from aputils.trainee_utils import is_trainee

def forms_available(request):
  user = request.user 
  if not hasattr(user, 'type') or not is_trainee(user):
    return {'forms_available': 0}

  public_forms = FormEntry.objects.filter(is_public=True)
  form_count = 0
  for pf in public_forms:
    if user_can_see_form(user, pf):
      form_count += 1
  return {'forms_available': form_count}

from aputils.trainee_utils import is_trainee, trainee_from_user

def class_popup(request):
  context_attr = 'is_in_class'
  user = request.user
  if not hasattr(user, 'type') or not is_trainee(user):
    return {context_attr: False}
  trainee = trainee_from_user(user)
  events = trainee.immediate_upcoming_event(time_delta=0)
  if not events:
    return {context_attr: False}
  event = events[0]
  if event.type == 'C':
    return {context_attr: True}
  else:
    return {context_attr: False}

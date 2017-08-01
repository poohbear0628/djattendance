from aputils.trainee_utils import is_trainee, trainee_from_user


def class_popup(request):
  context_attr = 'is_in_class'
  in_class = False
  user = request.user
  if hasattr(user, 'type') and is_trainee(user):
    trainee = trainee_from_user(user)
    events = trainee.immediate_upcoming_event(time_delta=0)
    if events:
      event = events[0]
      if event.type == 'C':
        in_class = True
  return {context_attr: in_class, 'user': user}

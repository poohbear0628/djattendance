from aputils.trainee_utils import is_trainee, trainee_from_user

def class_popup(request):
  data = {}
  if is_trainee(request.user):
    trainee = trainee_from_user(request.user)
    events = trainee.immediate_upcoming_event(time_delta=0)
    if not events:
      data['is_in_class'] = False
      return data
    event = events[0]
    if event.type == 'C':
      data['is_in_class'] = True
    else:
      data['is_in_class'] = False
  return data

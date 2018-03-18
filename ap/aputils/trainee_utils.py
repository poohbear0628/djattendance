def is_trainee(user):
  t = user.type
  return t in ('R', 'C', 'S')


def is_TA(user):
  t = user.type
  return t == 'T'

from accounts.models import Trainee

def is_trainee(user):
    try:
        t = user.type
    except:
        return False
    if t == 'R' or t == 'C' or t == 'S':
        return True
    return False

def is_TA(user):
    try:
        t = user.type
    except:
        return False
    if t == 'T':
        return True
    return False

def trainee_from_user(user):
    try:
        return Trainee.objects.get(id=user.id)
    except Trainee.DoesNotExist:
        return None

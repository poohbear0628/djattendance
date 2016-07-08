from accounts.models import Trainee
from django.template.defaulttags import register

def is_trainee(user):
    t = user.type
    if t == 'R' or t == 'C' or t == 'S':
        return True
    return False

def is_TA(user):
    t = user.type
    if t == 'T':
        return True
    return False

def trainee_from_user(user):
    try:
        return Trainee.objects.get(id=user.id)
    except Trainee.DoesNotExist:
        return None


COMMA_REGEX = r'^{0},|,{0},|,{0}$|^{0}$'

def comma_separated_field_is_in_regex(list):
    regs = []
    for item in list:
        regs.append(COMMA_REGEX.format(item))
    reg_str = '|'.join(regs)

    return reg_str

# Method to get value from dictionary in template
# Use: dictionary|get_item:key
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def lookup(list, key):
    for l in list:
        if l == key:
            return l
    return None

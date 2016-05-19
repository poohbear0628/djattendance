from django import template

register = template.Library()

@register.filter(name='is_trainee')
def is_trainee(user):
    t = user.type
    if t == 'R' or t == 'C' or t == 'S':
        return True
    return False
from django.template.defaulttags import register

# !! IMPORTANT: Keep this file free from any model imports to avoid cyclical dependencies!!

COMMA_REGEX = r'^{0},|,{0},|,{0}$|^{0}$'

def comma_separated_field_is_in_regex(list):
    regs = []
    for item in list:
        regs.append(COMMA_REGEX.format(item))
    reg_str = '|'.join(regs)

    return reg_str


def sorted_user_list_str(users):
    return ', '.join([u.full_name for u in users.order_by('firstname', 'lastname')])

# Method to get value from dictionary in template
# Use: dictionary|get_item:key
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

# Search for item in a list
@register.filter
def lookup(list, key):
    for l in list:
        if l == key:
            return l
    return None

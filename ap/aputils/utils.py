import cStringIO as StringIO

from django.template.defaulttags import register
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse

import xhtml2pdf.pisa as pisa
from cgi import escape
import re

# !! IMPORTANT: Keep this file free from any model imports to avoid cyclical dependencies!!

def render_to_pdf(template_src, context_dict):
	template = get_template(template_src)
	html = template.render(context=context_dict)
	result = StringIO.StringIO()

	pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return HttpResponse('We had some errors<pre>%s</pre>' %escape(html))

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

@register.filter
def get_index(lst, index):
    return lst[index]

@register.filter
def split_string_list(string):
    return string.split(';')

@register.filter
def split_string(string, delimiterIndex):
    delimiter = delimiterIndex.split(',')[0]
    index = int(delimiterIndex.split(',')[1])
    return string.split(delimiter)[index]

@register.filter
def print_str(obj):
    print obj

@register.filter
def str_contains(string, regex):
    return regex in string

@register.filter
def get_fill_in_the_blank_string(string):
    blanks = re.findall(r'\$[0-9]+', string)
    rtn_str = string
    for each in blanks:

        rtn_str = rtn_str.replace(each, '_____(' + each[1] + ')_____')
    return rtn_str

#'\$[0-9]+'
@register.filter
def count_occurences_of_blanks(string):
    return re.findall('\$[0-9]+', string)

#response|get_blank_for_question:forloop.parentloop.counter0,forloop.counter0
#response|get_item:forloop.parentloop.counter0|split_string:';,forloop.counter0'
#response|get_blank_for_question:forloop.parentloop.counter0,forloop.counter0
@register.filter
def get_blank_for_question(question, blank_index):
    return question.split(';')[blank_index]

# Search for item in a list
@register.filter
def lookup(list, key):
    for l in list:
        if l == key:
            return l
    return None


WEEKDAY_CODE = {
    0: 'M',
    1: 'T',
    2: 'W',
    3: 'Th',
    4: 'F',
    5: 'S',
    6: 'LD',
}

@register.filter
def weekday_code(day):
    return WEEKDAY_CODE[day]

WEEKDAYS = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: "Lord's Day",
}

@register.filter
def weekday_name(day):
    return WEEKDAYS[day]



@register.filter
def worker_list(workers):
    return ', '.join([w.full_name for w in workers])


@register.filter
def input_worker_list(workers):
    return ','.join([w.full_name for w in workers])

@register.filter
def input_workerID_list(workers):
    return ','.join([str(w.id) for w in workers])

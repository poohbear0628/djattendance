import cStringIO as StringIO
import xhtml2pdf.pisa as pisa
import time
import functools
from cgi import escape

from django.template.defaulttags import register
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

from .groups_required_decorator import group_required
# !! IMPORTANT: Keep this file free from any model imports to avoid cyclical dependencies!!

def modify_model_status(model, url):
  @group_required(('administration',), raise_exception=True)
  def modify_status(request, status, id):
    obj = get_object_or_404(model, pk=id)
    obj.status = status
    obj.save()

    status_messages = {
      'A': 'approved',
      'D': 'denied',
      'F': 'marked for fellowship',
      'S': 'approved',
    }

    message = "%s's %s was %s" % (obj.get_trainee_requester().full_name, obj._meta.verbose_name, status_messages[status])
    messages.add_message(request, messages.SUCCESS, message)
    return redirect(url)
  return modify_status

def memoize(obj):
  cache = obj.cache = {}

  @functools.wraps(obj)
  def memoizer(*args, **kwargs):
      key = str(args) + str(kwargs)
      if key not in cache:
          cache[key] = obj(*args, **kwargs)
      return cache[key]
  return memoizer

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

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def sorted_user_list_str(users):
  return ', '.join([u.full_name for u in users.order_by('firstname', 'lastname')])

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

# Timer decorator
def timeit(method):
  def timed(*args, **kw):
    ts = time.time()
    result = method(*args, **kw)
    te = time.time()

    print '%r %2.2f sec' % (method.__name__, te-ts)
    return result

  return timed

class timeit_inline(object):
  def __init__(self, title=""):
    self.title = title

  def start(self):
    print self.title
    self.ts = time.time()

  def end(self):
    self.te = time.time()
    print '%s %2.2f sec' % (self.title, self.te-self.ts)

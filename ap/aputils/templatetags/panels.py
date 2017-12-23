from collections import namedtuple
from django import template
from django.core.urlresolvers import reverse

#code structure copied from aputils/templatetags/smart_menu.py

def Panel(name, num, url):
  return namedtuple('Panel', 'name num url')(name=name, num=num, url=url)

register = template.Library()

def my_reverse(url_pattern):
  if url_pattern != '#':
    return reverse(url_pattern)
  else:
    return '#'

# Generates all the panels
@register.assignment_tag(takes_context=True)
def generate_panels(context):
  user = context['user']
  if user.is_anonymous():
    return ""

  lifestudies_panel = Panel(
      name='Life Studies',
      num='1', 
      url='lifestudies'
  )
  classnotes_panel = Panel(
      name='Class Notes',
      num='3', 
      url='attendance'
  )
  unexcusedtardies_panel = Panel(
      name='Unexcused Tardies',
      num='2', 
      url='attendance'
  )
  unexcusedabsences_panel = Panel(
      name='Unexcused Absences',
      num='0', 
      url='attendance'
  )
  leaveslips_panel = Panel(
      name='Leave Slips Pending',
      num='2', 
      url='attendance'
  )

  panels = [lifestudies_panel, classnotes_panel, unexcusedtardies_panel, unexcusedabsences_panel, leaveslips_panel]

  return panels

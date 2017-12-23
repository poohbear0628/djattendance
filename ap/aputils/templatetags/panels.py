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
      num='1's, 
      url=reverse('lifestudies:discipline_list'),
  )
  classnotes_panel = Panel(
      name='Class Notes',
      num='3', 
      url=reverse('classnotes:classnotes_list')
  )
  unexcusedtardies_panel = Panel(
      name='Unexcused Tardies',
      num='2', 
      url=reverse('attendance:attendance-submit')
  )
  unexcusedabsences_panel = Panel(
      name='Unexcused Absences',
      num='0', 
      url=reverse('attendance:attendance-submit')
  )
  leaveslips_panel = Panel(
      name='Leave Slips Pending',
      num='2', 
      url=reverse('attendance:attendance-submit')
  )

  panels = [lifestudies_panel, classnotes_panel, unexcusedtardies_panel, unexcusedabsences_panel, leaveslips_panel]

  return panels

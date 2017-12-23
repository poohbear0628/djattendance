from datetime import *
from collections import namedtuple
from django import template
from django.core.urlresolvers import reverse
from lifestudies.models import Discipline
from classnotes.models import Classnotes
from django.db.models import Q
from attendance.models import Roll
from attendance.utils import Period
from terms.models import Term
from leaveslips.models import *

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

  ls = Discipline.objects.filter(trainee=user).values('quantity')
  num_ls = 0
  for l in ls:
    num_ls = num_ls + l['quantity']

  lifestudies_panel = Panel(
      name='Life Studies',
      num=num_ls,
      url=reverse('lifestudies:discipline_list'),
  )

  classnotes_panel = Panel(
      name='Class Notes',
      num=Classnotes.objects.filter(Q(trainee=user) & ~Q(status='A')).count(),
      url=reverse('classnotes:classnotes_list')
  )

  # calculates unexcued absences and tardies for this period
  # absence and tardy is checked first compared to date as this is expected to be less computionally expensive
  # given that we're not checked every attendence record assuming that the trainee won't have much absence or tardies
  # oh Lord...
  # try and except to accomodate for superuser
  p = Period(Term.current_term()).period_of_date(date.today())
  uet = uea = 0
  try:
    att_rcd = Trainee.objects.filter(email=user.email).first().get_attendance_record()
    for att in att_rcd:
      if att['attendance'] == 'A':
        if (datetime.strptime(att['start'][0:10], "%Y-%m-%d").date() > Period(Term.current_term()).start(p)) & (datetime.strptime(att['end'][0:10], "%Y-%m-%d").date() < Period(Term.current_term()).end(p)):
          uea +=1
      elif att['attendance'] == 'T':
        if (datetime.strptime(att['start'][0:10], "%Y-%m-%d").date() > Period(Term.current_term()).start(p)) & (datetime.strptime(att['end'][0:10], "%Y-%m-%d").date() < Period(Term.current_term()).end(p)):
          uet +=1
  except AttributeError:
    pass

  unexcusedtardies_panel = Panel(
      name='Unexcused Tardies',
      num=uet,
      url=reverse('attendance:attendance-submit')
  )
  unexcusedabsences_panel = Panel(
      name='Unexcused Absences',
      num=uea,
      url=reverse('attendance:attendance-submit')
  )

  #leaveslip calculation and period calculation are off by one
  ls_pending = 0
  ls_p = IndividualSlip.objects.filter(trainee=user, status='P')
  for ls in ls_p:
    if (p-1) in ls.periods:
      ls_pending += 1

  leaveslips_panel = Panel(
      name='Leave Slips Pending',
      num=ls_pending,
      url=reverse('attendance:attendance-submit')
  )

  panels = [lifestudies_panel, classnotes_panel, unexcusedtardies_panel, unexcusedabsences_panel, leaveslips_panel]

  return panels
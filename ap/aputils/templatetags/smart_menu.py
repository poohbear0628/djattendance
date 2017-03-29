from collections import namedtuple

from django import template
from aputils.trainee_utils import is_trainee, is_TA
from django.core.urlresolvers import reverse

#Type Declarations
def SubMenuItem(name, permission=None, url='#', condition=True):
  return namedtuple('SubMenuItem', 'name permission url condition')(name = name, permission = permission, url = url, condition = condition)

def MenuItem(name, ta_only=[], trainee_only=[], common=[], specific=[]):
  return namedtuple('MenuItem', 'name ta_only trainee_only common specific')(name = name, ta_only = ta_only, trainee_only = trainee_only, common = common, specific = specific)

register = template.Library()

#Helper Functions
def my_reverse(url_pattern):
  if url_pattern != '#':
    return reverse(url_pattern)
  else:
    return '#'

def smart_add(url, name):
  path = my_reverse(url)
  return [(path, name)]


#Generates the menu
@register.assignment_tag(takes_context=True)
def generate_menu(context):
  user = context['user']

  if user.is_anonymous():
    return ""
  menu = ""

  #The sidebar menu items, with their permissions and conditions required, should be input here
  attendance_menu = MenuItem(name='Attendance',
    ta_only = [
      SubMenuItem(name='Create Event', url='schedules:event-create')
    ],
    trainee_only = [],
    common = [
      SubMenuItem(name='Personal Attendance', url='attendance:attendance-submit', condition=True),
      SubMenuItem(name='Submit Individual Leaveslips', url='leaveslips:individual-create'),
      SubMenuItem(name='Submit Group Leaveslips', url='leaveslips:group-create'),
      SubMenuItem(name='|', permission='attendance.add_roll', url='#'),
      SubMenuItem(name='Class & Study Roll', permission='attendance.add_roll', url='attendance:class-rolls'),
      SubMenuItem(name='Meal Roll', permission='attendance.add_roll', url='attendance:class-rolls'),
      SubMenuItem(name='House Roll', permission='attendance.add_roll', url='attendance:class-rolls'),
      SubMenuItem(name='YPC Roll', permission='attendance.add_roll', url='attendance:class-rolls'),
      SubMenuItem(name='Designated Service Roll', permission='attendance.add_roll', url='attendance:class-rolls')],
    specific = [])

  discipline_menu = MenuItem(name ='Discipline',
    common =[
      SubMenuItem(name='Life Studies', url='lifestudies:discipline_list'),
      SubMenuItem(name='Class Notes', url='#')
    ])

  exam_menu = MenuItem(name = 'Exams',
    specific = [
      SubMenuItem(name="Create Exam", permission='exams.add_exam', url='exams:new')
    ])

  requests_menu = MenuItem(name= 'Requests',
    common = [
      SubMenuItem(name='A/V Requests', url='#'),
      SubMenuItem(name='Maintenance Requests', url='house_requests:house-requests'),
      SubMenuItem(name='Room Reservations', url='#'),
      SubMenuItem(name='Web Access Requests', url='web_access:web_access-list')
    ])

  misc_menu = MenuItem(name="Misc.",
    common = [
      SubMenuItem(name='View Announcements', url='announcements:announcement-list'),
      SubMenuItem(name='Create Announcements', url='announcements:announcement-request')
    ],
    trainee_only = [
      SubMenuItem(name='Bible Reading Tracker', url='bible_tracker:index')
    ],
    specific = [
      SubMenuItem(name='Badges', permission='badges.add_badge', url='badges:badges_list'),
      SubMenuItem(name="Absent Trainee Roster", permission='attendance.add_roll', url='absent_trainee_roster:absent_trainee_form'),
      SubMenuItem(name='Meal Seating', permission='meal_seating.add_table', url='meal_seating.views.newseats'),
      SubMenuItem(name='Seating Chart', permission='seating.add_chart', url='seating:chart_list')
    ])

  #For every 'current' item that needs to appear in the side-bar, ie exams to be taken, iterim intentions form, exit interview, etc, the context variable needs to be added to the context, and the menu item can be added here as follows
  current_menu = MenuItem(name = 'Current',
    trainee_only=[
      SubMenuItem(name="Take Exam", url='exams:list', condition = context['exams_available'])
    ])

  user_menu = [attendance_menu, discipline_menu, requests_menu, exam_menu, misc_menu, current_menu]

  for menu_item in user_menu:
    items = []
    if menu_item.common:
      for sub_item in menu_item.common:
        if sub_item.condition:
          items += smart_add(sub_item.url, sub_item.name)
    if menu_item.ta_only:
      if is_TA(user):
        for sub_item in menu_item.ta_only:
          if sub_item.condition:
            items += smart_add(sub_item.url, sub_item.name)
    if menu_item.trainee_only:
      if is_trainee(user):
        for sub_item in menu_item.trainee_only:
          if sub_item.condition:
            items += smart_add(sub_item.url, sub_item.name)
    if menu_item.specific:
      for specific_perm_item in menu_item.specific:
        if specific_perm_item.permission in context['perms']:
          if specific_perm_item.condition:
            items += smart_add(specific_perm_item.url, specific_perm_item.name)
    if items:
      menu += "<li class=\"dropdown\"><a href=\"#\" class=\"dropdown-toggle\" data-toggle=\"dropdown\" role=\"button\" aria-haspopup=\"true\" aria-expanded=\"false\">" + menu_item.name + "<span class=\"caret\"></span></a><ul class=\"dropdown-menu\">"
      for (path, name) in items:
        if name == '|':
          menu += "<li role=\"separator\" class=\"divider\"></li>"
        else:
          menu += "<li><a href=\"" + path + "\">" + name + "</a></li>"
      menu += "</ul>"
  return menu
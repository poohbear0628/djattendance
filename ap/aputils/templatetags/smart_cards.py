from collections import namedtuple
from django import template
from django.core.urlresolvers import reverse

#code structure copied from aputils/templatetags/smart_menu.py

def CardLink(title, url='#', number=None):
  return namedtuple('CardLink', 'title url number')(title=title, url=url, number=number)

def Card(header_title, permission, card_links=[]):
  return namedtuple('Card', 'header_title permission card_links')(header_title=header_title, permission=permission, card_links=card_links)

# Helper Functions
def my_reverse(url_pattern):
  if url_pattern != '#':
    return reverse(url_pattern)
  else:
    return '#'

register = template.Library()

# Generates all the cards
@register.assignment_tag(takes_context=True)
def generate_cards(context):
  user = context['user']
  if user.is_anonymous():
    return ""
  menu = ""

  badge_card = Card(
      header_title='Badges',
      permission='badges', #is there a way to refer specifically to the group, like is it an enum? 
      card_links=[
          CardLink(title="Badge Portal", url='badges:badges_list')
      ]
  )

  cards = [badge_card]

  return cards
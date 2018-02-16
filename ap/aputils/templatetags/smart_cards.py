from collections import namedtuple
from django import template
from django.core.urlresolvers import reverse
from aputils.trainee_utils import is_trainee, is_TA

from web_access.models import WebRequest
from announcements.models import Announcement
from accounts.models import *
from audio.models import AudioRequest
from house_requests.models import *
from room_reservations.models import RoomReservation
from leaveslips.models import IndividualSlip, GroupSlip
from lifestudies.models import Summary
from classnotes.models import Classnotes

def CardLink(title, url='#', number=None):
  return namedtuple('CardLink', 'title url number')(title=title, url=url, number=number)

def Card(header_title, condition=True, card_links=[]):
  return namedtuple('Card', 'header_title condition card_links')(header_title=header_title, condition=condition, card_links=card_links)

register = template.Library()

# Generates all the cards
@register.assignment_tag(takes_context=True)
def generate_cards(context):
  user = context['user']
  if user.is_anonymous():
    return ""


  cards = []

  if user.has_group(['training_assistant']):
    
    #filter for trainees assigned to current TA and cross it with existing web requests
    my_trainees = Trainee.objects.filter(TA=user)

    web_access_count = WebRequest.objects.filter(status='P', trainee__in=my_trainees).count()
    av_count = AudioRequest.objects.filter(status='P', trainee_author__in=my_trainees).count()    
    house_count = MaintenanceRequest.objects.filter(status='P', trainee_author__in=my_trainees).count()+FramingRequest.objects.filter(status='P', trainee_author__in=my_trainees).count()+LinensRequest.objects.filter(status='P', trainee_author__in=my_trainees).count()
    
    my_trainees = User.objects.filter(TA=user)
    room_reservation_count = RoomReservation.objects.filter(status='P', requester__in=my_trainees).count()

    announce_count = Announcement.objects.filter(status='P').count()

    TA_requests = Card(
        header_title="Requests",
        card_links=[
          CardLink(title="Web Access", url=reverse('web_access:web_access-list'), number=web_access_count),
          CardLink(title="AV", url=reverse('audio:ta-audio-home'), number=av_count),
          CardLink(title="Housing", url=reverse('house_requests:house-requests'),number=house_count),
          CardLink(title="Room Reservation", url=reverse('room_reservations:ta-room-reservation-list'),number=room_reservation_count),
          CardLink(title="Announcements", url=reverse('announcements:announcement-request-list'), number=announce_count)
        ]);

    cards.append(TA_requests)

    ls_p = IndividualSlip.objects.filter(status='P', TA=user).count() + GroupSlip.objects.filter(status='P', trainees__in=my_trainees).count()
    ls_f = IndividualSlip.objects.filter(status='F', TA=user).count() + GroupSlip.objects.filter(status='F', trainees__in=my_trainees).count()


    TA_leaveslips = Card(
        header_title="Leaveslips",
        card_links=[
          CardLink(title="Pending", url=reverse('leaveslips:ta-leaveslip-list'), number=ls_p),
          CardLink(title="Marked for fellowship", url=reverse('leaveslips:ta-leaveslip-list'), number=ls_f),        
        ]);

    cards.append(TA_leaveslips)

    all_summ = Summary.objects.filter(approved=False)
    summ_count = 0
    for s in all_summ:
      if s.discipline.trainee in my_trainees:        
        summ_count = summ_count+1;


    cn = Classnotes.objects.filter(status='P', trainee__in=my_trainees).count()

    TA_disciplines = Card(
        header_title="Discipline",
        card_links=[
          CardLink(title="Life Study Summaries", url=reverse('lifestudies:discipline_list'), number=summ_count),
          CardLink(title="Classnotes", url=reverse('classnotes:classnotes_list'), number=cn),
        ]);

    cards.append(TA_disciplines)

    TA_admin = Card(
      header_title="Administration",
      card_links=[
        CardLink(title="Exams", url=reverse('exams:manage')),
        CardLink(title="HC Forms", url=reverse('hc:hc-admin')),
        CardLink(title="Graduation", url=reverse('graduation:grad-admin')),
      ]);

    cards.append(TA_admin)

    TA_reports = Card(
      header_title="Reports",
      card_links=[
        CardLink(title="Life-Study", url=reverse('lifestudies:discipline_report')),
        CardLink(title="Class Notes", url=reverse('classnotes:classnotes_report')),
        CardLink(title="Bible Reading", url=reverse('bible_tracker:report')),
        CardLink(title="Service", url=reverse('services:services_schedule')),
      ])

    cards.append(TA_reports)

  sample_card_2 = Card(
    header_title="Sample Card",
    condition=True,
    card_links=[
        CardLink(title="just a sample"),
        CardLink(title="look in smart_cards.py")
    ]
  )

  badge_card = Card(
      header_title='Badges',
      condition=user.has_group(['badges']),
      card_links=[
          CardLink(title="Badge Portal", url=reverse('badges:badges_list'))
      ]
  )

  ta_card_requests = Card(
      header_title='Requests',
      condition=is_TA(user),
      card_links=[

      ]
  )

  ta_card_leaveslips = Card(
      header_title='Leave Slips',
      condition=is_TA(user),
      card_links=[

      ]
  )

  ta_card_general = Card(
      header_title='General',
      condition=is_TA(user),
      card_links=[
        CardLink(title="just a sample"),
      ]
  )


  ta_card_other = Card(
      header_title='Other',
      condition=is_TA(user),
      card_links=[

      ]
  )

  return cards
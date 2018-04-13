from django.core.management.base import BaseCommand
from attendance.models import Roll
from schedules.models import Event
from terms.models import Term
from datetime import datetime
from leaveslips.models import IndividualSlip

import sys
from contextlib import contextmanager


@contextmanager
def stdout_redirected(new_stdout):
  save_stdout = sys.stdout
  sys.stdout = new_stdout
  try:
    yield None
  finally:
    sys.stdout = save_stdout


def open_file(filename):
  def a_wrapper(func):
    def another_wrapper(self):
      with open(filename, "w") as f:
        with stdout_redirected(f):
          func(self)
    return another_wrapper
  return a_wrapper


RIGHT_NOW = datetime.now().strftime("%m%d%Y_%H%M%S")


class Command(BaseCommand):
  # to use: python ap/manage.py data_check_rolls --settings=ap.settings.dev
  def add_arguments(self, parser):
    parser.add_argument(  # --mr 1
        '--mr',
        dest='mislink_rolls',
        help='Pull rolls with a mislink in schedules',
    )
    parser.add_argument(  # --gr 1
        '--gr',
        dest='ghost_rolls',
        help='Pull present rolls with no leave slips attached',
    )
    parser.add_argument(  # --ml 1
        '--ml',
        dest='mislink_slips',
        help='Pull all slips with mislink in rolls',
    )

  file_name = '../mislink_rolls' + RIGHT_NOW + '.txt'

  # @open_file(file_name)
  def _mislink_rolls(self):
    # Pulls all rolls that has a mislink, the event that the rolls points to does not exist in the trainee's active schedule
    print RIGHT_NOW
    rolls = Roll.objects.all().order_by('event__id', 'date')
    ct = Term.current_term()
    output = '{0}: {1}-- Submitted by: {2}\n'
    output2 = 'For Roll {0}: Possible Event: {1} [ID: {2}]\n'

    # stats
    bad_rolls = []
    errors = 0
    no_sched = 0
    wrong_elective = 0
    crc = 0
    yp_lb = 0
    yp_irv = 0

    def find_possible_events(roll):
      # pulls possible events that the roll should be attached to by looking at the atached event's start and end time or name or event type
      start = roll.event.start
      end = roll.event.end
      today = datetime.now().date()
      mid = datetime.combine(today, start) + (datetime.combine(today, end) - datetime.combine(today, start)) / 2

      evs = []
      s_priority = 0
      for s in roll.trainee.schedules.all().exclude(name='Generic Group Events'):
        if s.active_in_week(ct.term_week_of_date(roll.date)):
          for ev in s.events.filter(weekday=roll.event.weekday):
            if datetime.combine(today, ev.start) < mid and datetime.combine(today, ev.end) > mid and s.priority > s_priority:
              s_priority = s.priority
              evs.append(ev)

        s_priority = 0
      return evs

    for r in rolls:
      try:
        schedules = r.event.schedules.all()
        roll_week = ct.term_week_of_date(r.date)
        good = False
        # if roll is not associated with a schedule
        if schedules.count() == 0:
          no_sched += 1
          print 'NO SCHED, so '
          pass
        # if so, check each schedule
        else:
          for s in schedules:
            # is roll's trainee in that schedule ?
            if r.trainee.id not in s.trainees.values_list('id', flat=True):
              continue
            # if so, is the roll in an active schedule ?
            elif s.active_in_week(roll_week) and (str(roll_week) not in s.weeks):
              print 'Wrong Week: '
              print output.format(str(r.id), r, r.submitted_by)
            # if so, it's a good roll
            else:
              good = True
        if not good:
          bad_rolls.append(r)
          print 'Trainee DNM: '
          print output.format(str(r.id), r, r.submitted_by)
          if r.event.name in ["Greek I", "Greek II", "Character", "German I", "German II", "Greek/ Character", "Character Study"]:
            wrong_elective += 1
          elif r.trainee.team.code == "CRC":
            crc += 1
          elif r.trainee.team.code == "YP-LB":
            yp_lb += 1
          elif r.trainee.team.code == "YP-IRV":
            yp_irv += 1
          for ev in find_possible_events(r):
            print output2.format(r.id, ev, ev.id)
            print '\n'
      except Exception as e:
        errors += 1
        print output.format(str(r.id), e, r.submitted_by)
    print 'bad rolls: ' + str(len(bad_rolls)) + '\n'
    print 'Due to no schedules for the roll: ' + str(no_sched) + '\n'
    print 'Elective related (Gk, Char, Ger): ' + str(wrong_elective) + '\n'
    print 'Cerritos College Related: ' + str(crc) + '\n'
    print 'YP-LB Related: ' + str(yp_lb) + '\n'
    print 'YP-IRV Related: ' + str(yp_irv) + '\n'
    print 'errors: ' + str(errors) + '\n'

  file_name = '../ghost_rolls' + RIGHT_NOW + '.txt'

  # @open_file(file_name)
  def _ghost_rolls(self):
    print RIGHT_NOW
    # Pull all rolls that have a present status with no leave slips attached
    rolls = Roll.objects.filter(status='P').order_by('date')
    output = '{0}: {1}-- Submitted by: {2}\n'
    output2 = 'For Roll {0}: Possible Slip: {1} [ID: {2}]\n'
    ghost_rolls = []

    def find_possible_slips(roll):
      # check to see if there's a leaveslip submitted by the trainee for other rolls or events on the date that this roll takes place
      return roll.trainee.individualslips.filter(rolls__date__in=[roll.date])

    for r in rolls:
      try:
        slips = r.leaveslips.all()
        if slips.count() == 0:
          ghost_rolls.append(r)
          print output.format(r.id, r, r.submitted_by)
          for s in find_possible_slips(r):
            print output2.format(r.id, s, s.id)
            print '\n'
      except Exception as e:
        print output.format(r.id, e, r.submitted_by)
    print 'ghost rolls: ' + str(len(ghost_rolls)) + '\n'

  file_name = '../mislink_leaveslips' + RIGHT_NOW + '.txt'

  # @open_file(file_name)
  def _mislink_leaveslips(self):
    print RIGHT_NOW
    # Pull all leaveslips submitted by trainee X and has rolls not for trainee X
    output = '[{0} - {1}]: [{2} - {3}]\n'
    output2 = 'For Slip {0}: Possible Roll: {1} [ID: {2}] By: {3}\n'
    bad_slips = []

    def find_possible_rolls(roll, slip):
      # finds possible rolls for trainee X that matches the attached roll
      return Roll.objects.filter(event=roll.event, date=roll.date, trainee=slip.trainee)

    for slip in IndividualSlip.objects.all():
      try:
        for roll in slip.rolls.all():
          if slip.trainee.id != roll.trainee.id:
            bad_slips.append(slip)
            print output.format(slip.id, slip, roll.id, roll)
            for pr in find_possible_rolls(roll, slip):
              print output2.format(slip.id, pr, pr.id, pr.submitted_by)
              print '\n'
      except Exception as e:
        print output.format(slip, '!', e, '!')
    print 'bad slips: ' + str(len(bad_slips)) + '\n'

  def handle(self, *args, **options):
    allcmd = False
    if all(options[x] is None for x in ['mislink_rolls', 'ghost_rolls', 'mislink_slips']):
      allcmd = True
    if allcmd or options['mislink_rolls']:
      print('* Pulling Rolls with mislinked Trainee...')
      self._mislink_rolls()
    if allcmd or options['ghost_rolls']:
      print('* Pulling "present" Rolls with no leavslips attached...')
      self._ghost_rolls()
    if allcmd or options['mislink_slips']:
      print('* Pulling leaveslips with rolls that do not belong to submitting trainee')
      self._mislink_leaveslips()

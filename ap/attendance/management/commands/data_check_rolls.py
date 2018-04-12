from django.core.management.base import BaseCommand
from attendance.models import Roll
from schedules.models import Event
from terms.models import Term
from datetime import datetime
from leaveslips.models import IndividualSlip


def out(s, f):
  print s
  f.write(s)


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

  def _mislink_rolls(self):
    # Pulls all rolls that has a mislink, the event that the rolls points to does not exist in the trainee's active schedule
    right_now = datetime.now().strftime("%m%d%Y_%H%M%S")
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
      evs = Event.objects.none()
      for s in roll.trainee.schedules.all():
        evs |= s.events.filter(weekday=roll.event.weekday)
      return evs.filter(name=roll.event.name) | evs.filter(type=roll.event.type) | evs.filter(start=roll.event.start)

    with open('../mislink_rolls' + right_now + '.txt', 'w') as f:
      for r in rolls:
        try:
          schedules = r.event.schedules.all()
          roll_week = ct.term_week_of_date(r.date)
          good = False
          # if roll is not associated with a schedule
          if schedules.count() == 0:
            no_sched += 1
            out('NO SCHED, so ', f)
            pass
          # if so, check each schedule
          else:
            for s in schedules:
              # is roll's trainee in that schedule ?
              if r.trainee.id not in s.trainees.values_list('id', flat=True):
                continue
              # if so, is the roll in an active schedule ?
              elif s.active_in_week(roll_week) and (str(roll_week) not in s.weeks):
                out('Wrong Week: ', f)
                out(output.format(str(r.id), r, r.submitted_by), f)
              # if so, it's a good roll
              else:
                good = True
          if not good:
            bad_rolls.append(r)
            out('Trainee DNM: ', f)  # Trainee Did Not Match
            out(output.format(str(r.id), r, r.submitted_by), f)
            if r.event.name in ["Greek I", "Greek II", "Character", "German I", "German II", "Greek/ Character", "Character Study"]:
              wrong_elective += 1
            elif r.trainee.team.code == "CRC":
              crc += 1
            elif r.trainee.team.code == "YP-LB":
              yp_lb += 1
            elif r.trainee.team.code == "YP-IRV":
              yp_irv += 1
            for ev in find_possible_events(r).distinct():
              out(output2.format(r.id, ev, ev.id), f)
            out('\n', f)
        except Exception as e:
          errors += 1
          out(output.format(str(r.id), e, r.submitted_by), f)
      out('bad rolls: ' + str(len(bad_rolls)) + '\n', f)
      out('Due to no schedules for the roll: ' + str(no_sched) + '\n', f)
      out('Elective related (Gk, Char, Ger): ' + str(wrong_elective) + '\n', f)
      out('Cerritos College Related: ' + str(crc) + '\n', f)
      out('YP-LB Related: ' + str(yp_lb) + '\n', f)
      out('YP-IRV Related: ' + str(yp_irv) + '\n', f)
      out('errors: ' + str(errors) + '\n', f)

  def _ghost_rolls(self):
    # Pull all rolls that have a present status with no leave slips attached
    right_now = datetime.now().strftime("%m%d%Y_%H%M%S")
    rolls = Roll.objects.filter(status='P').order_by('date')
    output = '{0}: {1}-- Submitted by: {2} \n'
    output2 = 'For Roll {0}: Possible Slip: {1} [ID: {2}]\n'

    def find_possible_slips(roll):
      # check to see if there's a leaveslip submitted by the trainee for other rolls or events on the date that this roll takes place
      return roll.trainee.individualslips.filter(rolls__date__in=[roll.date])

    with open('../ghost_rolls' + right_now + '.txt', 'w') as f:
      for r in rolls:
        try:
          slips = r.leaveslips.all()
          if slips.count() == 0:
            out(output.format(r.id, r, r.submitted_by), f)
            for s in find_possible_slips(r):
              out(output2.format(r.id, s, s.id), f)
        except Exception as e:
          out(output.format(r.id, e, r.submitted_by), f)

  def _mislink_leaveslips(self):
    # Pull all leaveslips submitted by trainee X and has rolls not for trainee X
    right_now = datetime.now().strftime("%m%d%Y_%H%M%S")
    output = '[{0} - {1}]: [{2} - {3}]\n'
    output2 = 'For Slip {0}: Possible Roll: {1} [ID: {2}] By: {3}\n'

    def find_possible_rolls(roll, slip):
      # finds possible rolls for trainee X that matches the attached roll
      return Roll.objects.filter(event=roll.event, date=roll.date, trainee=slip.trainee)

    with open('../mislink_leaveslips' + right_now + '.txt', 'w') as f:
      for slip in IndividualSlip.objects.all():
        try:
          for roll in slip.rolls.all():
            if slip.trainee.id != roll.trainee.id:
              out(output.format(slip.id, slip, roll.id, roll), f)
              for pr in find_possible_rolls(roll, slip):
                out(output2.format(slip.id, pr, pr.id, pr.submitted_by), f)
        except Exception as e:
          out(output.format(slip, '!', e, '!'), f)

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

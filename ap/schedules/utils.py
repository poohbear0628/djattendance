from datetime import timedelta
from schedules.models import Event, Schedule
from terms.models import Term
from attendance.models import Roll

def afternoon_class_transfer(trainee, e_code, start_week):
  # assume that existing schedules for each of the afternoon class for the full term already exists

  # assure class is an afternoon class with following parameters
  # class type afternoon, on Tuesday or Thursday, attendace monitor takes roll
  # if the ev_code is not an afternoon class, return right away
  aftn_evs = Event.objects.filter(class_type='AFTN', weekday__in=[1, 3], monitor='AM')
  if e_code not in aftn_evs.values_list('code', flat=True):
    return "not an afternoon class"

  date = Term.objects.get(current=True).get_date(start_week, 0)

  # get set of unique events according to conditions, these are the afternoon class the trainee is currently on
  # also obtains old schedule trainee is on for priority and code
  # obtain involved rolls that needs to be modified here
  # make sure the django query is executed for both old_evs and rolls otherwise they mutute because of laziness or re-eval
  old_evs = set(ev for ev in trainee.events if ev.class_type=='AFTN' and ev.monitor=='AM')
  old_sch = Schedule.objects.filter(events__in=old_evs, trainees=trainee)
  old_priority = max(list(old_sch.values_list('priority', flat=True)))
  old_rolls_ids = list(Roll.objects.filter(trainee=trainee, event__in=old_evs, date__gte=date).values_list('id', flat=True))

  # get the new event and the new schedule that the trainee will be transferred onto
  new_ev = aftn_evs.filter(code=e_code)
  new_sch = Schedule.objects.none()

  # check if an existing schedule for those weeks onward exists
  # set the new schedule if already found, also find the whole term schedule for that class
  whole_term_sch = Schedule.objects.none()
  potential_sch = Schedule.objects.filter(events__in=new_ev)
  for sch in potential_sch:
    weeks = [int(i) for i in sch.weeks.split(',')]
    if min(weeks) == start_week:
      new_sch = sch
    if min(weeks) == 0:
      whole_term_sch = sch

  new_evs = whole_term_sch.events.all()

  # if existing schedule not found, duplicate from the whole term schedule
  # add events, change name, priority, comments and weeks
  if not new_sch:
    new_sch = whole_term_sch
    new_sch.pk = None
    new_sch.save()

    new_sch.import_to_next_term = False
    new_sch.name = new_sch.name + ' - transfer'
    new_sch.comments = new_sch.comments + ' // used for transfers'
    new_sch.priority = old_priority + 1
    weeks = ''
    # goes up to semi-annual
    for i in range(start_week, 19):
      weeks = weeks + str(i) + ','
    new_sch.weeks = weeks[:-1]

    for ev in new_evs:
      new_sch.events.add(ev)
      new_sch.save()
    new_sch.save()

  new_sch.trainees.add(trainee)
  new_sch.save()

  # move rolls that are attached to the old schedule
  for r_id in old_rolls_ids:
    roll = Roll.objects.get(pk=r_id)
    new_ev = new_evs.filter(weekday=roll.event.weekday).first()
    roll.event = new_ev
    roll.save()

  old_ev_name = old_sch.first().events.filter(weekday=3).first().code
  new_ev_name = new_evs.filter(weekday=3).first().code
  return "successfully moved " + str(trainee) + " from " + str(old_ev_name) + " to " + str(new_ev_name) + " starting from week " + str(start_week)


def next_dow(d, day):
  while d.weekday() != day:
    d += timedelta(1)
  return d


def should_split_schedule(schedule, week):
  """ Returns true if the schedule should be split if the schedule change takes place
    starting the inputted week. """
  if not schedule.term or not schedule.term.current:
    return False

  # Parent schedules should not be split.  Instead, split one of the split schedules off of
  # the parent schedule
  if schedule.is_parent_schedule:
    return False

  # If active before and after the given week, then we'll need to split
  weeks = [int(x) for x in schedule.weeks.split(',')]

  active_before = False
  active_after = False

  for w in range(1, week):
    if w in weeks:
      active_before = True

  if max(weeks) >= week:
    active_after = True

  if active_before and active_after:
    return True

  return False


def split_schedule(schedule, week):
  from schedules.models import Schedule
  """ If the schedule needs to split, returns a tuple of schedules--the parent schedule
    (which may or may not be the schedule that was passed in), the earlier split of the
    schedule, and the later split of the schedule.  Both of the splits will contain
    identical data to the original--only the weeks and pertinent settings on the schedules
    will have changed.  Make sure that any non-trainee changes you make are propagated to
    both the parent schedule and the newer split if you want the changes to be imported
    to the schedule on the following term.

    If the schedule does not need to be split, you will get a tuple of parent schedule,
    None, passed in schedule.  The parent schedule and passed in schedule may be the same.
  """

  if not should_split_schedule(schedule, week):
    if schedule.parent_schedule:
      return schedule.parent_schedule, None, schedule
    else:
      return schedule, None, schedule

  # clone
  schedule_copy = Schedule.objects.get(id=schedule.id)
  s1 = schedule_copy
  s1.pk = None
  s1.save()

  schedule_copy = Schedule.objects.get(id=schedule.id)
  s2 = schedule_copy
  s2.pk = None
  s2.save()

  s1.trainees = schedule.trainees.all()
  s2.trainees = schedule.trainees.all()

  s1.events = schedule.events.all()
  s2.events = schedule.events.all()

  weeks = [int(x) for x in schedule.weeks.split(',')]
  s1_weeks = [i for i in weeks if i < week]
  s2_weeks = [i for i in weeks if i >= week]
  s1.weeks = ','.join(map(str, s1_weeks))
  s2.weeks = ','.join(map(str, s2_weeks))

  # splits should not be ported to the following term.  Only parent schedules get moved, so
  # make sure changes are made both to s2 and parent schedule (after return)
  s1.import_to_next_term = s2.import_to_next_term = False

  # splits are parented to the original parent, if it exists
  if not schedule.parent_schedule:
    s1.parent_schedule = s2.parent_schedule = schedule
    schedule.is_parent_schedule = True

  s1.is_parent_schedule = s2.is_parent_schedule = False
  s1.trainee_set_locked = True

  s1.save()
  s2.save()

  schedule.trainees = []
  schedule.trainee_set_locked = True

  # If this schedule has a parent schedule, this schedule is no longer needed.
  # Todo(import2): After writing unit tests, consider if it's worthwhile to make it so
  # we don't create an extra schedule in this case (i.e. instead of creating s1, just
  # use schedule directly)
  if schedule.parent_schedule:
    schedule.is_deleted = True
  else:
    schedule.is_parent_schedule = True

  schedule.save()

  if schedule.parent_schedule:
    return schedule.parent_schedule, s1, s2
  else:
    return schedule, s1, s2

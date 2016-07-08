from datetime import datetime
from collections import OrderedDict
from copy import copy
from sets import Set

class EventUtils:
  # Handles ev.day correclty and returns all ev in terms of week, weekday
  @staticmethod
  def compute_prioritized_event_table(w_tb, weeks, evs, priority):
    '''
    Handles priority collision detection and normalizes ev.day events
    '''
    for ev in evs:
      # manually calculate week if day is specified
      for w in (weeks if not ev.day else [ev.week_from_date(ev.day),]):
        # absolute date is already calculated
        weekday = ev.weekday
        ev.priority = priority
        day_evnts = w_tb.setdefault((w, weekday), set())

        # check for conflicts. 
        # append ev to list, check for any conflicts (intersectinng time), replace any intersecting evs
        for day_evnt in day_evnts.copy():
          if day_evnt.check_time_conflict(ev):
            # replace ev if conflict
            # delete any conflicted evs
            day_evnts.remove(day_evnt)

        # append after remove all conflicting events
        day_evnts.add(ev)

    return w_tb

  # Create list from table and add absolute date to event
  @staticmethod
  def export_event_list_from_table(w_tb):
    event_list=[]
    for (w, d), evs in w_tb.items():
      for ev in evs:
        date = ev.date_for_week(w)
        # calc date from w
        ev.start_datetime = datetime.combine(date, ev.start)
        ev.end_datetime = datetime.combine(date, ev.end)
        # append a copy of ev to answer list you will return. B/c same event can have multiple instance across different weeks
        event_list.append(copy(ev))
    return event_list


  @staticmethod
  def collapse_priority_event_trainee_table(weeks, schedules, t_set):
    '''
      Go through all schedules and override conflicting events trainee roster list
      with trainee list that has higher priority

      Returns table {ev: set([trainee1, trainee2])} in order of increasing start/end time of ev
    '''
    import copy

    # Prioritized weekly event table
    # {(w, weekday): OrderedDict(ev: set([trainee1, trainee2,]))}
    w_tb = OrderedDict()

    wk_set = set(weeks)

    for schedule in schedules:
      # order events so collision detection behavior is very predictable
      evs = schedule.events.order_by('weekday', 'start', 'end')
      valid_weeks = set([int(x) for x in schedule.weeks.split(',')]).intersection(wk_set)
      t_intersect = set(schedule.trainees.all()).intersection(t_set)
      for ev in evs:
        # print 'ev', ev.weekday, ev.start, ev.day, ev
        # manually calculate week if day is specified
        for w in (valid_weeks if not ev.day else set([ev.week_from_date(ev.day),]).intersection(wk_set)):
          # absolute date is already calculated
          weekday = ev.weekday
          ev.priority = schedule.priority
          day_evnts = w_tb.setdefault((w, weekday), OrderedDict())

          # check for conflicts. 
          # append ev to list, check for any conflicts (intersectinng time), replace any intersecting evs
          # Cop day_evnts b/c later on will modified same events over multi-weeks to add start_time
          for day_evnt in day_evnts.copy():
            if day_evnt.check_time_conflict(ev):
              # replace ev if conflict
              # delete any conflicted evs
              # remove trainees in t_intersect from conflicting event and add new event with trainees in it
              day_evnts[day_evnt] -= t_intersect

          # Add new ev to day with t_intersect trainees inside
          day_evnts[ev] = t_intersect.copy()

    return w_tb


  @staticmethod
  def export_typed_ordered_roll_list(w_tb, type):
    # OrderedDict so events are in order of start/end time when iterated out unto the template
    event_trainee_tb = []
    for (w, d), evs in w_tb.items():
      for ev, ts in evs.items():
        # only calculate ev for type wanted
        if ev.type == type:
          date = ev.date_for_week(w)
          # calc date from w
          ev.start_datetime = datetime.combine(date, ev.start)
          ev.end_datetime = datetime.combine(date, ev.end)

          # append a copy of ev to answer list you will return. B/c same event can have multiple instance across different weeks
          event_trainee_tb.append((copy(ev), ts))

    return event_trainee_tb

  @staticmethod
  def export_ordered_roll_list_for_event_in_week(w_tb, event, week):
    # OrderedDict so events are in order of start/end time when iterated out unto the template
    event_trainee_tb = set()
    for (w, d), evs in w_tb.items():
      for ev, ts in evs.items():
        # only calculate ev for type wanted and for week wanted
        if ev == event:
          if w == week:
            event_trainee_tb.add(ts)

    return event_trainee_tb

  @staticmethod
  def flip_roll_list(roll_table):
    t_ev_tb = {}
    ordered_ev_list = []

    for ev, ts in roll_table:
      ordered_ev_list.append(ev)
      for t in ts:
        t_ev_tb.setdefault(t, []).append(ev)

    return (ordered_ev_list, t_ev_tb)
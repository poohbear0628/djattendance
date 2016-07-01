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
    print 'lib ev', evs
    for ev in evs:
      if ev.day:
        # manually calculate week if day is specified
        weeks = [ev.week_from_date(ev.day),]

      for w in weeks:
      # absolute date is already calculated
        weekday = ev.weekday
        ev.priority = priority
        day_evnts = w_tb.setdefault((w, weekday), set())

      # check for conflicts. 
      # append ev to list, check for any conflicts (intersectinng time), replace any intersecting evs
      for day_evnt in day_evnts.copy():
        print 'day', day_evnt
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

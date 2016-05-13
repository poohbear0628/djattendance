from .models import *
from django.db.models import Q
from datetime import timedelta

from ortools.graph import pywrapgraph
import random

from graph import DirectedFlowGraph

from sets import Set

from django.shortcuts import render_to_response

from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.template import RequestContext

'''
Pseudo-code for algo


-----
Hard-constraint

Get all the services without day (repeating services) + date falls within this coming week
Get all the workergroups + roles + count (related to services)

duplicate services node with multiple count for workergroups (single instance)

Get all workers?

Create edges based on worker.services_needed

check only 1 service per day, weekday
check conflicting services on same day -> flow into a single bottle-neck node

--------
Trim operation?
Apply exceptions to trim workers from services

All pre-assigned, take out of the graph (designated, shuttle, etc.), if 
assignment counts as service, trim all other services that day

how to check for time conflict
All pinned assignments -> check time conflict but not count as +1 service?



All time conflict will be caused only by irregular services
(piano, AV, Shuttle, Outline Sisters)


------
special operation

to choose star assignments for duo star assignments
flip coin for brother/sister and create edges

-------
Soft-constraint (edges cost)

Calculate the cost for the edges

pull history, health

health (base weight of trainee -> sink)
history (+1 for each service already done before), more weight, closer to current date (3 weeks?)
(visualize it for SS) experience (-0.5 for each service already done before)
noise (+- noise for randomly in the cost run each time)? maybe optional

AssignmentPool.workload (base weight of each trainee -> service)




-------
star assignment -> maybe greedy trim star edges and then 
randomly flip coins to ratio of brother/sister star ratio
and trim graph appropriately

(future dev) -> Maybe incorporate how constrained each star in the flipping 
probabilities to bias less constrained stars




'''

def hydrate(services):
  for s in services:
    # wg.get_workers to use filters in the future
    s.workers = [wg.get_workers() for wg in s.worker_groups.all()]
    s.assignmentpool = s.assignmentpool_set.all()
    print 'service', s, 'assignmentpool', len(s.assignmentpool)
    for p in s.assignmentpool:
      p.workers = Set(p.worker_group.get_workers())
    # [p.workers = p.worker_groups.workers.all() for p in s.assignmentpool]

  return services

def assign():
  cws = WeekSchedule.current_week_schedule()

  # get start date and end date of effective week

  week_start = cws.start
  week_end = cws.start + timedelta(days=6)

  # Gets services that are active with day null or day between week range
  css = SeasonalServiceSchedule.objects.filter(Q(services__day__isnull=True) | Q(services__day__range=(week_start, week_end))).filter(active=True, services__active=True).distinct()
  # may have to get services active for all 
  services = Set()
  for ss in css:
    services.union_update(Set(ss.services.filter(Q(day__isnull=True) | Q(day__range=(week_start, week_end))).filter(active=True).distinct()))
    # print ss.services
  # active_services = Service.objects.filter(active=True)


  print len(services)
  services = hydrate(services)

  # get all the valid exceptions to hydrate
  exceptions = Exception.objects.filter(active=True, start__gte=week_start).filter(Q(end__isnull=True) | Q(end__lte=week_end)).distinct()

  # hydrate exceptions
  for e in exceptions:
    e.hydated_services = hydrate(e.services.all())

  trim_service_exceptions(services, exceptions)

  # TODO: time conflict checking

  graph = build_graph(services)

  (status, soln) = graph.solve_partial_flow(debug=True)

  return (status, soln)


# Checks to see if there's a intersection between 2 time ranges
def is_overlap(a, b):
  # (StartA <= EndB) and (EndA >= StartB)
  return (a.calculated_weekday == b.calculated_weekday) and (a.start <= b.end) and (a.end >= b.start)

def sort_services(services):
  l = list(services)

  # in place stable sort
  l.sort(key = lambda x: (x.calculated_weekday, x.start, x.end))

  return l


'''
  Only have to worry about service time overlap conflict if I assign trainees 
  more than 1 service per day.
'''
def build_service_conflict_table(services):
  # build a table of service mapping to other services in conflicting times/day
  c_tb = {}

  l = sort_services(services)
  len_l = len(l)

  # for each service, check to see if it overlaps with next service and keep checking
  # until no more overlaps and then move on to the next service. Build collision table 2-way
  for i in range(len_l - 1):
    j = i + 1
    while j < len_l and is_overlap(l[i], l[j]):
      # if overlap build 2-way table
      c_tb.setdefault(l[i], Set()).add(l[j])
      # reverse
      c_tb.setdefault(l[j], Set()).add(l[i])

      j += 1


  # Run time: if every item overlaps with every other item, O(n^2), if only ~1, O(n)

  return c_tb





def trim_service_exceptions(services, exceptions):
  # go through all exceptions and delete workers out of hydrated services
  for e in exceptions:
    ws = e.workers.all()
    ss = e.hydated_services
    print 'all services', services
    for s in ss:
      print 'excpetion service', s
      # if service mentioned in exception
      if s in services:
        print 'EXCPETIONS!!!!!', s, s.assignmentpool
        # remove all trainees in ts from all the assignmentpool.workers.trainee
        for a in s.assignmentpool:
          for w in ws:
            # loop through all trainees listed in exception
            if w in a.workers:
              # remove worker
              a.workers.remove(w)
              print 'removing worker', w, a.workers

def build_graph(services):
  total_flow = 0
  min_cost_flow = DirectedFlowGraph()


  # TODO: overlapping services on same day. Maybe trim iterately reflow to solve


  # Add services to source
  for s in services:
    '''
      Loop through all the services, all the pools
      source -> (service, pool) -> workers
    '''
    source = 'Source'

    for pool in s.assignmentpool:
      min_cost_flow.add_or_set_arc(source, (s, pool), pool.workers_required, 1, 0)

      print 'pool', s, pool, pool.workers_required

      total_flow += pool.workers_required

  # Trim via exceptions from workers
  # rejoin conflicting times + feed into 1 day (worker, weekday)
  # all (worker, weekday) feed into worker

  # Add trainees to services
  for s, pool in min_cost_flow.get_stage(1):
    for w in pool.workers:

      # Calculate the cost
      # s_freq = 0
      # if s.name in w.service_frequency:
      #   s_freq = w.service_frequency[s.name]

      # TODO: Test s, pool will be the same in freq table as keys
      s_freq = w.service_frequency[(s, pool)] if (s, pool) in w.service_frequency else 0



      # Formula: cost = service workload + service history frequency
      cost = pool.workload + s_freq

      min_cost_flow.add_or_set_arc((s, pool), w, 1, cost, 1)


  # add trainees all to sink
  for w in min_cost_flow.get_stage(2):
    sink = 'Sink'

    num_services = w.services_needed
    print w, num_services
    sick_lvl = max(10 - w.health, 1)  # min sick_lvl is 1 so load balancing works
    for x in range(1, num_services + 1):
      cost = x * sick_lvl # Not sure this is the metric we want to use?

      min_cost_flow.add_or_set_arc(w, sink, 1, cost, 2, x)


  print '### total flow ###', total_flow

  min_cost_flow.set_total_flow(total_flow)

  return min_cost_flow


def services_view(request):
  status, soln = assign()
  print 'solution:', status, soln
  # status, soln = 'OPTIMAL', [(1, 2), (3, 4)]

  if status == 'OPTIMAL':
    ctx = {
      'assignments': soln,
    }
    return render_to_response('services/services_view.html', ctx) #context_instance=RequestContext(request), 
  else:
    return HttpResponseBadRequest('Status calculated: %s' % status)





'''
ArcIndex AddArcWithCapacityAndUnitCost(
  NodeIndex tail, NodeIndex head,
    FlowQuantity capacity,
     CostValue unit_cost);
'''

'''

  services.worker_groups

  # Make network nodes for services
  # Service.name : assignmentpool_set.role x assignmentpool_set.workers_required

  services.assignmentpool_set.worker_group.workers

  {
    servicename: service
  }

  {
    workerid: worker
  }


  {
    servicename: {
      workers: [
        worker1,
        worker2
      ],
      role: worker,
      workers_required: 3,
      workload: 3
    },
    day: Monday
  }

  worker = {
    history: [],
    service_cap: 3,
    service_needed: 3
  }

'''

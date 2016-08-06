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

from rest_framework_bulk import (
    BulkModelViewSet,
    BulkSerializerMixin,
    BulkListSerializer
)

from rest_framework.serializers import ModelSerializer

from .serializers import UpdateWorkerSerializer, ServiceSlotWorkloadSerializer

from aputils.trainee_utils import trainee_from_user

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

ServiceSlot.workload (base weight of each trainee -> service)




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
    # s.workers = [wg.get_workers() for wg in s.worker_groups.all()]
    # s.serviceslot = s.serviceslot_set.all()
    print 'service', s, 'serviceslot', len(s.serviceslot)
    for p in s.serviceslot:
      # blow away cache
      wg = p.worker_group
      workers = wg.get_workers#.prefetch_related(Prefetch('assignments', queryset=Assignment.objects.filter(week_schedule=cws, pin=True), to_attr='pinned_assignments'))
      # del wg.get_workers
      p.workers = Set(workers)
    # [p.workers = p.worker_groups.workers.all() for p in s.serviceslot]

  return services

def assign(cws):

  # get start date and end date of effective week

  week_start = cws.start
  week_end = cws.start + timedelta(days=6)

  # Gets services that are active with day null or day between week range
  css = SeasonalServiceSchedule.objects.filter(active=True)\
  .prefetch_related('services')
  # .prefetch_related('services',
  #   Prefetch('services__serviceslot_set', queryset=ServiceSlot.objects.order_by('workers_required'), to_attr='serviceslot'),
  #   'services__worker_groups__workers',
  #   'services__worker_groups__workers__trainee',
  #   Prefetch('services__worker_groups__workers__assignments', queryset=Assignment.objects.order_by('week_schedule__start'), to_attr='historical_assignments')).select_related() #Q(services__day__isnull=True) | Q(services__day__range=(week_start, week_end))).filter(active=True, services__active=True).distinct()
  # may have to get services active for all
  services = Set()
  for ss in css:
    s = ss.services.filter(Q(day__isnull=True) | Q(day__range=(week_start, week_end)))\
    .prefetch_related(Prefetch('serviceslot_set', queryset=ServiceSlot.objects.order_by('workers_required'), to_attr='serviceslot'),
    'worker_groups__workers',
    'worker_groups__workers__trainee',
    Prefetch('worker_groups__workers__assignments', queryset=Assignment.objects.order_by('week_schedule__start'), to_attr='historical_assignments'),
    Prefetch('worker_groups__workers__assignments', queryset=Assignment.objects.filter(week_schedule=cws, pin=True), to_attr='pinned_assignments')).select_related()\
    .distinct()
    services.union_update(Set(s))
    # print ss.services
  # active_services = Service.objects.filter(active=True)


  print len(services)
  services = hydrate(services)

  # Get all active exception in time period with active or no schedule constrains
  exceptions = Exception.objects.filter(active=True, start__lte=week_start)\
              .filter(Q(end__isnull=True) | Q(end__gte=week_end))\
              .filter(Q(schedule=None) | Q(schedule__active=True))\
              .distinct()
  exceptions = exceptions.prefetch_related('services', 'services__serviceslot_set', 'services__worker_groups__workers', 'workers')


  trim_service_exceptions(services, exceptions)

  # TODO: time conflict checking

  print 'services', services

  # Build service frequency db for all the workers

  graph = build_graph(services)

  (status, soln) = graph.solve_partial_flow(debug=True)

  graph.graph()

  print 'soln', soln

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


# def trim_service_exceptions(services, exceptions):
#   # go through all exceptions and delete workers out of hydrated services
#   for e in exceptions:
#     ws = e.workers.all()
#     ss = e.hydated_services
#     # print '!!!!!!!!all services exception', services, ws, ss
#     for s in ss:
#       print 'excpetion service', s
#       # if service mentioned in exception
#       if s in services:
#         print 'EXCPETIONS!!!!!', s, s.serviceslot
#         # remove all trainees in ts from all the serviceslot.workers.trainee
#         for w in ws:
#           for a in s.serviceslot:
#             print 'checking worker exception', w, a.workers
#             # loop through all trainees listed in exception
#             if w in a.workers:
#               # remove worker
#               a.workers.remove(w)
#               print 'removing worker!!!!!!!!!!!1', w, a.workers



def trim_service_exceptions(services, exceptions):
  # build exception table and then remove everyone in that table
  s_w_tb = {}
  for e in exceptions:
    ws = e.workers.all()
    for s in e.services.all():
      for w in ws:
        s_w_tb.setdefault(s, Set()).add(w)
  # go through all exceptions and delete workers out of hydrated services
  for s in services:
    print 'excpetion service', s
    # if service mentioned in exception
    if s in s_w_tb:
      ws = s_w_tb[s]
      # print 'EXCPETIONS!!!!!', s, s.serviceslot
      # remove all trainees in ts from all the serviceslot.workers.trainee
      for w in ws:
        for a in s.serviceslot:
          # print 'checking worker exception', w, a.workers
          # loop through all trainees listed in exception
          if w in a.workers:
            # remove worker
            a.workers.remove(w)
            print 'removing worker!!!!!!!!!!!1', w, a.workers


def build_graph(services):
  total_flow = 0
  min_cost_flow = DirectedFlowGraph()


  # TODO: overlapping services on same day. Maybe trim iterately reflow to solve


  # Add services to source
  for s in services:
    '''
      Loop through all the services, all the slots
      source -> (service, slot) -> workers
    '''
    source = 'Source'

    for slot in s.serviceslot:
      min_cost_flow.add_or_set_arc(source, (s, slot), capacity=slot.workers_required, cost=1, stage=0)

      print 'slot', s, slot, slot.workers_required, slot.workers

      total_flow += slot.workers_required

  # Trim via exceptions from workers
  # rejoin conflicting times + feed into 1 day (worker, weekday)
  # all (worker, weekday) feed into worker

  # Add trainees to services
  for s, slot in min_cost_flow.get_stage(1):
    print 'add arcs', s, slot, slot.workers

    for w in slot.workers:

      # Calculate the cost
      # s_freq = 0
      # if s.name in w.service_frequency:
      #   s_freq = w.service_frequency[s.name]

      # TODO: Test s, slot will be the same in freq table as keys
      s_freq = w.service_frequency[slot.id] if slot.id in w.service_frequency else 0



      # Formula: cost = service workload + service history frequency
      cost = slot.workload + s_freq

      min_cost_flow.add_or_set_arc((s, slot), (w, s.weekday), capacity=1, cost=1, stage=1)

  # Add 1 service/day constraint to each trainee
  for w, weekday in min_cost_flow.get_stage(2):
    min_cost_flow.add_or_set_arc((w, weekday), w, capacity=1, cost=1, stage=2)


  # add trainees all to sink
  for w in min_cost_flow.get_stage(3):
    sink = 'Sink'

    # Only add edges for none pinned assignment capacity left
    num_services = w.services_cap - len(w.pinned_assignments)
    print w, num_services
    sick_lvl = max(10 - w.health, 1)  # min sick_lvl is 1 so load balancing works
    for x in range(1, num_services + 1):
      cost = x * sick_lvl # Not sure this is the metric we want to use?

      min_cost_flow.add_or_set_arc(w, sink, capacity=1, cost=cost, stage=3, key=x)


  print '### total flow ###', total_flow

  min_cost_flow.set_total_flow(total_flow)

  return min_cost_flow


def services_assign(request):
  user = self.request.user
  trainee = trainee_from_user(user)
  cws = WeekSchedule.get_or_create_current_week_schedule(trainee)
  status, soln = assign(cws)
  print 'solution:', status, soln
  # status, soln = 'OPTIMAL', [(1, 2), (3, 4)]

  workers = Worker.objects.select_related('trainee').all()

  if status == 'OPTIMAL':
    ctx = {
      'assignments': soln,
      'workers': workers,
    }
    return render_to_response('services/services_view.html', ctx, context_instance=RequestContext(request))
  else:
    return HttpResponseBadRequest('Status calculated: %s' % status)


def services_view(request, run_assign=False):
  # status, soln = 'OPTIMAL', [(1, 2), (3, 4)]
  user = request.user
  trainee = trainee_from_user(user)
  cws = WeekSchedule.get_or_create_current_week_schedule(trainee)

  if run_assign:
    status, soln = assign(cws)
  else:
    status, soln = None, None

  workers = Worker.objects.select_related('trainee').all()

  categories = Category.objects.prefetch_related(Prefetch('services', queryset=Service.objects.order_by('weekday')), 'services__serviceslot_set').order_by('services__start').distinct()

  assignments = Assignment.objects.select_related('week_schedule', 'service', 'services_lot').prefetch_related('workers').all()

  worker_assignments = Worker.objects.select_related('trainee').prefetch_related(Prefetch('assignments',
    queryset=Assignment.objects.filter(week_schedule=cws).select_related('service', 'service__category').order_by('service__weekday'),
    to_attr='week_assignments'))

  # attach services directly to trainees for easier template traversal
  for worker in worker_assignments:
    service_db = {}
    for a in worker.week_assignments:
      service_db.setdefault(a.service.category, []).append(a.service)
    worker.services = service_db

  ctx = {
    'status': status,
    'assignments': soln,
    'workers': workers,
    # 'slots': slots,
    'categories': categories,
    'report_assignments': worker_assignments,
  }
  return render_to_response('services/services_view.html', ctx, context_instance=RequestContext(request))


################## API Views ###########################

class UpdateWorkerSerializer(BulkSerializerMixin, ModelSerializer):
  class Meta(object):
    model = Worker
    list_serializer_class = BulkListSerializer
    fields = ['id', 'health', 'services_cap']



class UpdateWorkersViewSet(BulkModelViewSet):
  queryset = Worker.objects.all()
  serializer_class = UpdateWorkerSerializer
  # filter_backends = (filters.DjangoFilterBackend,)
  # filter_class = RollFilter
  def allow_bulk_destroy(self, qs, filtered):
      return filtered



class ServiceSlotWorkloadViewSet(BulkModelViewSet):
  queryset = ServiceSlot.objects.all()
  serializer_class = ServiceSlotWorkloadSerializer
  # filter_backends = (filters.DjangoFilterBackend,)
  # filter_class = RollFilter
  def allow_bulk_destroy(self, qs, filtered):
      return filtered


'''
ArcIndex AddArcWithCapacityAndUnitCost(
  NodeIndex tail, NodeIndex head,
    FlowQuantity capacity,
     CostValue unit_cost);
'''

'''

  services.worker_groups

  # Make network nodes for services
  # Service.name : serviceslot_set.role x serviceslot_set.workers_required

  services.serviceslot_set.worker_group.workers

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

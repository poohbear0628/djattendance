from .models import *
from django.db.models import Q
from datetime import timedelta

from ortools.graph import pywrapgraph
import random

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
    s.workers = [wg.workers.all() for wg in s.worker_groups.all()]
    s.assignmentpool = s.assignmentpool_set.all()
    for p in s.assignmentpool:
      p.workers = p.worker_group.workers.all() 
    # [p.workers = p.worker_groups.workers.all() for p in s.assignmentpool]

  return services

def assign():
  cws = WeekSchedule.current_week_schedule()

  # get start date and end date of effective week

  week_start = cws.start
  week_end = cws.start + timedelta(days=6)

  # Gets services that are active with day null or day between week range
  css = SeasonalServiceSchedule.objects.filter(active=True, services__active=True).filter(Q(services__day__isnull=True) | Q(services__day__range=(week_start, week_end)))
  # may have to get services active for all 
  services = []
  for ss in css:
    services += ss.services.all()
    print ss.services
  # active_services = Service.objects.filter(active=True)

  services = hydrate(services)

  buildGraph(services)

  return services



'''
Need graph object represent

node, arc, capacity, weight

named nodes (types)

add adj directly to python objects instead of juggling node/arc indexes

alter adj freely (set/delete) -> cost/capacity



'''

# class Arc:


# class Node:
#   index, object, children, parent


from sets import Set

class Arc:
  
  def __init__(self, fro, to, capacity=1, cost=1):
    self.fro = fro
    self.to = to
    self.capacity = capacity
    self.cost = cost

  def __eq__(self, other):
    return self.fro == other.fro and self.to == other.to and \
      self.capacity == other.capacity and self.cost == other.cost


class Node:
  obj = None
  outflow = Set()
  inflow = Set()

  def __init__(self, obj):
    self.obj = obj

  def add_arc(self, node, capacity=1, cost=1):
    arc = Arc(self, node, capacity, cost)
    self.outflow.add(arc)
    node.inflow.add(arc)




class TwoWayIndexedDict(dict):
  def __setitem__(self, key, value):
    # Remove any previous connections with these values
    if key in self:
      del self[key]
    if value in self:
      del self[value]
    dict.__setitem__(self, key, value)
    dict.__setitem__(self, value, key)
  def __delitem__(self, key):
    dict.__delitem__(self, self[key])
    dict.__delitem__(self, key)
  def __len__(self):
    """Returns the number of connections"""
    return dict.__len__(self) // 2

'''

add_arc(fro, to, capacity, cost, stage)
'''

class DirectedFlowGraph:
  # source, sink, nodes, adj, ortool_graph

  # obj: index
  nodes = {}

  # stages[1] = Set([node])
  stages = {}
  # (fromIndex, toIndex): (capacity, cost)
  # adj[u][v] = (capacity, cost)
  adj = {}
  # total_flow to flow through whole graph
  total_flow = 0


  def __len__(self):
    return len(self.nodes)

  def __getitem__(self, n):
    return self.adj[n]

  def __contains__(self, n):
    try:
      return n in self.nodes
    except TypeError:
      return False

  def __iter__(self):
    return iter(self.nodes)

  # def copy(self):
  #   from copy import deepcopy
  #   return deepcopy(self)

  def set_total_flow(self, flow):
    self.total_flow = flow

  def get_stage(self, stage):
    # Return stages[stage] if exists or else Set()
    return self.stages.get(stage, Set())

  def get_node_index(self, node, stage=1):
    if node not in self.nodes:
      self.nodes[node] = len(self.nodes)
      # Keep track of node stages
      st = self.stages.setdefault(stage, Set())
      st.add(node)

      return self.nodes[node]

  def add_or_set_arc(self, fro, to, capacity=1, cost=1, stage=1):
    fi = self.get_node_index(fro, stage)
    ti = self.get_node_index(to, stage + 1)

    # Get fi if exists if not create a new dict for that key and return it
    edges = self.adj.setdefault(fi, dict())
    edges[ti] = (capacity, cost)

  def remove_arc(self, u, v):
    try:
      del self.adj[u][v]
    except KeyError:
      raise Exception("The edge %s-%s is not in the graph" % (u, v))


  def get_arc(self, fro, to):
    if fro in self.adj and to in self.adj[fro]:
      return self.adj[fro][to]
    else:
      return None

  # Compile into a ORTOOLS graph for faster calculations in C
  def compile(self):
    if self.total_flow:
      raise Exception('You forgot to set a positive total flow!')

    min_cost_flow = pywrapgraph.SimpleMinCostFlow()

    for (fro, to), (cap, cost) in self.adj.items():
      min_cost_flow.AddArcWithCapacityAndUnitCost(fro, to, cap, cost)

    # Set flow for source/sink
    min_cost_flow.SetNodeSupply(0, self.total_flow)
    min_cost_flow.SetNodeSupply(len(self.nodes), -self.total_flow)

    self.ortool_graph = min_cost_flow

    return min_cost_flow

  def print_solution(self):
    self.soln = []

    g = self.ortool_graph

    if self.status == g.OPTIMAL:
      print 'Total flow cost', g.OptimalCost()
      print 'Total max flow', g.MaximumFlow()
      print 'Total # of nodes', g.NumNodes()
      print 'Total # of edges', g.NumArcs()
      for i in range(0, g.NumArcs()):
        if g.Flow(i) > 0:
          self.soln.append([ortool_graph.Tail(i), ortool_graph.Head(i)])
          # print 'From source %d to target %d: cost %d' % (
          #     g.Tail(i),
          #     g.Head(i),
          #     g.UnitCost(i))
          self.graph()
    else:
      print 'There was an issue with the min cost flow input.', status, STATUS[status]


  # Solve with max partial flow allowed in graph
  def solve_partial_flow(self):
    self.compile()
    self.status = self.ortool_graph.SolveMaxFlowWithMinCost()

    self.print_solution()

  # solve graph for Full flow: compile() first and then .solve()
  def solve(self):
    self.compile()

    self.status = self.ortool_graph.Solve()

    self.print_solution()

    
  def graph(self):
    filename = '/home/rayli/Desktop/data.js'
    f = open(filename,'w')
    # print >>f, 'whatever'

    ########### js stuff!

    js_edges = []
    for fro in self.adj:
      for to in self.adj[fro]:
        capacity, cost = self.adj[fro][to]
        js_edges.append({'source': fro, 'target': to, 'weight': cost})


    contraints = []
    # loop through all the stages in order and create column constraints for each
    stages = self.stages.keys()
    stages.sort()

    ns = []

    for i in stages:
      st = self.stages[i]
      st_constraint = []

      st_ns = []
      # iterating through a set
      for n in st:
        index = self.nodes[n]
        st_constraint.append({"node":str(index), "offset":"0"})

        st_ns.append(index)

      constraints.append({"type": "alignment", "axis":"x", "offsets": st_constraint})

      ns.append(st_ns)




    code = '''
var color = ["#1f77b4", "#aec7e8", "#ff7f0e", "#ffbb78", "#2ca02c", "#98df8a", "#d62728", "#ff9896", "#9467bd", "#c5b0d5", "#8c564b", "#c49c94", "#e377c2", "#f7b6d2", "#7f7f7f", "#c7c7c7", "#bcbd22", "#dbdb8d", "#17becf", "#9edae5"];
var services = %d;
var trainees = %d;
var st_ns = %s;
var ns = [];
var n_tot = %d;
var scaling = 20;

// source/sink
//ns.push({id: 0, fixed: true, x: 100, y: services * scaling});
//ns.push({id: n_tot - 1, fixed: true, x: 500, y: services * scaling});

for (var i in st_ns) {
  // In stage i nodes
  var ns = st_ns[i];
  for (var j in ns) {
    var n = ns[j];
    ns.push({id: j, fixed: true, x: i * X_OFFSET, y: j * scaling});
  }
}
''' % (services, trainees, str(ns), min_cost_flow.NumNodes())

    f.write(code)
    # print >>f code
    f.write('constraints = ' + str(contraints) + '\n')
    f.write('lks = ' + str(js_edges) + '\n')
    f.write('solns = ' + str(self.soln) + '\n')
 






class Node:
  title = 'Default Node title'

  def __init__(self, title):
    self.title = title



def buildGraph(services):
  # service/trainee labels
  s_l = 'service_'
  t_l = 'trainee_'

  ss_edges = [] # Source to service
  st_edges = [] # Service to Trainee
  tt_edges = [] # Trainee to sink t

  pos = {}
  s_nodes = []
  t_nodes = []


  ###########

  e_count = 0
  node_count = 0
  total_flow = 0

  min_cost_flow = pywrapgraph.SimpleMinCostFlow()


# TODO: Figure out way to keep track of node index to node object conversion automatically
  service_lookup = {}
  worker_lookup = {}
  worker_reverse_lookup = {}

  # TODO: overlapping services on same day. Maybe trim iterately reflow to solve


  # Add services to source
  for s in services:
    '''
      Loop through all the services, all the pools
      source -> (service, pool) -> workers
    '''
    for pool in s.assignmentpool:
      node_count += 1
      (fro, to) = (0, node_count)
      ss_edges.append((fro, to, 1))
      s_nodes.append(to)

      service_lookup[to] = (s, pool)

      # there could be many assignmentpool reused for different services, increase capacity




      min_cost_flow.AddArcWithCapacityAndUnitCost(fro, to, pool.workers_required, 1)

      e_count+=1




  # Add trainees to services
  for i, (s, pool) in service_lookup.items():
    for w in pool.workers:
      fro = i
      # Have to do this lame uniqueness checking b/c I can't easily loop through workers
      if w in worker_reverse_lookup:
        to = worker_reverse_lookup[w]
      else:
        node_count += 1
        to = node_count
        worker_reverse_lookup[w] = to
        worker_lookup[to] = w
      # (fro, to) = (i, node_count)

      # Calculate the cost
      # s_freq = 0
      # if s.name in w.service_frequency:
      #   s_freq = w.service_frequency[s.name]

      # TODO: Test s, pool will be the same in freq table as keys
      s_freq = w.service_frequency[(s, pool)] if (s, pool) in w.service_frequency else 0

      # Formula: cost = service workload + service history frequency
      cost = pool.workload + s_freq
      st_edges.append((fro, to, cost))

      min_cost_flow.AddArcWithCapacityAndUnitCost(fro, to, 1, cost)
      e_count+=1


  
  print 'node_count, sink', node_count + 1
  
  print 'workers', worker_lookup

  # add trainees all to sink t
  for j, w in worker_lookup.items():
    (fro, to) = (j, node_count + 1)
    t_nodes.append(fro)

    num_services = w.services_needed
    print w, num_services
    sick_lvl = 10 - w.health
    for x in range(1, num_services + 1):
      cost = x * sick_lvl # Not sure this is the metric we want to use?
      tt_edges.append((fro, to, cost))

      min_cost_flow.AddArcWithCapacityAndUnitCost(fro, to, 1, cost)
      e_count+=1


  # TODO: calculate services workers_needed from pool
  services = len(service_lookup)
  trainees = len(worker_lookup)

  print 'total flow in graph', services


  # Set flow for source/sink
  min_cost_flow.SetNodeSupply(0, services)
  min_cost_flow.SetNodeSupply(node_count + 1, -services)


  ########### js stuff!

  all_edges = ss_edges + st_edges + tt_edges
  # print all_edges

  js_edges = []
  for (fro, to, cost) in all_edges:
    js_edges.append({'source': fro, 'target': to, 'weight': cost})

  s_align = []
  {"node":"1", "offset":"0"}
  for x in range(1, services + 1):
    s_align.append({"node":str(x), "offset":"0"})

  t_align = []
  for x in range(services + 1, services + trainees + 1):
    t_align.append({"node":str(x), "offset":"0"})


  ############

  STATUS = {
     0:   'NOT_SOLVED',
     1:   'OPTIMAL',
     2:   'FEASIBLE',
     3:   'INFEASIBLE',
     4:   'UNBALANCED',
     5:   'BAD_RESULT',
     6:   'BAD_COST_RANGE'
  };


  print 'solving...'

  status = min_cost_flow.Solve()


  soln = []

  if status == min_cost_flow.OPTIMAL:
    print 'Total flow cost', min_cost_flow.OptimalCost()
    print 'Total max flow', min_cost_flow.MaximumFlow()
    print 'Total # of nodes', min_cost_flow.NumNodes()
    print 'Total # of edges', min_cost_flow.NumArcs()
    for i in range(0, min_cost_flow.NumArcs()):
      if min_cost_flow.Flow(i) > 0:
        soln.append([min_cost_flow.Tail(i), min_cost_flow.Head(i)])
        # print 'From source %d to target %d: cost %d' % (
        #     min_cost_flow.Tail(i),
        #     min_cost_flow.Head(i),
        #     min_cost_flow.UnitCost(i))
    filename = '/home/rayli/Desktop/data.js'
    f = open(filename,'w')
    # print >>f, 'whatever'

    code = '''
var color = ["#1f77b4", "#aec7e8", "#ff7f0e", "#ffbb78", "#2ca02c", "#98df8a", "#d62728", "#ff9896", "#9467bd", "#c5b0d5", "#8c564b", "#c49c94", "#e377c2", "#f7b6d2", "#7f7f7f", "#c7c7c7", "#bcbd22", "#dbdb8d", "#17becf", "#9edae5"];
var services = %d;
var trainees = %d;
var ns = [];
var n_tot = %d;
var scaling = 20;

// source/sink
ns.push({id: 0, fixed: true, x: 100, y: services * scaling});
ns.push({id: n_tot - 1, fixed: true, x: 500, y: services * scaling});

for (var i = 1; i < (n_tot - 1); i++) {
  if (i <= services) {
    // services
    var c = color[1];
    nx = 200;
    ny = i * 2 * scaling;
  } else {
    // trainees
    var c = color[8];
    nx = 400;
    ny = ((services - trainees) * scaling) + (i - services) * 2 * scaling;
  }
  ns.push({id: i, fixed: true, color: c, x: nx, y: ny});
}
''' % (services, trainees, min_cost_flow.NumNodes())

    f.write(code)
    # print >>f code
    f.write('s_offsets = ' + str(s_align) + '\n')
    f.write('t_offsets = ' + str(t_align) + '\n')
    f.write('lks = ' + str(js_edges) + '\n')
    f.write('solns = ' + str(soln) + '\n')
  else:
    print 'There was an issue with the min cost flow input.', status, STATUS[status]

    soln = []
    for i in range(0, min_cost_flow.NumArcs()):
      soln.append([min_cost_flow.Tail(i), min_cost_flow.Head(i)])
      print 'From source %d to target %d: capacity %d, cost %d' % (
          min_cost_flow.Tail(i),
          min_cost_flow.Head(i),
          min_cost_flow.Capacity(i),
          min_cost_flow.UnitCost(i))




def __main__():


  s = assign()
  buildGraph(s)


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

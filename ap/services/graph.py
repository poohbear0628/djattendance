from ortools.graph import pywrapgraph
from sets import Set
import random
from collections import OrderedDict

'''
Need graph object represent

node, arc, capacity, weight

named nodes (types)

add adj directly to python objects instead of juggling node/arc indexes

alter adj freely (set/delete) -> cost/capacity



'''
class DirectedFlowGraph:
  # source, sink, nodes, adj, ortool_graph

  # obj: index

  STATUS = {
     0:   'NOT_SOLVED',
     1:   'OPTIMAL',
     2:   'FEASIBLE',
     3:   'INFEASIBLE',
     4:   'UNBALANCED',
     5:   'BAD_RESULT',
     6:   'BAD_COST_RANGE'
  }


  nodes = OrderedDict()

  # stages[1] = Set([node])
  stages = {}
  # (fromIndex, toIndex): (capacity, cost)
  # adj[u][v] = {0: (capacity, cost)}
  adj = {}
  # total_flow to flow through whole graph
  total_flow = 0

  soln_nodes = []

  ''' 
  Initializing with minimal_features cuts out any nice features of the graph
  It doesn't save edges info so you can't do: g[u][v] to get edges
  '''
  def __init__(self, ortool_graph=None, minimal_features=True):
    if ortool_graph is None:
      self.ortool_graph = pywrapgraph.SimpleMinCostFlow()
    else:
      self.ortool_graph = ortool_graph

    self.minimal_features = minimal_features

    if minimal_features:
      self.add_or_set_arc = self._fast_add_or_set_arc
    else:
      self.add_or_set_arc = self._add_or_set_arc


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

  def node_count(self):
    return len(self.nodes)

  def set_total_flow(self, flow):
    self.total_flow = flow

  # Return a Set of nodes in stage
  def get_stage(self, stage):
    '''
      Return Set of Node objs in each stage
    '''
    # Return stages[stage] if exists or else Set()
    return self.stages.get(stage, Set())

  # Gets the node index if already registered, if not register node and return index
  def get_node_index(self, node, stage=0):
    if node not in self.nodes:
      self.nodes[node] = len(self.nodes)
      # Keep track of node stages
      st = self.stages.setdefault(stage, Set())
      st.add(node)

    return self.nodes[node]

  def _fast_add_or_set_arc(self, fro, to, capacity=1, cost=1, stage=0, key=0):
    fi = self.get_node_index(fro, stage)
    ti = self.get_node_index(to, stage + 1)

    ai = self.ortool_graph.AddArcWithCapacityAndUnitCost(fi, ti, capacity, cost)

  def _add_or_set_arc(self, fro, to, capacity=1, cost=1, stage=0, key=0):
    fi = self.get_node_index(fro, stage)
    ti = self.get_node_index(to, stage + 1)

    ai = self.ortool_graph.AddArcWithCapacityAndUnitCost(fi, ti, capacity, cost)
    edges = self.adj.setdefault(fi, dict())
    edges.setdefault(ti, {})[key] = ai

  def add_or_set_arc_old(self, fro, to, capacity=1, cost=1, stage=0, key=0):
    fi = self.get_node_index(fro, stage)
    ti = self.get_node_index(to, stage + 1)

    # Get fi if exists if not create a new dict for that key and return it
    edges = self.adj.setdefault(fi, dict())
    # extra layer of keys for multigraph support (multiple edges btw same 2 nodes)
    edges.setdefault(ti, {})[key] = (capacity, cost)

  def has_arc(self, u, v, key):
    try:
      if key in None:
        return v in self.adj[u]
      else:
        return key in self.adj[u][v]
    except KeyError:
      return False

  def remove_arc(self, u, v, key):
    try:
      if key is None:
        # delete everything
        del self.adj[u][v]
      else:
        del self.adj[u][v][key]
        # if key dict empty, delete it
        if len(self.adj[u][v]) == 0:
          del self.adj[u][v]

    except KeyError:
      raise Exception("The edge %s-%s-%s is not in the graph" % (u, v, key))


  def get_arc(self, fro, to, key=0):
    if fro in self.adj and to in self.adj[fro]:
      ai = self.adj[fro][to][key]

      g = self.ortool_graph

      return (g.Capcity(ai), g.UnitCost(ai))
    else:
      return None

  def get_arc_old(self, fro, to):
    if fro in self.adj and to in self.adj[fro]:
      return self.adj[fro][to]
    else:
      return None

  def print_arcs(self):
    for fro in self.adj:
      for to in self.adj[fro]:
        for key in self.adj[fro][to]:
          capacity, cost = self.adj[fro][to][key]
          print 'Edge %s -> %s : %d, %d' % (str(fro), str(to), capacity, cost)

  def print_stages(self):
    stages = self.stages.keys()
    stages.sort()

    ns = []

    for i in stages:
      st = self.stages[i]
      print 'stage %d : %s' % (i, str(st))

  # Compile into a ORTOOLS graph for faster calculations in C
  def compile(self):
    if self.total_flow <= 0:
      raise Exception('You forgot to set a positive total flow!')

    min_cost_flow = self.ortool_graph

    # Set flow for source/sink. Get first and last stage as source/sink
    st = self.stages
    ks = st.keys()
    ks.sort()
    (source, ) = st[ks[0]]
    (sink, ) = st[ks[-1]]
    source, sink = self.nodes[source], self.nodes[sink]
    print 'source/sink/flow', source, sink, self.total_flow
    min_cost_flow.SetNodeSupply(source, self.total_flow)
    min_cost_flow.SetNodeSupply(sink, -self.total_flow)

    return min_cost_flow

  def print_solution(self, debug=False):
    self.soln = []

    g = self.ortool_graph

    if self.status == g.OPTIMAL:
      print 'Total flow cost', g.OptimalCost()
      print 'Total max flow', g.MaximumFlow()
      print 'Total # of nodes', g.NumNodes()
      print 'Total # of edges', g.NumArcs()
      for i in range(0, g.NumArcs()):
        if g.Flow(i) > 0:
          self.soln.append([g.Tail(i), g.Head(i)])
          # print 'From source %d to target %d: cost %d' % (
          #     g.Tail(i),
          #     g.Head(i),
          #     g.UnitCost(i))
      if debug:
        self.graph()
    else:
      print 'There was an issue with the min cost flow input.', self.status, self.STATUS[self.status]


  # Converts from soln indices to soln node obj pairings
  def solution_to_node(self, start_stage=1, end_stage=-1):
    if end_stage == -1:
      # get the second to last stage
      end_stage = len(self.stages) - 2

    # [(fro_node, to_node)]
    self.soln_nodes = []

    # {fro_i : Set([to_i,])}
    soln_lookup = {}

    g = self.ortool_graph

    if self.status == g.OPTIMAL:
      # calculate reverse lookup for nodes
      nodes = self.nodes.keys()
      print 'Total flow cost', g.OptimalCost()
      print 'Total max flow', g.MaximumFlow()
      print 'Total # of nodes', g.NumNodes()
      print 'Total # of edges', g.NumArcs()
      for i in range(0, g.NumArcs()):
        if g.Flow(i) > 0:
          fro, to = g.Tail(i), g.Head(i)
          soln_lookup.setdefault(fro, Set()).add(to)
          # soln_lookup[fro] = to
          # print 'From source %d to target %d: cost %d' % (
          #     g.Tail(i),
          #     g.Head(i),
          #     g.UnitCost(i))

      start_s = self.get_stage(start_stage)
      end_s = self.get_stage(end_stage)

      print 'soln_lookup', soln_lookup, start_s, end_s

      for s_node in start_s:
        n1 = self.get_node_index(s_node)
        if n1 not in soln_lookup:
          print 'No solution found for %d in soln_lookup' % n1
        else:
          # trace the to's all the way to end_stage nodes
          for to in soln_lookup[n1]:
            nxts = Set([to,])
          
            while len(nxts) > 0:
              n2 = nxts.pop()
              if nodes[n2] in end_s:
                # save solution mapping from start_stage to end_stage
                self.soln_nodes.append((nodes[n1], nodes[n2]))
              else:
                # keep going down the rabbit hole
                if n2 in soln_lookup:
                  nxts.union_update(soln_lookup[n2])

        
    return (self.STATUS[self.status], self.soln_nodes)


  # Solve with max partial flow allowed in graph
  def solve_partial_flow(self, debug=False):
    self.compile()
    self.status = self.ortool_graph.SolveMaxFlowWithMinCost()

    print 'solving partial...'

    self.print_solution(debug)

    return self.solution_to_node()

  # solve graph for Full flow: compile() first and then .solve()
  def solve(self, debug=False):
    self.compile()

    print 'solving...'

    self.status = self.ortool_graph.Solve()

    self.print_solution(debug)

    return self.solution_to_node()

  
  def graph(self):
    filename = '/home/rayli/Desktop/data.js'
    f = open(filename,'w')
    # print >>f, 'whatever'

    ########### js stuff!

    g = self.ortool_graph

    js_edges = []

    if self.minimal_features:
      # need to get arcs from ortools
      for i in range(g.NumArcs()):
        js_edges.append({'source': g.Tail(i), 'target': g.Head(i), 'weight': int(g.UnitCost(i))})


    constraints = []
    # loop through all the stages in order and create column constraints for each
    stages = self.stages.keys()
    stages.sort()

    ns = []

    max_stage_length = 0

    for i in stages:
      st = self.stages[i]
      if len(st) > max_stage_length:
        max_stage_length = len(st)

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
var st_ns = %s;
var ns = [];
var n_tot = %d;
var scaling = 40;
var X_OFFSET = 200;
var MARGIN = 100;
var max_stage_length = %d;

// source/sink
//ns.push({id: 0, fixed: true, x: 100, y: services * scaling});
//ns.push({id: n_tot - 1, fixed: true, x: 500, y: services * scaling});

for (var i in st_ns) {
  // In stage i nodes
  var ns_i = st_ns[i];
  var Y_OFFSET = (max_stage_length - ns_i.length) / 2;
  for (var j in ns_i) {
    var n = ns_i[j];
    ns.push({id: n, fixed: true, x: MARGIN + i * X_OFFSET, y: MARGIN + (Y_OFFSET + parseInt(j)) * scaling});
  }
}
''' % (str(ns), self.ortool_graph.NumNodes(), max_stage_length)

    f.write(code)
    # print >>f code
    f.write('constraints = ' + str(constraints) + '\n')
    f.write('lks = ' + str(js_edges) + '\n')
    f.write('solns = ' + str(self.soln) + '\n')
 

# Test stuff
# @profile
def serviceMinCostFlow():

  # Don't make services same as trainees!
  services = 10
  trainees = 5
  s_t_ratio = services / (trainees - 1)
  # number of services per trainee
  t_s_max_capacity = 4
  expected_cost = 275

  # service/trainee labels
  s_l = 'service_'
  t_l = 'trainee_'

  ss_edges = [] # Source to service
  st_edges = [] # Service to Trainee
  tt_edges = [] # Trainee to sink t

  pos = {}
  s_nodes = []
  t_nodes = []


  pos['s'] = [0, services / 2]

  # Edge Count
  e_count = 0

  # G = nx.DiGraph()
  # # source
  # G.add_node('s', demand = -services)
  # # sink node
  # G.add_node('t', demand = services)


  '''
    ArcIndex AddArcWithCapacityAndUnitCost(NodeIndex tail, NodeIndex head,
                                           FlowQuantity capacity,
                                           CostValue unit_cost);
  '''

  node_count = 0;

  min_cost_flow = DirectedFlowGraph()

  # Add services to source
  for i in range(services):
    node_count += 1
    (fro, to) = (0, node_count)
    ss_edges.append((fro, to, 1))
    pos[to] = [1, i]
    s_nodes.append(to)
    min_cost_flow.add_or_set_arc(fro, to, 1, 1, 0)
    # G.add_edge(fro, to, weight = 1, capacity = 1, edge_color='g')
    e_count+=1

  # Add trainees to services
  for i in range(trainees):
    node_count += 1 
    for j in range(1, services + 1):
      # flip a coin to determine to link the trainee to services or not. 3/4 change of linkage
      if random.random() <= 0.75:
        (fro, to) = (j, node_count)
        cost = random.randint(1, 10)
        st_edges.append((fro, to, cost))
        min_cost_flow.add_or_set_arc(fro, to, 1, cost, 1)
        # G.add_edge(fro, to, weight = random.randint(1, 10), capacity = 1, edge_color='r')
        e_count+=1

  print 'node_count, sink', node_count + 1
  # add trainees all to sink t
  for j in range(trainees):
    (fro, to) = (node_count - j, node_count + 1)
    pos[fro] = [2, s_t_ratio * j]
    t_nodes.append(fro)
    num_services = random.randint(1, 3)
    sick_lvl = random.randint(1, 10)
    for x in range(1, t_s_max_capacity + 1):
      tt_edges.append((fro, to, x * sick_lvl))
      min_cost_flow.add_or_set_arc(fro, to, 1, x * sick_lvl, 2, x)
    # G.add_edge(fro, to, weight = random.randint(1, 3), capacity = t_s_max_capacity, edge_color='b')
    e_count+=1

  # min_cost_flow.SetNodeSupply(0, services)
  # min_cost_flow.SetNodeSupply(node_count + 1, -services)

  min_cost_flow.set_total_flow(services)

  # print 'edges', min_cost_flow.adj

  # min_cost_flow.print_arcs()

  # min_cost_flow.print_stages()

  min_cost_flow.solve(debug=True)






# serviceMinCostFlow()
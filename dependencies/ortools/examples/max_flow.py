# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""From Taha 'Introduction to Operations Research', example 6.4-2."""

from google.apputils import app
from ortools.graph import pywrapgraph

def MaxFlow():
  """MaxFlow simple interface example."""

  # Define three parallel arrays: sources, destinations, and the capacities
  # between each pair. For instance, the arc from node 0 to node 1 has a
  # capacity of 20.

  sources = [0, 0, 0, 1, 1, 2, 2, 3, 3]
  destinations = [1, 2, 3, 2, 4, 3, 4, 2, 4]
  capacities = [20, 30, 10, 40, 30, 10, 20, 5, 20]

  # Instantiate a SimpleMaxFlow solver.
  max_flow = pywrapgraph.SimpleMaxFlow()

  # Add each arc.
  for i in range(0, len(sources)):
    max_flow.AddArcWithCapacity(sources[i], destinations[i], capacities[i])

  # Find the maximum flow between node 0 and node 4.
  if max_flow.Solve(0, 4) == max_flow.OPTIMAL:
    print 'Max flow:', max_flow.OptimalFlow()
    for i in range(max_flow.NumArcs()):
      print 'From source %d to target %d: %d / %d' % (
          max_flow.Tail(i),
          max_flow.Head(i),
          max_flow.Flow(i),
          max_flow.Capacity(i))
    print 'Source side min-cut:', max_flow.GetSourceSideMinCut()
    print 'Sink side min-cut:', max_flow.GetSinkSideMinCut()
  else:
    print 'There was an issue with the max flow input.'
    
def main(unused_argv):
  MaxFlow()

if __name__ == '__main__':
  app.run()

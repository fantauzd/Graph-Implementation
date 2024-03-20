"""
Depth-first search the shortest distance algorithm:

To find the set of vertices reachable from an initial vertex vs
Create and Initialize set of reachable vertices
Add vs to a stack
While stack is not empty
    Get and remove (pop) last vertex v from stack
    If v is known to be reachable, discard
    Otherwise, add v to set of reachable vertices, then
        For all neighbors, vj, of v
        If vj is not is set of reachable vertices, add to stack
"""


"""
Dijkstra’s Shortest Path Algorithm (Weighted Breadth-first:

The complexity of this version of the algorithm is O(|E| log |E|). 
The innermost loop is executed at most |E| times, and the cost of the instructions inside the loop is O(log |E|).

To find the shortest distance to vertices reachable from an initial vertex vs
Initialize dictionary of reachable vertices with vs having cost zero,
and add vs to a priority queue with distance zero
While priority queue is not empty
    Get and remove (pop) vertex v with shortest distance from priority queue
    If v is known to be reachable, discard
    Otherwise, add v with given cost to dictionary of reachable vertices
        For all neighbors, vj, of v
        If vj is not is set of reachable vertices, combine cost of reaching v
        with cost to travel from v to vj, and add to priority queue 
"""


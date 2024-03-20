"""
Graph Pseudocode
"""

"""
Depth-first search:

O(V) space complexity in the worst case.

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
Breadth-first search:

O(V) space complexity in the worst case.

Initialize an empty set of visited vertices.
Initialize an empty queue (BFS). Add vi to the queue.
While the queue is not empty, 
    dequeue a vertex v.
    If v is in visited vertices, discard
    Otherwise, Add v to the set of visited vertices.
        For each direct successor v’ of v:
        If v’ is not in the set of visited vertices, enqueue it into the queue
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
        
        
Initialize an empty map/hash table representing visited vertices.
    Key is the vertex v.
    Value is the min distance d to vertex v.
Initialize an empty priority queue, and insert vs into it with distance (priority) 0.
While the priority queue is not empty:
    Remove the first element (a vertex) from the priority queue and assign it to v. Let d be v’s distance (priority).
    If v is not in the map of visited vertices:
        Add v to the visited map with distance/cost d.
        For each direct successor vi of v:
            Let di equal the cost/distance associated with edge (v, vi).
            Insert vi to the priority queue with distance (priority) d + di.
"""


"""
Space Complexity of Graph representations:
Adjacency list: O(|V| + |E|)
Adjacency matrix: O(|V|2)
"""
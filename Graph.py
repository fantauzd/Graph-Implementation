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
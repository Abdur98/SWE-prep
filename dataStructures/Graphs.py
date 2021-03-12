# can solve several imp problems if represented as a DAG (directed + acyclic)
# adjacency matrix good if large # of edges but sparse matrix otherwise so use adjacency list to be more space-efficient
# adjacency list -> adjaceny dicts (key = connected vertex and value = weight)

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    # def __str__(self):
    #     return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


g = Graph()
for i in range(6):
    g.addVertex(i)

g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)

for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))

# BFS
# finds all vertices k edges before BEFORE finding any which are k+1 edges away
# O(V+E)

def BFS(g, start):
    dist = {}
    preds = {}
    visited = set()
    Q = []

    visited.add(start)
    Q.append(start)
    while Q:
        curr = Q.pop(0)
        print(curr.id, end = " ?? ")

        for nbr in curr.getConnections():
            if nbr not in visited:
                visited.add(nbr)
                Q.append(nbr)

print('BFS=')
BFS(g, g.vertList[0])

# parenthesis property. This property means that all the children of a particular node in the depth first tree have a later discovery time and an earlier finish time than their parent.


print('', 'DFS=')
def DFS(g, start, visited=set()):
    if start not in visited:
        print(start.id, end=" || ")
        visited.add(start)
        for nbr in start.getConnections():
            DFS(g, nbr, visited)

DFS(g, g.vertList[0])

# # sorting by least # of nbrs available
# key to reducing runtime of Knight's Tour problem
# def orderByAvail(n):
#     resList = []
#     for v in n.getConnections():
#         if v.getColor() == 'white':
#             c = 0
#             for w in v.getConnections():
#                 if w.getColor() == 'white':
#                     c = c + 1
#             resList.append((c,v))
#     resList.sort(key=lambda x: x[0])
#     return [y[1] for y in resList]




# TopSort
# A topological sort takes a directed acyclic graph and produces a linear ordering of all its vertices such that if the graph G contains an edge
# (𝑣,𝑤), then the vertex 𝑣 comes before the vertex 𝑤 in the ordering.

# Algorithm
# Call dfs(g) for some graph g. The main reason we want to call depth first search is to compute the finish times for each of the vertices. (paranthesis property: all child have later discovery and earlier finish)
# Store the vertices in a list in decreasing order of finish time.
# Return the ordered list as the result of the topological sort.


def recursive_dfs(graph, node):
    result = []
    seen = set()

    def recursive_helper(node):
        for neighbor in graph[node]:
            if neighbor not in seen:
                result.append(neighbor)     # this line will be replaced below
                seen.add(neighbor)
                recursive_helper(neighbor)

    recursive_helper(node)
    return result

def recursive_topological_sort(graph, node):
    result = []
    seen = set()

    def recursive_helper(node):
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                recursive_helper(neighbor)
        result.insert(0, node)              # this line replaces the result.append line

    recursive_helper(node)
    return result

    We can now describe the algorithm to compute the strongly connected components for a graph.

# Strongly connected components (SCC)
# Call dfs for the graph 𝐺 to compute the finish times for each vertex.
# Compute 𝐺^t (i.e. if G has path (u, v), G^t has path (v, u))
# Call dfs for the graph 𝐺^t but in the main loop of DFS explore each vertex in decreasing order of finish time.
# Each tree in the forest computed in step 3 is a strongly connected component. Output the vertex ids for each vertex in each tree in the forest to identify the component.

# Dijkstra's algorithm (O(V)log(v) for constructing heap & O(E)Log(V) for runtime so O((E+V)log(v))) overall
# BFS for shortest path but with weighted edges
# only works when weights all +ve

# def dijkstra(aGraph,start):
#     pq = PriorityQueue()
#     start.setDistance(0)
#     pq.buildHeap([(v.getDistance(),v) for v in aGraph])
#     while not pq.isEmpty():
#         currentVert = pq.delMin()
#         for nextVert in currentVert.getConnections():
#             newDist = currentVert.getDistance() \
#                     + currentVert.getWeight(nextVert)
#             if newDist < nextVert.getDistance():
#                 nextVert.setDistance( newDist )
#                 nextVert.setPred(currentVert)
#                 pq.decreaseKey(nextVert,newDist)

# Bellman Ford (O(V * E))
# Can handle negative weights
# cannot handle negative weight cycles

# function BellmanFord(list vertices, list edges, vertex source) is

#     // This implementation takes in a graph, represented as
#     // lists of vertices (represented as integers [0..n-1]) and edges,
#     // and fills two arrays (distance and predecessor) holding
#     // the shortest path from the source to each vertex

#     distance := list of size n
#     predecessor := list of size n

#     // Step 1: initialize graph
#     for each vertex v in vertices do
#         distance[v] := inf             // Initialize the distance to all vertices to infinity
#         predecessor[v] := null         // And having a null predecessor

#     distance[source] := 0              // The distance from the source to itself is, of course, zero

#     // Step 2: relax edges repeatedly
#     repeat |V|−1 times:
#         for each edge (u, v) with weight w in edges do
#             if distance[u] + w < distance[v] then
#                 distance[v] := distance[u] + w
#                 predecessor[v] := u

#     // Step 3: check for negative-weight cycles
#     for each edge (u, v) with weight w in edges do
#         if distance[u] + w < distance[v] then
#             error "Graph contains a negative-weight cycle"

# #     return distance, predecessor


# Spanning Trees
# Prim's
# While T is not yet a spanning tree
#    Find an edge that is safe to add to the tree
#    Add the new edge to T


# def prim(G,start):
#     pq = PriorityQueue()
#     for v in G:
#         v.setDistance(sys.maxsize)
#         v.setPred(None)
#     start.setDistance(0)
#     pq.buildHeap([(v.getDistance(),v) for v in G]) O(n * log(n))
#     while not pq.isEmpty(): O(n * log(n))
#         currentVert = pq.delMin()
#         for nextVert in currentVert.getConnections():
#           newCost = currentVert.getWeight(nextVert)
#           if nextVert in pq and newCost<nextVert.getDistance():
#               nextVert.setPred(currentVert)
#               nextVert.setDistance(newCost)
#               pq.decreaseKey(nextVert,newCost)


















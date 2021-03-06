#Chapter 4.1


#4.1.1

answer = "The maximum number of edges can be found in a graph with V vertices is (V * V)/2 graph. The minimum number" \
         "of edges would be a star structure of V-1 edges"

#4.1.2

adjacency_list = {
    12: 16,
    8: [2, 4, 0],
    1:[0,1],
    3: 10,
    7: 7,
    11: [2,6, 8],
    6: [3,5],
    5: 5,
    4:3,
    2:2,
    10: 0

}



#4.1.3

class Graph:
    def __init__(self, graph):
        self.V = graph.V
        self.adj = list()
        for index, adj in  enumerate(graph.adj):
            self.adj[index] = adj

    def hasEdge(self, v, w):
        for edge in self.adj[v]:
            if edge == w:
                return True

        return False


#4.1.4 See Graph class above

#4.1.5 TBC

#4.1.6

adjacency_list = {
    0: [1, 2, 3],
    1: [0, 2],
    3: [0],
    2: [1]
}

#4.1.8

class Search:
    """find verices connected to a source vertex"""
    def __init__(self, graph, source):
        self.V = graph.V
        self.adj = list()
        for index, adj in  enumerate(graph.adj):
            self.adj[index] = adj
        self.source = source

    def find(self,s):
        print("Source vertex:", s)
        for w in self.adj[s]:
              self.find[w]

#4.1.10

answer = "A vertex with adjacent vertices who are all marked, indicates the graph is connected and removing this vertex" \
         "will have no impact on its connctivity."

class DFS_Connected_Vertex_Finder:
    def __init__(self, source=0):
        self.marked = list()
        self.edgeTo = list()
        self.source = source


    def dfs(self, graph, v):
        self.marked[v] = True;
        self.marked_bool = True
        for w in graph.adj[v]:
            if self.marked[w] is None:
                self.edgeTo[w] = v
                self.dfs(graph, w)
                self.marked_bool = False

        if self.marked_bool == True:
            """a vertext where all adjacent vertices are marked"""
            return v

#4.1.12

answer = "One cannot calculate the distance between two nodes at least one of them is not the root."

#4.1.13


class BFS_DistanceTo:
    def __init__(self, G, source=0):
        self.marked = [None]*G.V()
        self.edgeTo = [None]*G.V()
        self.distTo = [None] * G.V()
        self.source = source

    def bfs(self, G, s):
        queue = list()
        self.marked[s] = True
        self.edgeTo[s] = s
        queue.append(s)

        while len(queue)>0:
            vertex = queue.pop(0)
            count = 0
            while True:
                previous = self.edgeTo[vertex]
                count += 1
                if previous == s:
                    break;
            self.distTo[vertex] = count
            for w in G.adj(vertex):
                if self.marked[w] == None:
                    self.edgeTo[w] = vertex
                    self.marked[w] = True
                    queue.append(w)

    def retrieve_distTo(self, v):
        return self.distTo[v]



    def eccentricity_constructor(self,s, G, diameter, radius):
        max_eccentricities = [None] * G.V()

        self.bfs(G, s)

        self.all_vertices = self.marked[:]

        max_eccentricities[s] = max(self.distTo)

        for vertex in self.all_vertices:
            self.distTo = [None] * G.V()
            self.bfs(G, vertex)
            max_eccentricities[vertex] = max(self.distTo)

        if diameter:
            return max(max_eccentricities)
        elif radius:
            return min(max_eccentricities)
        else:
            self.center = max_eccentricities.index(min(max_eccentricities))

    def diameter(self,s, G):
        return self.eccentricity_constructor(self, s, G, True)

    def radius(self,s, G):
        return self.eccentricity_constructor(self, s, G, False, True)

    def center(self, s, G):
        return self.eccentricity_constructor(self, s, G, False, False)

    def wiener_index(self, s, G):

        shortest_paths = list()
        self.weiner_marked = [None] * G.V()
        self.all_vertices = self.marked.copy()

        self.bfs(G, s)
        
        for vertex in self.all_vertices:
            self.distTo = [None] * G.V()
            self.bfs(G, vertex)
            self.weiner_marked[vertex] = True

            for index, distance in enumerate(self.distTo):
                if self.weiner_marked[index] == None:
                    shortest_paths.append(distance)

        return sum(shortest_paths)


#4.1.14

answer = "No, the result would be a DFS"

#4.1.16  See 4.1.13


#4.1.17 See 4.1.13

#4.1.20 See PDF.

answer = "Runtime is proportional to the length of the cycle"


#4.1.26

class SymbolGraph:
    def __init__(self):
        self.keys_to_ints = dict()
        self.ints_to_keys = list()

class DegreesOfSeparation:
    def __init__(self, G):
        self.dfs = DepthFirstSearch(G)
        self.G = G

    def degrees_of_separation(self, sink):
        vertex = self.G.indexOf(sink)
        if (self.dfs.hasPathTo(vertex)):
            for w in self.dfs.pathTo(vertex):
                print("movie/performer", self.G.nameOf(w))


#4.1.27

answer = "Just considering the E edges represented by a bag of linked lists, the memory used is proportional to 32 + 64 E. The array" \
         "and the linked lists combined use to hold the hold the edges us ~ 8 E * V bytes"


#4.1.28 See PDF.
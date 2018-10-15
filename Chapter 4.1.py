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


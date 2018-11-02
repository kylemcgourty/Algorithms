#Chapter 4.4

#4.4.1

answer = "False. Adding a negative constant may create a negative cycle."

#4.4.2

import fileinput


class DirectedEdge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def returnWeight(self):
        return self.weight

    def fromVertex(self):
        return self.v
    def toVertex(self):
        return self.w



class EdgeWeightedDiagraph:
    def __init__(self, V):
        """From graph"""
        self.V = V
        self.E = 0
        self.adjacency_list = [[] for i in range(V+1)]
        """From std in"""
        # for line in fileinput.input():
        #     edge =line.split(" ")
        #     directedEdge = DirectedEdge(edge[0], edge[1], edge[2])
        #     self.addEdge(directedEdge)

    def addEdge(self, edge):
        self.adjacency_list[edge.fromVertex()].append(edge)
        self.E +=1
    def toString(self):
        for vertex in self.adjacency_list:
            for edge in vertex:
                print(edge.fromVertx(), "->", edge.toVertex(), "weight:", edge.weight())


#4.4.3 See 4.4.2

#4.4.4 See 4.4.4.pdf

note = "Difference between MST, PST - Prims and Dijkstra's: The main difference is the value chosen to be minimal. " \
       "For Dijkstra it is the length of the complete path from start node to the candidate node, for Prim it is" \
       " just the weight of that single edge."

#4.4.6
"""
                    pq
                     0
   edgeTo   DistTo  pq
    0-4     .38     .38
   edgeTo   DistTo  pq
    0-4     .38     .73
    4-5     .73
    edgeTo   DistTo  pq
    0-4     .38     .73
    4-5     .73
    edgeTo   DistTo  pq
    0-4     .38     1.05
    4-5     .73
    5-1      1.05
    edgeTo   DistTo  pq
    0-4     .38     1.05
    4-5     .73
    5-1      1.05
    edgeTo   DistTo  pq
    0-4     .38     1.34
    4-5     .73
    5-1      1.05
    1-3      1.34  
    edgeTo   DistTo  pq
    0-4     .38     1.86
    4-5     .73
    5-1      1.05
    1-3      1.34  
    3-6      1.86 
    edgeTo   DistTo  pq
    0-4     .38     2.26
    4-5     .73
    5-1      1.05
    1-3      1.34  
    3-6      1.86 
    6-2      2.26   
"""


#4.4.7
import math

class IndexMinPQ:
    def __init__(self):
        self.keys = [None]*1000
        self.pq = [0] * 1000
        self.qp = [-1] * 1000
        self.n = 0

    def insert(self, i, key):
        self.n += 1
        self.qp[i] = self.n
        self.pq[self.n] = i
        self.keys[i] = key
        self.swim(self.n)


    def swim(self, k,):

        while k > 1 and self.less(k//2, k):
            self.exchange(k//2, k)
            k = k//2


    def sink(self, k):
        while 2*k <= self.n:
            j = 2*k
            if j < self.n and self.less(j, j+1):
                j+=1
            if self.less(k, j) == False:
                break
            self.exchange(k, j)
            k = j


    def less(self, k , j):
        if self.keys[self.pq[j]] < self.keys[self.pq[k]]:
            return True
        elif self.keys[self.pq[j]] > self.keys[self.pq[k]]:
            return False
        else:
            return False

    def exchange(self, k, j):
        #update qp
        temp1 = self.qp[self.pq[k]]
        self.qp[self.pq[k]] = self.qp[self.pq[j]]
        self.qp[self.pq[j]] = temp1

        #update pq
        temp = self.pq[k]
        self.pq[k] = self.pq[j]
        self.pq[j] = temp




    def delMin(self):
        minimum_key = self.pq[1]
        self.exchange(1, self.n)
        self.n -= 1
        self.sink(1)
        self.keys[self.pq[self.n+1]] = None
        self.qp[self.pq[self.n+1]] = -1
        return minimum_key

    def isEmpty(self):
        return self.n == 0

    def contains(self, w):
        return self.keys[w] != None

    def changeKey(self, v, key):
            self.keys[v] = key
            self.swim(self.qp[v])


class Dijkstras_Shortest_Path:
    def __init__(self, V, G, src):
        self.edgeTo = [None] * V
        self.distTo = [math.inf] * V
        self.pq = IndexMinPQ()
        self.G = G

        self.distTo[src] = 0
        self.pq.insert(src, 0.0)

        while(self.pq.isEmpty() == False):
            self.relax(self.pq.delMin())

        for edge in self.edgeTo:
            if edge is not None:
                print(edge.fromVertex(), "->", edge.toVertex(), " ", edge.returnWeight())

    def relax(self, vertex):
        for edge in self.G.adjacency_list[vertex]:
            w = edge.toVertex()
            print("The v, dist values and edge weight", vertex, self.distTo[vertex], edge.returnWeight())
            if self.distTo[w] > self.distTo[vertex] + edge.returnWeight():
                self.distTo[w] = self.distTo[vertex] + edge.returnWeight()
                self.edgeTo[w] = edge
                if (self.pq.contains(w)):
                    self.pq.changeKey(w, self.distTo[w])
                else:
                    self.pq.insert(w, self.distTo[w])


graph = EdgeWeightedDiagraph(6)
graph.addEdge(DirectedEdge(0,4, .38))
graph.addEdge(DirectedEdge(4,5, .35))
graph.addEdge(DirectedEdge(5,4, .35))
graph.addEdge(DirectedEdge(5,1, .32))
graph.addEdge(DirectedEdge(1,3, .29))
graph.addEdge(DirectedEdge(3,6, .52))
graph.addEdge(DirectedEdge(6,2, .4))
graph.addEdge(DirectedEdge(0,2, .26))
graph.addEdge(DirectedEdge(6,0, .58))
graph.addEdge(DirectedEdge(6,4, .93))

Dijkstras_Shortest_Path(7, graph, 0)
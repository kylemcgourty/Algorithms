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
        self.adjacency_list = [[] for i in range(V)]
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


# graph = EdgeWeightedDiagraph(6)
# graph.addEdge(DirectedEdge(0,4, .38))
# graph.addEdge(DirectedEdge(4,5, .35))
# graph.addEdge(DirectedEdge(5,4, .35))
# graph.addEdge(DirectedEdge(5,1, .32))
# graph.addEdge(DirectedEdge(1,3, .29))
# graph.addEdge(DirectedEdge(3,6, .52))
# graph.addEdge(DirectedEdge(6,2, .4))
# graph.addEdge(DirectedEdge(0,2, .26))
# graph.addEdge(DirectedEdge(6,0, .58))
# graph.addEdge(DirectedEdge(6,4, .93))

# Dijkstras_Shortest_Path(7, graph, 0)


#4.4.8

answer = 'The diameter is defined to be the maximum length shortest path. In other words, it is the shortest path that ' \
         'visits the most vertices.'


class Dijkstras_Shortest_Path_Diameter:
    def __init__(self, V, G, src):
        self.edgeTo = [None] * V
        self.distTo = [math.inf] * V
        self.pq = IndexMinPQ()
        self.G = G
        self.verticesTo = [0]* V

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

                self.verticesTo[w] = self.verticesTo[vertex] + 1
                if (self.pq.contains(w)):
                    self.pq.changeKey(w, self.distTo[w])
                else:
                    self.pq.insert(w, self.distTo[w])




#4.4.10

answer = "The graph to be considered is the graph tinyEWD.text but with all edges bidirectional."

"""
edgeTo   distTo   pq
0-2       .26     .26
0-4       .38     .38
edgeTo   distTo   pq
2-0       .26       .52
2-7       .34      .60
0-4       .38      .38
edgeTo   distTo   pq
2-0       .26       .52
2-7       .34       .60
4-0       .76       .76
4-7       .75       .75
4-5       .73       .73
edgeTo   distTo   pq
***here, the graph retraces back along 2-0***
0-2       .78       .78
0-4       .9         .9
2-7       .34       .60
4-0       .76       .76
4-7       .75       .75
4-5       .73       .73
edgeTo   distTo   pq
0-2       .78       .78
0-4       .9         .9
4-0       .76       .76
4-7       .75       .75
4-5       .73       .73
7-3       .99       .99
7-5       .88       .88
7-2       .94       .94
edgeTo   distTo   pq
0-2       .78       .78
0-4       .9         .9
4-0       .76       .76
4-7       .75       .75
4-5       .73       .73
5-1      1.05      1.05
5-7      1.01      1.01
5-4      1.08      1.08
7-3       .99       .99
7-5       .88       .88
7-2       .94       .94

"""

#4.4.11

answer = "An edge-weighted graph with an adjaceny list implementation is similar to a two-dimesional array of objects." \
         "The bytes used can be approximated by 8*V*(E/V) + 32 V + 23 + 28 * E"


#4.4.12

class EdgeWeightedDirectedCycle:
    def __init__(self, G, V):

        self.onStack = [False] * V
        self.edgeTo = [None] * V
        self.marked = [False] * V
        self.cycle = list()

        for vertex in range(V):
            if self.marked[vertex] is False:
                self.cycle_detector_dfs(G, vertex)

        for v in self.cycle:
            print("the cycle:", v)

    def cycle_detector_dfs(self, G, v):
        self.onStack[v] = True
        self.marked[v] = True

        for unit in G.adjacency_list:
            for edge in unit:
                print(edge.fromVertex(), "->", edge.toVertex(), ":", edge.returnWeight())
        for w in G.adjacency_list[v]:
            w = w.toVertex()
            if self.hasCycle():
                return
            elif self.marked[w] == False:

                self.edgeTo[w] = v
                self.cycle_detector_dfs(G, w)
            elif self.onStack[w]:
                x = v
                while x != w:
                    self.cycle.append(x)
                    x = self.edgeTo[x]
                self.cycle.append(w)
                self.cycle.append(v)

        self.onStack[v] = False


    def hasCycle(self):
        return len(self.cycle) > 0


# graph = EdgeWeightedDiagraph(6)
# graph.addEdge(DirectedEdge(0,4, .38))
# graph.addEdge(DirectedEdge(4,5, .35))
# # graph.addEdge(DirectedEdge(5,4, .35))
# graph.addEdge(DirectedEdge(5,1, .32))
# graph.addEdge(DirectedEdge(1,3, .29))
# graph.addEdge(DirectedEdge(3,6, .52))
# graph.addEdge(DirectedEdge(6,2, .4))
# graph.addEdge(DirectedEdge(0,2, .26))
# graph.addEdge(DirectedEdge(6,0, .58))
# graph.addEdge(DirectedEdge(6,4, .93))
#
# detect_cycle = EdgeWeightedDirectedCycle(graph, 7)


class Topological:
    def __init__(self, graph, V):
        self.order = list()
        detect_cycle = EdgeWeightedDirectedCycle(graph, V+1)
        if detect_cycle.hasCycle() == False:
            print("in if being called")
            dfs = DepthFirstOrder(graph, V+1)
            self.order = dfs.reversePost

        # for v in reversed(self.order):
            # print("The topolocial order", v)

class DepthFirstOrder:
    def __init__(self, graph, V):
        self.pre = list()
        self.post = list()
        self.reversePost = list()
        self.marked = [False] * V


        for vertex in range(V):
            if self.marked[vertex] is False:
                self.dfs(graph, vertex)


    def dfs(self, G, v):

        self.pre.append(v)
        self.marked[v] = True
        for w in G.adjacency_list[v]:
            w = w.toVertex()
            if self.marked[w] == False:
                self.dfs(G, w)

        self.post.append(v)
        self.reversePost.append(v)

# graph = EdgeWeightedDiagraph(7)
# graph.addEdge(DirectedEdge(0,4, .38))
# graph.addEdge(DirectedEdge(4,5, .35))
# graph.addEdge(DirectedEdge(5,1, .32))
# graph.addEdge(DirectedEdge(5,7,.77))
# graph.addEdge(DirectedEdge(3,6, .52))
# graph.addEdge(DirectedEdge(6,2, .4))
# graph.addEdge(DirectedEdge(1,3, .29))
#
# detect_cycle = Topological(graph, 8)


#4.4.14

answer = "The first strawman is to take the absolute value of a negative edge and add it to all the other edges." \
         "The approach is inappropriate because some paths are not necessarily affected by the negative edge. Thus," \
         "the values of their paths will be unnecessarily inflated." \
         "The second strawman is to use Dijkstra's algorithm in some way. Again, this method does not work as Dijkstra's" \
         "algorithm is predicted on the on edges getting longer."


#4.4.15

answer = "With a negative cycle, calling pathTo would begin an infinite loop."

#4.4.16

answer = "Creating an edge-weighted digraph from an edge-weighted graph, using directed edges that run in both directions" \
         "would be infeasible for the Bellman-Ford algorithm. Take an edge that has a negative weight: it would be a negative" \
         "cycle between its two vertices, causing the algorithm to quit."

#4.4.17

answer = "If vertices were added to a queue more than once, they would be relaxed more than once. This would lead to" \
         "unnecessary processing. In the case of negative weights, the running time could be exponential."

#4.4.18


class CriticalPathMethod:
    def __init__(self, V, duration_list):
        graph = EdgeWeightedDiagraph(2*V+2)
        s = 2*V
        t = 2*V+1
        for i in range(V):
            graph.addEdge(DirectedEdge(i, i+V, -duration_list[i][0]))
            graph.addEdge(DirectedEdge(s, i, 0))
            graph.addEdge(DirectedEdge(i+V, t, 0))
            if len(duration_list[i])>1:
                for j in duration_list[i][1]:
                    print("in dur li", duration_list[i], i)
                    graph.addEdge(DirectedEdge(i+V, j, 0.0))

        AcyclicLP = AcyclicSP(graph, 2*V+1, s)

        for k in range(V):
            print("start times:", k, ":", -AcyclicLP.distTo[k])
        print("finish time:", -AcyclicLP.distTo[t])


class AcyclicSP:
    def __init__(self, graph, V, s):
        self.edgeTo = [None]*(V+1)
        self.distTo = [0] *(V+1)
        self.G = graph
        self.distTo[s] = 0

        print("the v going in", V)
        topological = Topological(graph, V)

        print("The top order", topological.order)
        for v in reversed(topological.order):
            self.relax(v)

    def relax(self, vertex):
        for edge in self.G.adjacency_list[vertex]:
            w = edge.toVertex()
            print("w disto, weight,", w, self.distTo, edge.returnWeight())
            if self.distTo[w] > self.distTo[vertex] + edge.returnWeight():
                self.distTo[w] = self.distTo[vertex] + edge.returnWeight()
                self.edgeTo[w] = edge




# CPM = CriticalPathMethod(5, [[10, (2, 3)], [11], [12], [1,(4,)], [1]])


#4.4.19


class BellmanFord_ShortestPaths:
    def __init__(self, edgeWeightDigraph, V, s):
        self.distTo = [math.inf] * V
        self.edgeTo = [None] * V
        self.marked = [False] * V
        self.onQueue = [False] * V
        self.queue = list()
        self.G = edgeWeightDigraph
        self.V = V
        """cost is the number or relaxations performed"""
        self.cost = 0
        self.cycle = None

        self.distTo[s] = 0
        self.queue.append(s)
        self.onQueue[s] = True
        while len(self.queue) > 0 and not self.hasNegativeCycle():
            v = self.queue.pop(0)
            self.onQueue[v] = False
            self.relax(v)


    def relax(self, vertex):
        for edge in self.G.adjacency_list[vertex]:
            w = edge.toVertex()

            if self.distTo[w] > self.distTo[vertex] + edge.returnWeight():
                self.distTo[w] = self.distTo[vertex] + edge.returnWeight()
                self.edgeTo[w] = edge

                if self.onQueue[w] == False:
                    self.queue.append(w)
                    self.onQueue[w]= True

            self.cost += 1
            if self.cost % self.V == 0:
                self.findNegativeCycle()


    def findNegativeCycle(self):
        V = len(self.edgeTo)
        spt = EdgeWeightedDiagraph(V)
        for v in range(V):
            if self.edgeTo[v] is not None:
                spt.addEdge(self.edgeTo[v])

        cf = EdgeWeightedDirectedCycle(spt, V)
        self.cycle = cf.cycle


    def hasNegativeCycle(self):
        return self.cycle is not None

    def negativeCyle(self):
        return self.cycle


graph = EdgeWeightedDiagraph(8)
graph.addEdge(DirectedEdge(0,4, .38))
graph.addEdge(DirectedEdge(4,5, .35))
graph.addEdge(DirectedEdge(5,1, .32))
graph.addEdge(DirectedEdge(5,7,.77))
graph.addEdge(DirectedEdge(3,6, .52))
graph.addEdge(DirectedEdge(6,2, .4))
graph.addEdge(DirectedEdge(1,3, .29))
graph.addEdge(DirectedEdge(6,1, -1))

bf = BellmanFord_ShortestPaths(graph, 8, 0)
print("neg cycle", bf.negativeCyle())


class Arbitrage:
    def __init__(self, edgeWeightedDigraph, V, edges_and_rates):
        self.G = edgeWeightedDigraph(V)
        self.name = [None]*V
        for edge in edges_and_rates:
            self.name = edge[0]
            for toEdge in edge[1]:
                self.G.addEge(DirectedEdge(edge[0], toEdge[0],toEdge[1]))

        spt = BellmanFord_ShortestPaths(self.G, 0)

        # if spt.hasNegativeCycle():
        #     for v in spt.negativeCyle():
        #         stake = 1000
        #         print("Starting", stake, self.name[v])
        #         # stake *= math.exp(edge)
        #         print(stake, self.name[edge.fromVertex()])




#4.4.21

answer = "Beginning of trace:"

"""
edgeTo   distTo    Queue
 0-4      .38        4
 edgeTo   distTo    Queue
 0-4      .38        7, 5
 4-7      .75        
 4-5      .73        
edgeTo   distTo    Queue
 0-4      .38        5,3
 4-7      .75        
 4-5      .73        
 7-3      1.09
 7-5      1.03
edgeTo   distTo    Queue
 0-4      .38        3,1,7,4
 4-7      .75        
 4-5      .73        
 7-3      1.09
 7-5      1.03
 5-1      1.05
 5-7      1.01
 5-4      1.08
edgeTo   distTo    Queue
 0-4      .38        1,7,4, 6
 4-7      .75        
 4-5      .73        
 7-3      1.09
 7-5      1.03
 5-1      1.05
 5-7      1.01
 5-4      1.08
 3-6      1.61
"""
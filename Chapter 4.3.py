#Chapter 4.3

#4.3.1

answer = "Let a minimum spanning tree have weights (a+ b + c). Adding each weight by the same constant has the effect of" \
         "increasing the total weight of the MST, but it does not alter the constitution of the edges in the MST. The same applies" \
         "multiplying all weights by a positive constant."

#4.3.3

answer = "If a graph's edges all have distinct weights, the MST is unique. By following Prim's algorithm, adding an edge means" \
         "taking the crossing edge of minimal weight. If two weights have the same value, the tree will not be unique. If all " \
         "weights have distinct values, the tree will be unique."


#4.3.4

answer = "By way of Prim's algorithm, choosing a minimum weighted edge at each step will produce a MST. If every edge is distinct," \
         "there will be only one choice at each step. THus, the MST will be unique."

#4.3.5

answer = "The presence of multiple edges of the same weight does not prevent the greedy algorithm from finding a MST. The MST," \
         "however, may not be unique."

#4.3.6

MST = {(1,5), (5,4), (1,3), (3,2), (2,6), (2,0)}


#4.3.7

answer = "Consider all weights between a cut. Take the maximum valued edged between the two partitions. Repeat with all other " \
         "cuts of the graph until a maximum spanning tree is formed."


#4.3.8

answer = "A cycle is a minimum spanning tree plus one additional edge. Thus the minimum spanning tree of a given cycle of nodes " \
         "must be formed by removing the edge of maximum weight. Otherwise, it would not be a MST."

#4.3.9


class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def edge_weight(self):
        return self.weight

    def either(self):
        return self.v

    def other(self, vertex):
        if vertex == self.v:
            return self.w
        if vertex == self.w:
            return self.v

    def compateTo(self, other_edge):
        if self.weight < other_edge.weight:
            return -1
        elif self.weight > other_edge.weight:
            return 1
        else:
            return 0


class EdgeWeightGraph:
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adjacency_list = [[] for i in range(self.V)]

    def addEdge(self, edge):
        v = edge.either()
        w = edge.other(v)

        self.adjacency_list[v].append(edge)
        self.adjacency_list[w].append(edge)

        self.E +=1

    def adjacency_list_iterator(self, v):
        return self.adjacency_list[v]

    def vertices_count(self):
        return self.V

    def toString(self):
        for vertex in self.adjacency_list:
            for edge in vertex:
                print("the edge and weight", edge.either(), edge.other(edge.either()), edge.weight)
#4.3.11

answer = "Each edge is an object with three integer instance variables. The memory for each edge is 3 * 4 bytes for each integer" \
         "and then 16 bytes of overhead. Thus the edges consume 28*E bytes. Assuming that the adjacency list is an array of arrays" \
         "of references to objects. The inner array of objects consumers 24+40*2E bytes. The outer array consumes ~24 + 32V bytes."

#4.3.12

answer = "Prim's algorithm and Proposition J, both demonstrate that a graph's lightest edge will belong to the MST. The heaviest" \
         "edge in a graph may also belong to a MST: consider a 3 node graph with only two edges. A cycle can be composed of a cut;" \
         "therefore, it's lightest edge will belong to the MST (by Proposition J)"

#4.3.13

answer = "The problem with this implementation is that it always adds an edge to the most recently added vertex. This compromises" \
         "the cut principle, because the least weight edge will not be added to the MST"

#4.3.14

answer = "Traverse graph G's edgeTo array until the missing edge is found. Add all weights from the cut to the PQ. Take the minimum" \
         "weight on the PQ as the new edge on the MST."

#4.3.15

answer = "Traverse nodes until finding new edge. Traverse  edgeTo[] array, identifying those on both sides of the cut created" \
         "by the new edge. Compare new edge to crossing edge. Replace if the new edge weight is smaller."

#4.3.16

"""A rendition of Prim's algorithm"""


class PrimsAlgorithm:
    def __init__(self, EdgeWeightedGraph):
        self.mst = list()
        self.graph = EdgeWeightedGraph
        self.pq = IndexMinPQ(self.graph.vertices_count())
        self.marked = [False]*self.graph.vertices_count()


        self.visit(0)

        while self.pq.isEmpty() == False:
            edge = self.pq.delMin()
            v = edge.either()
            w = edge.other(v)
            if self.marked[v] and self.marked[w]:
                continue
            self.mst.append((v, w, edge.edge_weight()))
            if self.marked[v] == False:
                self.visit(v)
            if self.marked[w] == False:
                self.visit(w)
        print("The MST", self.mst)

    def visit(self, v):

        self.marked[v] = True
        for edge in self.graph.adjacency_list_iterator(v):
            if self.marked[edge.other(v)] == False:
                self.pq.insert(int(edge.weight*10), edge)




class IndexMinPQ:
    def __init__(self, N):
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
        if self.pq[j] < self.pq[k]:
            return True
        elif self.pq[j] > self.pq[k]:
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
        minimum_key = self.keys[self.pq[1]]
        self.exchange(1, self.n)
        self.n -= 1
        self.sink(1)
        self.keys[self.pq[self.n+1]] = None
        self.qp[self.pq[self.n+1]] = -1
        return minimum_key

    def isEmpty(self):
        return self.n == 0


graph = EdgeWeightGraph(9)
graph.addEdge(Edge(1,2,.5))
graph.addEdge(Edge(1,3,5))
graph.addEdge(Edge(3,4,.7))
graph.addEdge(Edge(4,7,.3))
graph.addEdge(Edge(4,6,8))
graph.addEdge(Edge(1,4,.1))
graph.addEdge(Edge(2,5,.7))
graph.addEdge(Edge(7,6,.2))
graph.addEdge(Edge(0,3,.3))


prim = PrimsAlgorithm(graph)


#4.3.17 See 4.3.9

#4.3.19

answer = "Each scan through distTo would be a linear time operation. The operation would then be multiplied by V-1. " \
         "The result of this would be significan decrease in performance. Using the priority queue makes this operation " \
         "constant time."

#4.3.20

answer = "False. Two vertices may be just an edge apart. Their edge, however, might have a large weight. As a result," \
         "the vertices would belong to different subtrees."

#4.3.21

def edges(G):
    edgeTo = G.edgeTo
    mst = list()
    for edge in edgeTo:
        mst.append(edge)
    return mst
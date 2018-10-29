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
        v = edge.either
        w = edge.other(e)

        self.adjacency_list[v].append(edge)
        self.adjacency_list[w].append(edge)

        self.E +=1

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
#Chapter 4.2


#4.2.1

answer = "Maximum number of edges V(V-1); Minimum number of edges (V-1)"

#4.2.2

adjacency_list = {
    0: [5,6],
    2: [3, 0],
    3: [6, 10],
    4: [1],
    5: [2, 10],
    6: [2],
    7: [11, 8],
    8: [4,1],
    10: [3],
    11: [8],
}

#4.2.3


class Diagraph:
    def __init__(self, v):
        self.V = v
        self.E = 0
        self.adjacency = dict()
        for i in range(self.V):
            self.adjacency[i] = list()


    def addEdge(self, v, w):

        if v == w:
            return
        if w in self.adjacency[v]:
            return

        self.adjacency[v].append(w)
        self.E += 1

    def reverseDiagraph(self):
        reversed = Diagraph()
        for v in range(self.V):
           for w in self.adjacency[v]:
               reversed.addEdge(w, v)

        return reversed

    def hasEdge(self,v, w):

        if v not in self.adjacency:
            return False
        if w in self.adjacency[v]:
            return True
        else:
            return False

#4.2.4 See hasEdge in 4.2.3

#4.2.5 See 4.2.3


#4.2.6


class Diagraph_Client_Tester:
    def __init__(self, V):
        self.diagraph = Diagraph(V)

    def addEdge(self, v,w):
        self.diagraph.addEdge(v, w)

    def hasEdge(self, v, w):
        print(self.diagraph.hasEdge(v,w))



# diagraph_tester = Diagraph_Client_Tester(10)
#
# diagraph_tester.addEdge(4,7)
# diagraph_tester.addEdge(5,3)
# diagraph_tester.addEdge(2,1)
# diagraph_tester.addEdge(6,8)
# diagraph_tester.addEdge(9,3)
# diagraph_tester.addEdge(1,4)
# diagraph_tester.addEdge(0,2)
# diagraph_tester.addEdge(8,7)
#
# diagraph_tester.hasEdge(4,7)
# diagraph_tester.hasEdge(2,1)
# diagraph_tester.hasEdge(6,8)
# diagraph_tester.hasEdge(11,5)
# diagraph_tester.hasEdge(4,8)


#4.2.7


class Degrees_Diagraph:
    def __init__(self, v):
        self.V = v
        self.E = 0
        self.adjacency = dict()
        for i in range(self.V):
            self.adjacency[i] = list()


    def addEdge(self, v, w):

        if v == w:
            return
        if w in self.adjacency[v]:
            return

        self.adjacency[v].append(w)
        self.E += 1

    def indegrees(self, w):
        count = 0
        for v in range(self.V):
            if self.hasEdge(v, w):
                count +=1

        return count

    def outdegrees(self, v):
        return len(self.adjacency[v])

    def sources(self):
        sources = list()
        for v in range(self.V):
            if 0 == self.indegrees(v):
                sources.append(v)
        return sources

    def sinks(self):
        sinks = list()
        for v in range(self.V):
            if self.outdegrees(v) == 0:
                sinks.append(v)

        return sinks

    def isMap(self):

        for v in range (self.V):
            if self.outdegrees(v) > 1 :
                return False

        return True

    def hasEdge(self,v, w):

        if v not in self.adjacency:
            return False
        if w in self.adjacency[v]:
            return True
        else:
            return False


# diagraph_tester = Degrees_Diagraph(10)
#
# diagraph_tester.addEdge(4,7)
# diagraph_tester.addEdge(5,3)
# diagraph_tester.addEdge(2,1)
# diagraph_tester.addEdge(6,4)
# diagraph_tester.addEdge(4,5)
# diagraph_tester.addEdge(1,4)
# diagraph_tester.addEdge(0,4)
# diagraph_tester.addEdge(8,7)
#
# print(diagraph_tester.outdegrees(4))
# print(diagraph_tester.indegrees(4))
# print(diagraph_tester.sources())
# print(diagraph_tester.sinks())
# print(diagraph_tester.isMap())


#4.2.8 See PDF


#4.2.9


class DirectedCycle:
    def __init__(self, G, V):
        self.marked = [None]*V
        self.edgeTo = [None]*V
        self.cycle = None
        self.onStack = [None]*V

        # print("the adjacencies", G.adjacency)
        for v in range(V):
            if self.hasCycle():
                return
            if self.marked[v] is None:
                self.dfs(G, v)

    def dfs(self, G, v):
        self.onStack[v] = True
        self.marked[v]=True


        for w in G.adjacency[v]:
            if self.hasCycle():
                return
            elif self.marked[w] is None:
                self.edgeTo[w] = v
                self.dfs(G, w)
            elif self.onStack[w]:
                self.cycle = list()
                x = v
                print("the edgeto", self.edgeTo)
                while True:
                    print("in loop", x, w)
                    if x == w:
                        break
                    self.cycle.append(x)
                    x = self.edgeTo[x]
                self.cycle.append(w)
                self.cycle.append(v)
                return self.hasCycle()

        self.onStack[v] = False

    def hasCycle(self):
        print("cycle at ", self.cycle)
        return self.cycle is not None


diagraph = Diagraph(10)
diagraph.addEdge(4,7)
diagraph.addEdge(5,3)
diagraph.addEdge(2,1)
diagraph.addEdge(6,8)
diagraph.addEdge(9,3)
diagraph.addEdge(1,4)
diagraph.addEdge(0,2)
diagraph.addEdge(8,7)
diagraph.addEdge(7,3)
# diagraph.addEdge(3,4)

# directed_cycle = DirectedCycle(diagraph,10)



class DepthFirstOrder:
    def __init__(self, G, V):
        self.pre = list()
        self.post = list()
        self.reversePostStack = list()
        self.marked = [None]*V

        for v in range(V):
            if self.marked[v] is None:
                self.dfs(G, v)

        print("pre", self.pre)
        print("post", self.post)
        print("reverse", self.reversePostStack)
    def dfs(self, G, v):

        self.pre.append(v)
        self.marked[v] = True
        for w in G.adjacency[v]:
            if self.marked[w] == None:
                self.dfs(G, w)

        self.post.append(v)
        self.reversePostStack.append(v)

# dfo = DepthFirstOrder(diagraph, 10)


class Topological:
    def __init__(self, Graph, V):
        cyclefinder = DirectedCycle(Graph, V)

        if not cyclefinder.hasCycle():
            dfo = DepthFirstOrder(Graph, V)

            for v in reversed(dfo.reversePostStack):
                print(v)

topological = Topological(diagraph, 10)


#4.2.10

answer = "Given that DFS traverses all the nodes in a graph, it should stand that aside from permutations of adjacent nodes," \
         "all topological orderings will be given."

#4.2.11

answer = "Take an initial graph consisting of a cycle of three nodes. Continually add vertices that connect to" \
         "at least two other nodes graph. The number of cycles should grow exponentially."

#4.2.12

answer = "Strongly connected components have some sort of cycle enabling the components to be mutually reachable. Reversing" \
         "a graph still preserves these cycles."

#4.2.13

answer = "Two vertices a strongly connected if they are mutually reachable. In a directed graph, if A is reachable from B" \
         "and B is reachable from A, this implies a cycle."

#4.2.14

answer = "The value of vertex v means in may be called by DFS before or after the strongly connected component C. Two situations" \
         "arise in which C is processed by DFS. 1) It is invoked by a node in C. The result is the v will be invoked by DFS later " \
         "and hence will be appear earlier in the ReversePost Order. 2) v may be processed first, and thus the edge leading to C" \
         "will invoke DFS on C. As in the earlier case, v will appear earlier in the RPO."

#4.2.15

ansewr = "The setup of this problem leads to the same solution as 4.2.14. In Gr, the edge of v leads to C, thus the answer is the"\
         "same."

#4.2.16

answer = "A kernel DAG operates just as a standard DAG. The first item in the reverse postorder, must be a source of the. The reasoning" \
         "behind this is as follows: if a vertex v is the last vertex in the adjacency list selected last by DFS, then it is " \
         "naturally the source component. On the other hand, if v is selected, and then all other nodes are processed by DFS," \
         "this also means it will be placed first in the RPO. In both cases, v is a source node."\
         "In Gr, edges are reversed. The RPO will have as its first vertex strong component that acts as a source to Gr. Self evidently, if edges" \
         "are reveresed again, this strong component is a sink in G."
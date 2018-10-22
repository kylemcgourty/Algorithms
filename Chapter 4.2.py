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


diagraph_tester = Degrees_Diagraph(10)

diagraph_tester.addEdge(4,7)
diagraph_tester.addEdge(5,3)
diagraph_tester.addEdge(2,1)
diagraph_tester.addEdge(6,4)
diagraph_tester.addEdge(4,5)
diagraph_tester.addEdge(1,4)
diagraph_tester.addEdge(0,4)
diagraph_tester.addEdge(8,7)

print(diagraph_tester.outdegrees(4))
print(diagraph_tester.indegrees(4))
print(diagraph_tester.sources())
print(diagraph_tester.sinks())
print(diagraph_tester.isMap())


#4.2.8


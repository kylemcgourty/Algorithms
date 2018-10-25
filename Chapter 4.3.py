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



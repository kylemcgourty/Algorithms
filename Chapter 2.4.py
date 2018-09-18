#Chapter 2.4

#2.4.1

answer = "R R P O T Y I I U Q  E U"


#2.4.2

answer = "Two pitfalls: the array would need to be resized for every additional entry. Second," \
         "after removing the first max, how would one remove the second max and so forth? One could keep" \
         "track with a second array, but this is not space and time efficient."

#2.4.3

class PQUnorderArray:
    def __init__(self):
        self.uo_array = [];

        self.uo_array = [4, 5, 77, 22, 1, 33]
        self.push(99)
        self.push(88)
        print(self.remove_maximum())

    def push(self, key):
        self.uo_array.append(key)

    def remove_maximum(self):
        max = 0
        max_index = 0
        for index, key in enumerate(self.uo_array):
            if key > max:
                max = key
                max_index = index

        return self.uo_array.pop(max_index)


#UO_array = PQUnorderArray()

unordered_array_runtime = "Insert in constant. Remove maximum is proportional to array size"

def exchange(a, i , j):
    initial = a[i]
    a[i] = a[j]
    a[j] = initial


class PQOrderedArray:
    def __init__(self):
        self.ordered = list()
        self.ordered.insert(0, 1)
        self.swim(len(self.ordered),3)
        self.swim(len(self.ordered),7)
        self.swim(len(self.ordered),2)
        self.swim(len(self.ordered),11)
        self.swim(len(self.ordered),5)

        self.remove_maximum();

        self.remove_maximum();

    def swim(self, idx, key):
        self.ordered.insert(len(self.ordered), key)
        # idx +=1
        print(self.ordered, idx)
        while idx > 1 and self.ordered[idx//2] < self.ordered[idx]:
            exchange(self.ordered, idx//2, idx)
            idx = idx//2

        print("udpated array", self.ordered)

    def remove_maximum(self):


        max = self.ordered[1]

        exchange(self.ordered, 1, len(self.ordered)-1);

        self.ordered.pop(len(self.ordered)-1)

        self.sink(1, self.ordered[1])

        print("the max and new array", max, self.ordered)


    def sink(self, idx, key):

        while 2*idx < len(self.ordered):
            j = idx *2
            if j +1 < len(self.ordered) and (self.ordered[j] < self.ordered[j+1]):
                j += 1
            if key >= self.ordered[j]:
                break
            exchange(self.ordered, idx, j)
            idx = j



#OrderedArray_PQ = PQOrderedArray()


answer = "The PQ ordered array requires lg n + 1 compares for " \
         "insert and 3 lg n compares for remove the maximum"


class UnorderedLinkedList:
    def __init__(self):


        self.front = None
        self.end = None
        self.length = 0

        self.insert(1)
        self.insert(7)
        self.insert(5)
        self.insert(11)
        self.insert(2)

        self.remove_maximum()
        self.remove_maximum()

    class Node:
        def __init__(self, val):
            self.next = None
            self.value = val

    def insert(self, val):

        new_node = self.Node(val)
        if self.end != None:
             self.end.next = new_node
        self.end = new_node

        if self.length == 0:
             self.front = new_node

        self.length += 1

    def remove_maximum(self):
         max = 0
         node = self.front
         while node.next:

             if node.value > max:
                 max = node.value
             node = node.next

         if self.front.value == max:
             self.front = self.front.next

             return
         node2 = self.front.next
         node1 = self.front

         while node2 is not None:
            if node2.value == max:
                self.remove_logic(node1, node2)
            node1 = node1.next
            node2 = node2.next

         print("the max,", max)

    def remove_logic(self,previous, current):
        previous.next = current.next
        current = None

#UOLL = UnorderedLinkedList()

answer = "The runtime for an unordered list PQ is constant time for insert and proportional to 2n for remove" \
         "the maximum"


class PQOrderedLinkedList:
    def __init__(self):

        self.front = None
        self.end = None
        self.length = 0

        # first = self.Node(1)
        # first.previous = None
        # first.next = None
        self.front = None
        self.end = None


        self.insert(1)
        self.insert(7)
        self.insert(5)
        self.insert(11)
        self.insert(2)

        self.inspectList()

        # self.remove_maximum()
        # self.remove_maximum()

    class Node:
        def __init__(self, val):
            self.next = None
            self.previous = None
            self.value = val

    def inspectList(self):
        first = self.front
        print("node1", first)
        # while (first.next != None):
        #     print("node", first.next.value)
        #     first = first.next

    def insert(self, val):

        new_node = self.Node(val)

        self.length += 1

        self.swim(new_node, self.length)

    def swim(self, new_node, index):

        if self.end != None:
            self.end.next = new_node
            new_node.previous = self.end
        self.end = new_node
        if self.length == 1:
            self.front = new_node


        if index == 0 or index == 1:
            return


        node = self.end
        if index == 1:
            i = 1
        else:
            i = (index ) // 2
        j = index
        while j > i:
            node = node.previous
            j -= 1
        if node.value < new_node.value:
            new_location_node =self.exchange(node, new_node)
            # if index == self.length:
            #     self.set_new_end(new_location_node)
            self.swim(new_location_node, j)
        else:

            return

        # self.ordered.insert(len(self.ordered), key)
        # # idx +=1
        # print(self.ordered, idx)
        # while idx > 1 and self.ordered[idx//2] < self.ordered[idx]:
        #     exchange(self.ordered, idx//2, idx)
        #     idx = idx//2


    def set_new_end(self, node):
        self.end = node

    def exchange(self, node1, node2):

        value = node1.value

        node1.value = node2.value

        node2.value = value
        return node2
    # def remove_maximum(self):
    #
    #
    #     max = self.ordered[1]
    #
    #     exchange(self.ordered, 1, len(self.ordered)-1);
    #
    #     self.ordered.pop(len(self.ordered)-1)
    #
    #     self.sink(1, self.ordered[1])
    #
    #     print("the max and new array", max, self.ordered)
    #
    #
    # def sink(self, idx, key):
    #
    #     while 2*idx < len(self.ordered):
    #         j = idx *2
    #         if j +1 < len(self.ordered) and (self.ordered[j] < self.ordered[j+1]):
    #             j += 1
    #         if key >= self.ordered[j]:
    #             break
    #         exchange(self.ordered, idx, j)
    #         idx = j

#PQOrdered_LL = PQOrderedLinkedList()


answer = "While this code is incomplete, insert has a time complexity proporitional n and remove the max" \
         "has a runtime proportional to n"


#2.4.4

answer = "Yes, because each value at k will always be greater than the values at 2k, 2k+1"

#2.4.5

answer = "E" \
         "E A" \
         "S E A" \
         "Y S E A" \
         "Y S Q E A" \
         "Y U S Q E A" \
         "Y U S Q E E A" \
         "Y U S S Q E E A" \
         "Y U T S S Q E E A" \
         "Y U T S S Q I E E A" \
         "Y U T S S Q O I E E A" \
         "Y U T S S Q O N I E E A"

#2.4.6

answer = "P" \
         "R P" \
         "R P I" \
         "R P O I" \
         "P O I" \
         "R P O I" \
         "R P O I" \
         "O I" \
         "O I I" \
         "I I" \
         "T I I" \
         "I I" \
         "Y I I" \
         "Q " \
         "Q U" \
         "Q U E" \
         "U" \
         "E"

#2.4.7

answer = "The second largest element may appear at index 2 or 3. It may not appear anywhere else." \
         "The 3rd largest element may appear at 2, 3, 4, 5, 6, 7." \
         "The 4th largest element may appear at 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15"



#2.4.8

answer = "the Kth smallest item is the (n-k)th largest. The position for the (n-k)th largest" \
         "can be found to range from (n-k), if (n-k) is even, or (n-k)-1, if (n-k) is odd," \
         "to the end value found by iterating through " \
         "for (i = 1; i < (n-k); i ++){ i = (2*i) + 1}."

#2.4.9


answer = "Assuming we care constructing max heaps, then"
bheaps ="E D C B A"\
         "E D C A B"\
         "E C D B A"\
         "E C D A B"\
         "E D A B C"\
         "E D B A C"\

twokeybheaps ="B B A A A" \
            "B A B A A"


#2.4.10

answer = "The parents exists at index i. Children occupy space 2i + 1 and 2i+2"


#2.4.11

answer = "The inserts for an unordered array are constant time while a remove the maximum is at least n." \
         "The inserts for a heap have a time complexity of 1 + lg n and 2lg n compares for remove the maximum." \
         "Inserts for an ordered array have a run time proportional to n while remove the maximum is constant time." \
         "Given the large numer of inserts, an uordered array would be the best choice in this scencario."

#2.4.12

answer = "The best choices lie between an ordered array and a heap. Heap inserts take time proportional" \
         "to log n and ordered array inserts have a runtime proporitional to n. Both have a " \
         "find the maximum runtime that is constant. Therefore, a binary heap would be the best" \
         "choice in this scenario."


#2.4.13

answer = "The compare j < n can be removed if the following code is made its substitute"

# def sink(k):
#     while((j = 2*k) <= n){
#        if j == n:
#            compare_and_exchange(j, k)
#         else:
#         if less(j, j+1):
#             j +=1
#             compare_and_exchange(j, k)
#
# def compare_and_exchange(j, k):
#     """exchange details"""
#     if !less(k, j):
#         break;
#     exchange(k, j);


#2.4.15

# def MinPQ_Tester(pq, keys):
#     minimum = keys[pq[0]]
#     for index in pq[1:]:
#         if minimum < keys[pq[index]]:
#             minimum = keys[pq[index]]
#         else:
#             return "Not a minimum PQ"

#2.4.16

answer = "Heapsort will use as few compares as possible for an array with similar entries. This is because the " \
         "call to sink will use one less compare per iteration." \
         "By contrast, heap sort will use as many compares are possible if the array is sorted in reverse."

#2.4.17

answer = "Take a pq of size k. Do n - k inserts and remove the minimum. Each call to insert calls swim. The call to " \
          "deleteMin removes the minimum and sinks an item from the bottom of the array. Since each call is guaranteed" \
          "to remove the minimum value in the PQ, the remaining items are larger. Thus, n - k such calls will leave the k" \
          "largest of the n items in the pq."


#2.4.18

answer = "Part 1: A heap receives a new max item. Swim is called, moving the item to the beginning of the array." \
         "DelMax takes an item at the bottom of the array. The call to sink may move it to a new position in the array." \
         "Part 2: The heap receives two max items followed by two DelMax calls. It can be shown the heaps will no longer be " \
         "identical."

#2.4.19


class MaxPQ:
    def __init__(self, array):
        self.array = array
        self.size = len(array)-1
        for index in range(self.size//2, -1, -1):
            self.sink(index)

        print("The max pq array", self.array)

    def sink(self, k):
        while 2*k <= self.size:
            j = 2*k
            if j < self.size and self.array[j] < self.array[j+1]:
                j +=1
            if self.array[k] > self.array[j]:
                break
            exchange(self.array, k, j);
            k = j;



maxPQ = MaxPQ([3, 5, 6, 2, 1, 9, 7, 88, 22, 11])


#2.4.20

answer = "Sink based construction begins with iterating in reverse through the first half of the array. Half of" \
         "these calls to sink (1/4 of the total array), will be involved with construting subheaps. At worst case," \
         "there will be 1/4 *3 n compares and 1/4 exchanges. As the iteration proceeds through the first quarter " \
         "of the array, the subheaps are ordered. Each step in this case would take at worst 1/4* 6n compares" \
         "and 1/4 * 2n exchanges. These totals are 9/4n (~2n) compares and 3/4 (~n) exhanges.
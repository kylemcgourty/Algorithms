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
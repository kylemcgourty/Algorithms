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

        print("array after exchange", self.ordered)

        self.ordered.pop(len(self.ordered)-1)

        self.sink(1, self.ordered[1])


        print("max new array", max, self.ordered)


    def sink(self, idx, key):

        print("The indx and key in sink", idx, key)
        while 2*idx < len(self.ordered):
            j = idx *2
            print("the j values", j)
            if j +1 < len(self.ordered) and (self.ordered[j] < self.ordered[j+1]):
                j += 1
            if key >= self.ordered[j]:
                break
            exchange(self.ordered, idx, j)
            idx = j



OrderedArray_PQ = PQOrderedArray()
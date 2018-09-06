#Chapter 1.5.1

print("Hello chapter 1.5")


#1.5.1 and

class QuickFind:
    def __init__(self):
        self.id = [i for i in range(10)]
        print('the array', self.id)
        self.count = 10

        self.union(9, 0)
        self.union(3, 4)
        self.union(5, 8)
        self.union(7, 2)
        self.union(2, 1)
        self.union(5, 7)
        self.union(0, 3)
        self.union(4, 2)


    def find(self, p):
        return self.id[p]

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        pID = self.find(p)
        qID = self.find(q)


        if pID == qID:
            return

        loop_counter = 2
        for index, _ in enumerate(self.id):
            loop_counter += 1
            if self.id[index] == pID:
                self.id[index] = qID
                loop_counter += 1


        print("array accesses", loop_counter)
        print("new id array", self.id)
        self.count -= 1




#quick_find = QuickFind()

#1.5.2

class QuickUnion:
    def __init__(self):
        self.id = [i for i in range(10)]
        print('the array', self.id)
        self.count = 10
        self.array_accesses = 0

        self.quickunion(9, 0)
        self.quickunion(3, 4)
        self.quickunion(5, 8)
        self.quickunion(7, 2)
        self.quickunion(2, 1)
        self.quickunion(5, 7)
        self.quickunion(0, 3)
        self.quickunion(4, 2)

    def find(self, p):
        while p != self.id[p]:
            self.array_accesses +=2
            p = self.id[p]
        return p


    def quickunion(self, p, q):
        self.array_accesses = 0
        i = self.find(p)
        j = self.find(q)
        if i == j:
            return
        self.id[i] = j
        self.array_accesses += 1
        print("the array and array accesses", self.id, self.array_accesses)

        self.count -= 1


#quickunion = QuickUnion()


#1.5.3

class WeightedQuickUnion:
    def __init__(self):
        self.id = [i for i in range(10)]
        self.sz = [1 for i in range(10)]
        print('the arrays', self.id, self.sz)
        self.count = 10
        self.array_accesses = 0

        """ intial 1.5.3 inputs"""
        # self.weighted_quickunion(9, 0)
        # self.weighted_quickunion(3, 4)
        # self.weighted_quickunion(5, 8)
        # self.weighted_quickunion(7, 2)
        # self.weighted_quickunion(2, 1)
        # self.weighted_quickunion(5, 7)
        # self.weighted_quickunion(0, 3)
        # self.weighted_quickunion(4, 2)

        """" 1.5.4 reference inputs """

        self.weighted_quickunion(4, 3)
        self.weighted_quickunion(3, 8)
        self.weighted_quickunion(6, 5)
        self.weighted_quickunion(9, 4)
        self.weighted_quickunion(2, 1)
        self.weighted_quickunion(5, 0)
        self.weighted_quickunion(7, 2)
        self.weighted_quickunion(6, 1)

        """Worst case inputs"""

        print ("worst case inputs")
        self.weighted_quickunion(0, 1)
        self.weighted_quickunion(2, 3)
        self.weighted_quickunion(4, 5)
        self.weighted_quickunion(6, 7)
        self.weighted_quickunion(0, 2)
        self.weighted_quickunion(4, 6)
        self.weighted_quickunion(0, 4)

    def find(self, p):
        while p != self.id[p]:
            self.array_accesses +=1
            p = self.id[p]
        return p


    def weighted_quickunion(self, p, q):
        self.array_accesses = 0
        i = self.find(p)
        j = self.find(q)
        if i == j:
            return
        if self.sz[i] > self.sz[j]:
            self.sz[j] += self.sz[i]
            self.id[i] = j
        else:
            self.sz[i] += self.sz[j]
            self.id[j] =i

        self.array_accesses += 2
        print("the weighted array and array accesses", self.id, self.sz, self.array_accesses)

        self.count -= 1

#weighted_quickunion = WeightedQuickUnion()


#1.5.4
# See 1.5.3 reference and worst-case inputs

#1.5.5

answer = "10 machine instructions in the inner loop + 2 other array accesses. 10^6 input pairs * 10^9 sites * 12 instructions = 1.2 * 10^15 instructions" \
         "1.2 * 10^15 instructions * 1 second / 10^9 instructions == 12 million seconds. 8640 seconds in a day. It would take 1,388 days"

#1.5.6

answer = "Weighted quick union uses at most c m lg n array accesses, m is connections and n is sites. Let c == 2. Let the number of input pairs be the" \
         "number of connections to be established. Thus we have, 2 * 10^6 lg 10^9 = 590, 794, 000. Converting to seconds: 59794000 * 1 second/ 10^9 instructions =" \
         "approximately .058 seconds"


#1.5.7

#See 1.5.1 and 1.5.2

#1.5.8

answer = "Rather than store the results of id[p], the call to union uses at worst two array accesses to id[p] inside the inner loop"

#1.5.9
"""Tree"""
"""   1
   0  3  6
     2 7   5
          9  4
               8
"""

answer = "By Proposition H, the height of any node forest built by weighted quick-union is at most lg n. Since this height of 4 > lg 10, it violates the proposition."


#1.5.10

answer = "Yes, the algorithm would function. But the tree heights would be increased."

#1.5.11


class WeightedQuickUnionExperiment:
    def __init__(self):
        self.id = [i for i in range(10)]
        self.sz = [1 for i in range(10)]
        print('the arrays', self.id, self.sz)
        self.count = 10
        self.array_accesses = 0



        """" reference inputs """

        self.weighted_quickunion(4, 3)
        self.weighted_quickunion(3, 8)
        self.weighted_quickunion(6, 5)
        self.weighted_quickunion(9, 4)
        self.weighted_quickunion(2, 1)
        self.weighted_quickunion(5, 0)
        self.weighted_quickunion(7, 2)
        self.weighted_quickunion(6, 1)


    def find(self, p):
        while p != self.id[p]:
            self.array_accesses +=1
            p = self.id[p]
        return p


    def weighted_quickunion(self, p, q):
        self.array_accesses = 0
        i = self.find(p)
        j = self.find(q)
        if i == j:
            return
        if self.sz[i] > self.sz[j]:
            self.sz[i] += self.sz[j]
            self.changeAllComponents(q, p)
        else:
            self.sz[j] += self.sz[i]
            self.id[j] =i
            self.changeAllComponents(p, q)

        self.array_accesses += 2
        print("the weighted array and array accesses", self.id, self.sz, self.array_accesses)

        self.count -= 1

    def changeAllComponents(self, smaller , larger):
        while smaller != self.id[smaller]:
            p = self.id[smaller]
            self.id[smaller] = larger
            smaller = p
            self.array_accesses += 3


#weighted_quickunion = WeightedQuickUnionExperiment()

answer = "The tree has a much flatter structure at the expense of more array accesses."
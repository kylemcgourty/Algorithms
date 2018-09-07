#Chapter 2.2


#2.2.1

i = 0
j = 5


aux = "A E Q S U Y E I N O S T"

"""TABLE:
   i  j    a
   0       A
   1       A E 
      5    A E E
      6    A E E I
      7    A E E I N
      8    A E E I N O
   2       A E E I N O Q
   3       A E E I N O Q S
      9    A E E I N O Q S S
      10   A E E I N O Q S S T
   4       A E E I N O Q S S T Y   

"""



#2.2.2
answer = "topdown mergesort"
"""                  a = E A S Y Q U E S T I O N
        
merge(a, 0, 0, 1)    a = A E
merge(a, 2, 2, 3)    a =     S Y
merge(a, 0, 1, 3)    a = A E S Y
merge(a, 4, 4, 5)    a           Q U
merge(a, 6, 6, 7)    a =             E S
merge(a, 4, 5, 7)    a =         E Q S U
merge(a, 0, 3, 7)    a = A E E Q S S U Y
merge(a, 8, 8, 9)    a =                 I T
merge(a, 10, 10, 11) a =                     N O
merge(a, 8, 9, 11)   a =                 I N O T
merge(a, 0, 5, 11)   a = A E E I N O Q S S T U Y
"""

#2.2.3
answer = "bottomup mergesort"

"""                  a = E A S Y Q U E S T I O N

merge(a, 0, 0, 1)    a = A E
merge(a, 2, 2, 3)    a =     S Y
merge(a, 4, 4, 5)    a           Q U
merge(a, 6, 6, 7)    a =             E S
merge(a, 8, 8, 9)    a =                 I T
merge(a, 10, 10, 11) a =                     N O
merge(a, 0, 1, 3)    a = A E S Y
merge(a, 4, 5, 7)    a =         E Q S U
merge(a, 8, 9, 11)   a =                 I N O T
merge(a, 0, 3, 7)    a = A E E Q S S U Y
merge(a, 0, 5, 11)   a = A E E I N O Q S S T U Y
"""

#2.2.4

answer = "Yes. Otherwise as sorting proceeds, a small key may occur later on in the unordered subarray." \
         "As a result, the output would not be in sorted order."

#2.2.5

"""
Top down
Subarray lengths: 2, 4, 8, 16, 32, 39.

Bottom up
Subarray lengths: 2, 4, 8, 16, 32, 39

"""

#2.2.6
import math
import numpy

class MergeSort:
    def __init__(self):


        for i in range(1, 513):
            self.array_accesses = 0
            self.compares = 0
            self.aux = [None]*i;
            self.a = numpy.random.randint(0,i, i)
            self.sort(0, len(self.a)-1)
            # print("sorted", self.a)
            print("the compares", self.compares)
            # print("actual array accesses", self.array_accesses)
            # print("predicted array accesses", 6*i*math.log(i, 2))



    def sort(self, lo, hi):

        if hi <= lo:
            return
        mid = lo + (hi-lo)//2
        self.sort(lo, mid)
        self.sort(mid+1, hi)
        self.merge(lo, mid, hi)

    def merge(self, lo, mid, hi):

        i = lo
        j = mid+1

        for k in range(lo, hi+1):
            self.aux[k] = self.a[k]
            self.array_accesses += 2

        for k in range(lo, hi+1):
            if i > mid:
                self.a[k] = self.aux[j]
                j += 1
                self.compares += 1

            elif j > hi:
                self.a[k] = self.aux[i]
                i += 1
                self.compares +=2
            elif self.less(self.aux[j], self.aux[i]):
                self.a[k] = self.aux[j]
                j += 1
                self.compares +=3
            else:
                self.a[k] = self.aux[i]
                i += 1
                self.compares += 3
            self.array_accesses += 2

    def less(self, a, b):
        self.array_accesses += 2
        if a < b:
            return True
        else:
            return False


# merge = MergeSort()



class BottomUpMergeSort:
    def __init__(self):

        # self.array_accesses = 0
        # self.a = [4, 22, 2, 11, 6, 8]
        # self.aux = [None] * 6
        # self.sort()
        # print("array", self.a)

        for i in range(1, 513):
            self.array_accesses = 0
            self.aux = [None]*i;
            self.a = numpy.random.randint(0,i, i)
            self.sort()
            print("sorted", self.a)
            print("actual array accesses", self.array_accesses)
            print("predicted array accesses", 6*i*math.log(i, 2))



    def sort(self):
        length = len(self.a)
        iterables = [2 ** j for j in range(0, length+1, 1) if 2 ** j < length]

        print("the iterables", iterables)
        for i in iterables:
            for j in range(0, length - i, 2*i):
                self.merge(j, j + i - 1, min([j + i + i - 1, length - 1]))



    def merge(self, lo, mid, hi):

        i = lo
        j = mid+1

        for k in range(lo, hi+1):
            self.aux[k] = self.a[k]
            self.array_accesses += 2

        for k in range(lo, hi+1):
            if i > mid:
                self.a[k] = self.aux[j]
                j += 1
            elif j > hi:
                self.a[k] = self.aux[i]
                i += 1
            elif self.less(self.aux[j], self.aux[i]):
                self.a[k] = self.aux[j]
                j += 1
            else:
                self.a[k] = self.aux[i]
                i += 1
            self.array_accesses += 2

    def less(self, a, b):
        self.array_accesses += 2
        if a < b:
            return True
        else:
            return False


#BMS = BottomUpMergeSort()


#2.2.7

#See class on 2.2.6 mergesort

#2.2.8

"""experimental mergesort: skip already sorted arrays"""


class ExperimentalMergeSort:
    def __init__(self):


        for i in range(1, 513):
            self.array_accesses = 0
            self.compares = 0
            self.aux = [None]*i;
            self.a = numpy.random.randint(0,i, i)
            self.sort(0, len(self.a)-1)
            print("sorted", self.a)
            print("compares", self.compares)

            # print("actual array accesses", self.array_accesses)
            # print("predicted array accesses", 6*i*math.log(i, 2))



    def sort(self, lo, hi):

        if hi <= lo:
            return
        mid = lo + (hi-lo)//2
        self.sort(lo, mid)
        self.sort(mid+1, hi)

        if self.a[mid] <= self.a[mid+1]:
            self.compares += 1
            pass
        else:
            self.compares += 1
            self.merge(lo, mid, hi)

    def merge(self, lo, mid, hi):

        i = lo
        j = mid+1

        for k in range(lo, hi+1):
            self.aux[k] = self.a[k]
            self.array_accesses += 2

        for k in range(lo, hi+1):
            if i > mid:
                self.a[k] = self.aux[j]
                j += 1
                self.compares += 1

            elif j > hi:
                self.a[k] = self.aux[i]
                i += 1
                self.compares += 2

            elif self.less(self.aux[j], self.aux[i]):
                self.a[k] = self.aux[j]
                j += 1
                self.compares +=3
            else:
                self.a[k] = self.aux[i]
                i += 1
                self.compares +=3

            self.array_accesses += 2

    def less(self, a, b):
        self.array_accesses += 2
        if a < b:
            return True
        else:
            return False


#ems = ExperimentalMergeSort()

"""Sorted arrays would have a linear number of compares given the change made in experimental mergesort."""



#2.2.9

"""My implementatinos use an instance variable for aux."""
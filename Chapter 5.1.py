#Chapter 5.1


#5.1.1

courses_and_room = [("Databases 1", 1), ("AI 3", 5), ("Design 2", 2), ("Operating Systems 5.0", 4),
                    ("AI Deep Learning", 5), ("Design Databases", 2), ("Operating Systems Linux", 4),
                    ("Databases SQL", 1), ("AI Networks", 5),
                    ("Databases NoSQL", 1), ("AI", 5), ("Design Software", 2), ("Operating Systems MacOS", 4),
                    ("Databases Big Data", 1), ("AI", 5), ("Operating Systems Windows", 4), ("Robotics", 3)]


class keyIndexCounter:
    def __init__(self, a):
        self.data = a
        self.count = [0]*7
        self.aux = [0]*(len(a)+1)

        self.distinguish_unique_keys()
        self.transform_keys_to_indices()
        self.sort_keys(len(a))

    def distinguish_unique_keys(self):
        for item in self.data:
            self.count[item[1]+1] += 1
    def transform_keys_to_indices(self):
        R = len(self.count)-1
        for i in range(R):
            self.count[i+1] += self.count[i]

    def sort_keys(self, n):
        for i in range(n):
            self.aux[self.count[self.data[i][1]]] = (self.data[i][0], self.data[i][1])
            self.count[self.data[i][1]] +=1

        print("the sorted array", self.aux)


# keyIndexCounter(courses_and_room)


#5.1.2

"""
LSD TRACE

pa         
pe         
of         
th        
th        
th         
ai         
ti
al
fo
to
is

ai
al
fo
is
pa
pe
th
th
th
ti
to

"""

#5.1.3

"""
MSD trace

al
ai
fo
go
is
no
pa
pe
th
ti
th
th
to

ai 
al
fo
go
is
no
pa
pe
th
th
th
ti
to

"""

#5.1.4

"""
Trace for 3 way quicksort. Multiple recursive calls shown in each step

1st

is 
fo
al
go
co
ai


no


th
ti
pe
to
to
th
of
th
pa


2nd

fo
al
go
co
ai

is 


pe 
of 
pa

th
ti
th
th
to


3rd

al
co
ai

fo

go

is 

of
pe
pa

th
th
th
ti
to

4th

al
ai

co

fo

go

is 

of
pa
pe

th
th
ti
to

4th

ai 
al
co
fo
go
is
of
pa
pe
th
th
ti
to
"""

#5.1.5

"""
MSD trace

all
aid
come
for
good
is
now
of
people
the
time
to
to
the

aid
all
come
for
good
is
now 
of
people
the
the
time
to
to
"""

#5.1.7

"""To be completed"""
# class KeyIndexedCounterWithQueue:
#     def __init__(self, a, size):
#         self.a = a
#         self.count = [0]*size;
#         self.count_helper = [0]*size;
#         self.aux = [None]*len(a)
#
#         self.countKeys()
#         self.transitionToIndices()
#         self.accumulateInQueues()
#
#         print("the aux array", self.aux)
#
#     def countKeys(self):
#
#         for class_data in self.a:
#             self.count[class_data[1]]+=1
#
#     def transitionToIndices(self):
#
#         for index in self.count:
#
#             if index == len(self.count)-1:
#                 return
#
#             self.count[index+1] += self.count[index]
#
#     def accumulateInQueues(self):
#
#         for class_data in self.a:
#             diff = self.count[class_data[1]]-self.count[class_data[1]-1]
#             if self.aux[class_data[1]] == None:
#                 self.aux[class_data[1]] = [0]*(diff)
#             else:
#                 self.aux[class_data[1]][self.count_helper[class_data[1]]] = class_data
#                 self.count_helper[class_data[1]] +=1
#
# counter = KeyIndexedCounterWithQueue(courses_and_room, 6)


#5.1.8

answer = "For MSD, the runtime would be proportional to 1/2n^2. For three-way quicksort," \
         " the runtime is proportinal to 1/2n^2 log R"

#5.1.10

answer = "The worst case runtime would be W*n log (size of alphabet)"
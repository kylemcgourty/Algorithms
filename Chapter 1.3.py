# Chapter 1.3

# 1.3.1

class FixedCapacityStackOfStrings:

    def __init__(self, max_capacity):
        self.stack = [None] * max_capacity
        self.max_capacity = max_capacity
        self.index = 0
    def push(self, item):
        if self.index  < self.max_capacity:
            self.stack[self.index] = item
            self.index += 1
    def isFull(self):
        return self.index == self.max_capacity


stack = FixedCapacityStackOfStrings(10)

stack.push("tree")
print(stack.isFull())


# 1.3.2

answer = "was best times of the was the it"


# 1.3.3

answer  = "b,e,f,g"



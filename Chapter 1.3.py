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


#stack = FixedCapacityStackOfStrings(10)

#stack.push("tree")
#print(stack.isFull())


# 1.3.2

answer = "was best times of the was the it"


# 1.3.3

answer  = "b,e,f,g"


# 1.3.4

import fileinput

class Parentheses:

    def __init__(self):

        self.parentheses = list(str(input("Enter brackets, parentheses, and braces :")))

        self.stack = []

        self.check_parentheses()

#performs the matching logic
    def check_parentheses(self):
        while(True):

            if len(self.parentheses) == 0:
                print("successful")
                return
            top = self.parentheses.pop(0)

            if top == ")" or top == "]" or top == "}":
                match = self.stack.pop(0)
                if top == ")" and match == "(":
                    continue
                if top == "]" and match == "[":
                    continue
                if top == "}" and match == "{":
                    continue
                print("error matching!")
                return
            else:
                self.stack.insert(0, top)
                continue



# 1.3.5

answer = "Prints the binary representation of n"

# 1.3.6

answer = "Reverses the order of the queue"


# 1.3.7

class Stack:

    def __init__(self):
        self.stack = []
        self.index

    def peek(self):
        return self.stack[self.index]


#1.3.8

notes = "Resizing array stack of strings"

answer = "stack size of 1, value in stack: 'it'"


#1.3.9


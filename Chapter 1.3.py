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

# function that completes left parentheses

class ParenthesesProcessor:
    def __init__(self, incomplete_math_expression):
        self.expressions = []
        self.operators = []
        self.final_expression = ""
        self.missing_parentheses_parser(incomplete_math_expression)

    def missing_parentheses_parser(self, incomplete_math_expression):
        for character in incomplete_math_expression:
            if self.operand_determiner(character):
                self.expressions.append(character)
            elif self.operator_determiner(character):
                self.operators.append(character)
            elif self.parentheses_determiner(character):
                first_expression = self.expressions.pop()
                operator = self.operators.pop()
                second_expression = self.expressions.pop()
                newexpression ='(' + second_expression + operator + first_expression + ')'
                self.expressions.append(newexpression)

        print("before,", self.expressions)
        for expression in self.expressions:
            self.final_expression += expression

        print(self.final_expression)

    def operand_determiner(self, character):
        if character in set(["1", "2", "3", "4", "5", "6", "7","8", "9"]):
            return True
        else:
            return False
    def operator_determiner(self, character):
        if character == '+' or character == '-' or character == '*':
            return True
        else:
            return False
    def parentheses_determiner(self, character):
        if character == ')':
            return True
        else:
            return False


#parentheses = ParenthesesProcessor("1+2)*3-4)*5-6)))")


#1.3.10
#TBC
#converts infix to postfix (operators trail operands)


# class InfixToPostfix:
#     def __init__(self, mathematical_expression):
#         self.experssions = list()
#         self.operators = list()
#         self.skip = False
#         self.convert_to_postfix(mathematical_expression)
#
#     def convert_to_postfix(self, mathematical_expression):
#         for char, index in enumerate(mathematical_expression):
#             if self.skip:
#                 self.skip = False
#                 continue;
#             if mathematical_expression == "(" or mathematical_expression == ")":
#                 continue;
#             if self.operand_determiner(char):
#                 self.experssions.append(char)
#             elif self.operator_determiner(char):
#                 if mathematical_expression[index+1] != "(":
#                     self.convert_to_postfix(mathematical_expression[index+1])
#                     newexpression = "".join(self.experssions[-2:])
#                     newexpression += char
#                     self.expressions.append(newexpression)
#                     self.skip = True
#                     if len(self.experssions) > 1:
#                         self.compose()
#                 else:
#                     self.operators.append(char)
#
#         print("the final", self.experssions)
#
#     def compose(self):
#         first_expression =self.experssions.pop()+self.operators.pop()+self.operators.pop()
#         new_expression = self.experssions.pop()+ first_expression
#         self.expressions.append(new_expression)
#
#     def operand_determiner(self, character):
#         if character in set(["1", "2", "3", "4", "5", "6", "7", "8", "9"]):
#             return True
#         else:
#             return False
#
#     def operator_determiner(self, character):
#         if character == '+' or character == '-' or character == '*' or character == "/":
#             return True
#         else:
#             return False


#postfix = InfixToPostfix("A*B+C/D")


#1.3.11

import operator

class EvaluatePostfix:
    def __init__(self, postfix):
        self.operands = list()
        self.operators_table = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
        self.evaluate(postfix)


    def evaluate(self, postfix):
        for index, char in enumerate(postfix):
            if self.char_eval(char):
                self.operands.append(char)
            else:
                self.operand_combiner(char)

        print("result", self.operands.pop())

    def char_eval(self, char):
        if char in set(["1", "2", "3", "4", "5", "6", "7", "8", "9"]):
            return True
        else:
            return False

    def operand_combiner(self, op):
        most_recent_operand = int(self.operands.pop())
        second_operand = int(self.operands.pop())
        evaluated_expression = self.operators_table[op](second_operand, most_recent_operand)
        self.operands.append(evaluated_expression)


#postfix = EvaluatePostfix("223+*4/")


#1.3.12
"""copy function for a stack of strings"""

class CopyStack:
    def __init__(self, string_stack):
        self.copy_stack(string_stack)
    def copy_stack(self, string_stack):
        """I'm cheating because this is Python. Future exercises in C to come."""
        return string_stack.copy()

#1.3.13

answer = "b, c, d"

#1.3.14

import numpy
class ResizingArrayQueueOfStrings:

    def __init__(self, array_size):
        self.queue = numpy.empty(array_size, object)
        self.array_pointer = 0
        self.dq_array_pointer = 0
        self.array_size = array_size
        self.amount = 0
    def enqueue(self, item):
        self.queue[self.array_pointer] = item
        self.array_pointer = (self.array_pointer + 1) % self.array_size

        """resizing logic"""
        self.amount +=1
        if self.amount > 1/2 * self.array_size:
            self.resize()
        print(self.queue)
    def dequeue(self):
        string_item = self.queue[self.dq_array_pointer]
        self.queue[self.dq_array_pointer] = None
        self.dq_array_pointer = (self.dq_array_pointer + 1) % self.array_size
        self.amount -= 1
        if (self.amount < self.array_size * 1/4):
            self.decrease_size()
        print(self.queue)
        return string_item

    def resize(self):
        self.array_size *= 2
        new_queue = numpy.empty(self.array_size, object)
        for index, string in enumerate(self.queue):
            new_queue[index] = string
        self.queue = new_queue

    def decrease_size(self):
        self.array_size = self.array_size // 2
        new_queue = numpy.empty(self.array_size, object)

        i = self.dq_array_pointer
        j =0
        while (self.queue[i] != None and i < len(self.queue)):
            new_queue[j] = self.queue[i]
            i += 1
            j += 1

        self.array_pointer = j
        self.queue = new_queue
        self.dq_array_pointer = 0;



# queue = ResizingArrayQueueOfStrings(5)
#
# queue.enqueue("first")
# queue.enqueue("second")
# queue.dequeue()
# queue.enqueue("third")
# queue.dequeue()




#1.3.15

"""use queue to find the kth from last item"""

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None

    def enqueue(self, item):
        new_node = self.Node(item)
        print("the new node!", item)
        if self.last != None:
            self.last.next = new_node
        self.last = new_node
        if self.first == None:
            self.first = new_node
        self.size += 1

    def dequeue(self):
        item = self.first.item
        self.first = first.next
        if self.first == None:
            self.last = None
        print("the item", item)
        self.size -= 1
        return item




class PrintK:

    def __init__(self):
        self.k = input("enter value")
        self.stringStack = list(input("enter strings").split())
        self.queue = Queue()

        print("the string stack", self.stringStack)
        for user_string in self.stringStack:
            self.queue.enqueue(user_string)

        values_to_traverse = self.queue.size - int(self.k)

        node = self.queue.first
        i = 1
        while(i<= values_to_traverse):
            node = node.next
            i +=1

        item = node.item

        print("the retrieved item", item)


#kth_item = PrintK()


#1.3.16



class ReadAllDates:

    def __init__(self):

        self.dateStack = list(input("enter dates").split())
        self.queue = Queue()

        print("the string stack", self.dateStack)
        for date_string in self.dateStack:
            self.queue.enqueue(self.Date(date_string))


        node = self.queue.first
        dates_array = numpy.empty(self.queue.size, object)
        i = 0
        while(node != None):
            dates_array[i] = node.item.getDate()
            node = node.next
            i += 1




        print("the dates", dates_array)

    class Date:
        def __init__(self, date):
            times = date.split("/")
            self.month = times[0]
            self.day = times[1]
            self.year = times[2]

        def getDate(self):
            return self.month + "-" + self.day + "-" + self.year



#date = ReadAllDates()
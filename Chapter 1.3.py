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
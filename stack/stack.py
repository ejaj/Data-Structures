#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : stack.py
@Time : 4/17/22 11:59 AM
@Desc: 
"""


# Function Base
def create_stack():
    stack = []
    return stack


def check_empty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)


def pop(stack):
    if check_empty(stack):
        return "Stack is empty"
    return stack.pop()


# Class Base
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        return item

    def is_empty(self):
        return len(self.stack) == 0

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]


def main():
    # stack = create_stack()
    # push(stack, str(1))
    # push(stack, str(2))
    # push(stack, str(3))
    # push(stack, str(4))
    # print("popped item: " + pop(stack))
    # print("stack after popping an element: " + str(stack))

    stack = Stack()
    print(stack.is_empty())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(stack.is_empty())
    print(stack.peek())
    stack.pop()
    print(stack.peek())
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    print(stack.is_empty())


if __name__ == '__main__':
    main()

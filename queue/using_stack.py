#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : using_stack.py
@Time : 4/17/22 10:44 PM
@Desc: 
"""
from collections import deque


# Using two stack

# Method 1
class Queue:
    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()

    def enqueue(self, data):
        """
        Add item to the queue
        :param data:
        :return:
        """
        while len(self.s1):
            self.s2.append(self.s1.pop())
        self.s1.append(data)
        while len(self.s2):
            self.s1.append(self.s2.pop())

    def dequeue(self):
        if not self.s1:
            print('Underflow!!')
            exit(0)
        return self.s1.pop()


# Method 2
class Queue1:
    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()

    def enqueue(self, data):
        self.s1.append(data)

    def dequeue(self):
        if not self.s1 and not self.s2:
            print('Underflow!!')
            exit(0)
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()


# Using one stack with call stack
class Queue2:
    s = deque()

    def __init__(self):
        self.s = deque()

    def enqueue(self, data):
        self.s.append(data)

    def dequeue(self):
        if not self.s:
            print('Underflow!!')
            exit(0)
        top = self.s.pop()
        if not self.s:
            return top
        item = self.dequeue()
        self.s.append(item)
        return item


def main():
    # keys = [1, 2, 3, 4, 5]
    # q = Queue()
    # for key in keys:
    #     q.enqueue(key)
    # print(q.dequeue())
    # print(q.dequeue())

    # keys = [1, 2, 3, 4, 5]
    # q = Queue1()
    # for key in keys:
    #     q.enqueue(key)
    # print(q.dequeue())
    # print(q.dequeue())

    keys = [1, 2, 3, 4, 5]
    q = Queue2()
    for key in keys:
        q.enqueue(key)
    print(q.dequeue())
    print(q.dequeue())


if __name__ == '__main__':
    main()

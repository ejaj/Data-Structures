#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : basic.py
@Time : 4/17/22 4:04 PM
@Desc: 
"""


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)


def main():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.display()
    q.dequeue()
    print("After removing an element")
    q.display()


if __name__ == '__main__':
    main()

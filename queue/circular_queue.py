#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : circular_queue.py
@Time : 4/17/22 4:23 PM
@Desc: 
"""


class CircularQueue:
    """
    A Circular Queue Class
    """

    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.front = self.rear = -1

    def enqueue(self, data):
        """
        Add element
        :param data:
        :return:
        """
        if (self.rear + 1) % self.k == self.front:
            print("The circular queue is full\n")
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data

    def dequeue(self):
        """
        Remove element
        :return:
        """
        if self.front == -1:
            print("The circular queue is empty\n")
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.k
            return temp

    def print_queue(self):
        """
        Print queue
        :return:
        """
        if self.front == -1:
            print("No element in the circular queue")
        elif self.rear >= self.front:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.front, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
            print()


def main():
    obj = CircularQueue(5)
    obj.enqueue(1)
    obj.enqueue(2)
    obj.enqueue(3)
    obj.enqueue(4)
    obj.enqueue(5)
    print("Initial queue")
    obj.print_queue()
    obj.dequeue()
    print("After removing an element from the queue")
    obj.print_queue()


if __name__ == '__main__':
    main()

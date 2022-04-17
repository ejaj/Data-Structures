#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : priority_queue_link_list.py
@Time : 4/17/22 10:02 PM
@Desc: 
"""


class PriorityQueueNode:
    """
    A Class for Priority Queue Node
    """

    def __init__(self, data, pr):
        self.data = data
        self.priority = pr
        self.next = None


class PriorityQueue:
    """
    A class for Priority Queue
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        """
        Check Queue is empty
        :return:
        """
        return True if self.head is None else False

    def push(self, value, priority):
        """
        Insert a node
        :param value:
        :param priority:
        :return:
        """
        if self.is_empty():
            self.head = PriorityQueueNode(value, priority)
            return 1
        else:
            if self.head.priority > priority:
                new_node = PriorityQueueNode(value, priority)
                new_node.next = self.head
                self.head = new_node
                return 1
            else:
                current = self.head
                while current is not None:
                    if priority < current.next.priority:
                        break
                    current = current.next
                new_node = PriorityQueueNode(value, priority)
                new_node.next = current.next
                current.next = new_node
                return 1

    def pop(self):
        """
        Pop/remove a node
        :return:
        """
        if self.is_empty():
            return
        else:
            self.head = self.head.next
            return 1

    def peek(self):
        """
        Peek a node
        :return:
        """
        if self.is_empty():
            return
        else:
            return self.head.data

    def traverse(self):
        """
        Traverse node
        :return:
        """
        if self.is_empty():
            return "Queue is empty"
        else:
            current = self.head
            while current:
                print(current.data, end=" ")
                current = current.next


def main():
    """
    Main function for drive code
    :return:
    """
    pq = PriorityQueue()
    pq.push(4, 1)
    pq.push(5, 2)
    pq.push(6, 3)
    pq.push(7, 0)
    pq.traverse()
    pq.pop()


if __name__ == '__main__':
    main()

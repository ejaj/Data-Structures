#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : stack_linked_list.py
@Time : 4/17/22 2:58 PM
@Desc: 
"""


class Node:
    """
    A node class
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    """
    A Stack Class
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        """
        Empty stack check
        :return:
        """
        if self.head == None:
            return True
        else:
            return False

    def push(self, data):
        """
        Insert node at the begging
        :param data:
        :return:
        """
        if self.head == None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        """
        Pop a node value
        :return:
        """
        if self.is_empty():
            return None
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            return popped_node.data

    def peek(self):
        """
        Peak a node value
        :return:
        """
        if self.is_empty():
            return None
        else:
            return self.head.data

    def display(self):
        """
        Display node value
        :return:
        """
        current = self.head
        if self.is_empty():
            return "Stack Underflow"
        else:
            while current is not None:
                print(current.data, "->", end=" ")
                current = current.next

            return


def main():
    my_stack = Stack()
    my_stack.push(11)
    my_stack.push(22)
    my_stack.push(33)
    my_stack.push(44)
    my_stack.display()
    print("\nTop element is ", my_stack.peek())
    my_stack.pop()
    my_stack.pop()
    my_stack.display()
    print("\nTop element is ", my_stack.peek())


if __name__ == '__main__':
    main()

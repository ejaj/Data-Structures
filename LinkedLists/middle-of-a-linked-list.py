#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : middle-of-a-linked-list.py
@Time : 5/20/22 11:23 AM
@Desc: 
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_middle_by_count(self):
        total_node = 0
        temp = self.head
        while temp:
            temp = temp.next
            total_node = total_node + 1
        temp = self.head
        mid = 0
        while mid < total_node // 2:
            temp = temp.next
            mid = mid + 1
        print(temp.data)

    def print_middle_by_update_mid(self):
        count = 0
        head = self.head
        mid = self.head
        while head:
            if count & 1:
                mid = mid.next
            count = count + 1
            head = head.next
        print(mid.data)

    def print_middle_by_tow_pointers(self):
        fast = self.head
        slow = self.head
        if self.head is not None:
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

        print(slow.data)


list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.push(1)
# list1.print_middle_by_count()
# print(list1.print_middle_by_update_mid())
print(list1.print_middle_by_tow_pointers())

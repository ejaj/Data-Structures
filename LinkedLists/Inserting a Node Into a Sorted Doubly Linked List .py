import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def sortedInsert(head, data):

    node = DoublyLinkedListNode(data)

    if head == None:
        head = node

    elif data < head.data:
        node.next = head
        head.prev = node
        head = node
    else:
        cur = head
        while cur.next != None and cur.data < data:
            cur = cur.next

        if cur.next == None and cur.data<data:
            cur.next = node
            node.prev = cur
        else:
            previous = cur.prev
            previous.next = node
            node.prev = previous
            node.next = cur
            cur.next = node
    return head

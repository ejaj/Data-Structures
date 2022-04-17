#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : deque.py
@Time : 4/17/22 11:07 PM
@Desc: 
"""


class Deque:
    """
    A class for Deque
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        """
        Check queue is empty
        :return:
        """
        return self.items == []

    def add_rear(self, item):
        """
        Add item from rear
        :param item:
        :return:
        """
        self.items.append(item)

    def add_front(self, item):
        """
        Add item from front
        :param item:
        :return:
        """
        self.items.insert(0, item)

    def remove_front(self):
        """
        Remove item from front
        :return:
        """
        return self.items.pop(0)

    def remove_rear(self):
        """
        Remove item from rear
        :return:
        """
        return self.items.pop()

    def size(self):
        """
        Get the size of queue
        :return:
        """
        return len(self.items)


def main():
    """
    Main function for drive code
    :return:
    """
    d = Deque()
    print(d.is_empty())
    d.add_rear(8)
    d.add_rear(5)
    d.add_front(7)
    d.add_front(10)
    print(d.size())
    print(d.is_empty())
    d.add_rear(11)
    print(d.remove_rear())
    print(d.remove_front())
    d.add_front(55)
    d.add_rear(45)
    print(d.items)


if __name__ == '__main__':
    main()

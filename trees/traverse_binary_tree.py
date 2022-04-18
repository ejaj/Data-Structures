#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : traverse_binary_tree.py
@Time : 4/18/22 11:48 AM
@Desc: 
"""


class Node:
    """
    A Tree Class
    """

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def traverse_in_order(self):
        """
        In order traverse
        :return:
        """
        if self.left:
            self.left.traverse_in_order()
        print(self.value, end=' ')
        if self.right:
            self.right.traverse_in_order()

    def traverse_pre_order(self):
        """
        Pre order traverse
        :return:
        """
        print(self.value, end=' ')
        if self.left:
            self.left.traverse_pre_order()
        if self.right:
            self.right.traverse_pre_order()

    def traverse_post_order(self):
        """
        Post order traverse
        :return:
        """
        if self.left:
            self.left.traverse_post_order()
        if self.right:
            self.right.traverse_post_order()
        print(self.value, end=' ')


def insert(temp, key):
    """
    Insert value
    :param temp:
    :param key:
    :return:
    """
    if not temp:
        root = Node(key)
        return
    q = [temp]
    while len(q):
        temp = q[0]
        q.pop(0)

        if not temp.left:
            temp.left = Node(key)
            break
        else:
            q.append(temp.left)

        if not temp.right:
            temp.right = Node(key)
            break
        else:
            q.append(temp.right)


def main():
    """
    Main function for drive code
    :return:
    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    print("\nIn order Traversal: ", end="")
    root.traverse_in_order()
    print("\nPre order Traversal: ", end="")
    root.traverse_pre_order()
    print("\nPost order Traversal: ", end="")
    root.traverse_post_order()
    insert(root, 5)
    print("\nIn order Traversal After insert: ", end="")
    root.traverse_in_order()


if __name__ == '__main__':
    main()

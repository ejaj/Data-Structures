#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : perfect_binary_tree.py
@Time : 4/18/22 1:54 PM
@Desc: 
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def calculate_depth(node):
    d = 0
    while node is not None:
        d += 1
        node = node.left
    return d


def is_perfect(root, d, level=0):
    if root is None:
        return True

    if root.left is None and root.right is None:
        return d == level + 1
    return is_perfect(root.left, d, level + 1) and is_perfect(root.right, d, level + 1)


def main():
    root = None
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    if is_perfect(root, calculate_depth(root)):
        print("The tree is a perfect binary tree")
    else:
        print("The tree is not a perfect binary tree")


if __name__ == '__main__':
    main()

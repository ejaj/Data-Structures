#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : complete_binary_tree.py
@Time : 4/18/22 2:25 PM
@Desc: 
"""


class Node:

    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


def is_complete(root, index, number_nodes):
    if root is None:
        return True

    if index >= number_nodes:
        return False
    return (is_complete(root.left, 2 * index + 1, number_nodes)
            and is_complete(root.right, 2 * index + 2, number_nodes))


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    node_count = count_nodes(root)
    index = 0
    if is_complete(root, index, node_count):
        print("The tree is a complete binary tree")
    else:
        print("The tree is not a complete binary tree")


if __name__ == '__main__':
    main()

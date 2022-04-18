#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : full_binary_tree.py
@Time : 4/18/22 1:26 PM
@Desc: 
"""


class Node:
    """
    A Tree Class
    """

    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


def is_full_tree(root):
    """
    Check Tree is full binary tree¬
    :param root:
    :return:
    """
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    if root.left is not None and root.right is not None:
        return is_full_tree(root.left) and is_full_tree(root.right)
    return False


def main():
    """
    Main function for drive code
    :return:
    """
    root = Node(1)
    root.right = Node(3)
    root.left = Node(2)

    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.left = Node(6)
    root.left.right.left = Node(7)

    if is_full_tree(root):
        print("The tree is a full binary tree")
    else:
        print("The tree is not a full binary tree")


if __name__ == '__main__':
    main()

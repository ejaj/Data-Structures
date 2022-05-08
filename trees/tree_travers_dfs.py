#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : tree_travers_dfs.py
@Time : 5/8/22 10:32 PM
@Desc:
Time Complexity: O(n)
Auxiliary Space: If we don’t consider size of stack for function calls then O(1) otherwise O(n).
"""


class Node:
    """
    A Class node
    """

    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def print_in_order(root):
    """
    Print tree values in order process.
    Flow below three steps:
        1. First recur on left child
        2. Then print the data of node
        3. Now recur on right child

    :param root:
    :return:
    """
    if root:
        print_in_order(root.left)
        print(root.val),
        print_in_order(root.right)


def print_post_order(root):
    """
    Print tree values post order process.
    Flow below three steps:
        1. First recur on left child
        2. Then, the recur on right child
        3. Now print the data of node
    :param root:
    :return:
    """
    if root:
        print_post_order(root.left)
        print_post_order(root.right)
        print(root.val),


def print_pre_order(root):
    """
    Print tree values post order process.
    Flow below three steps:
        1. First print the data of node
        2. Then recur on left child
        3. Finally recur on right child
    :param root:
    :return:
    """
    if root:
        print(root.val),
        print_pre_order(root.left)
        print_pre_order(root.right)


def main():
    """
    Main function for drive code.
    :return:
    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Preorder traversal of binary tree is")
    print_pre_order(root)

    print("\nInorder traversal of binary tree is")
    print_in_order(root)

    print("\nPostorder traversal of binary tree is")
    print_post_order(root)


if __name__ == '__main__':
    main()

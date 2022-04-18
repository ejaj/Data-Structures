#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : balanced_binary_tree.py
@Time : 4/18/22 2:53 PM
@Desc: 
"""


class Node:
    """
    A Tree Class
    """

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Height:
    """
    A Height Class
    """

    def __init__(self):
        self.height = 0


def is_height_balanced(root, height):
    """
    Check Tree is balanced binary tree
    :param root:
    :param height:
    :return:
    """
    left_height = Height()
    right_height = Height()
    if root is None:
        return True
    l = is_height_balanced(root.left, left_height)
    r = is_height_balanced(root.right, right_height)
    height.height = max(left_height.height, right_height.height) + 1
    if abs(left_height.height - right_height.height) <= 1:
        return l and r

    return False


def main():
    height = Height()

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    if is_height_balanced(root, height):
        print('The tree is balanced')
    else:
        print('The tree is not balanced')


if __name__ == '__main__':
    main()

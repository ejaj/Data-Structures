#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : traverse_ways.py
@Time : 4/18/22 11:50 AM
@Desc:
Tree:
     1
    / \
    2  3
   / \
  4   5
Inorder traversal:
    1. First, visit all the nodes in the left subtree
    2. Then the root node
    3. Visit all the nodes in the right subtree
    i.e: 4 -> 2 -> 5 -> 1 -> 3
    inorder(root->left)
    print(root->data)
    inorder(root->right)

Preorder traversal:
    1. Visit root node
    2. Visit all the nodes in the left subtree
    3. Visit all the nodes in the right subtree
    i.e: 1 -> 2 -> 4 -> 5 -> 3
    print(root->data)
    preorder(root->left)
    preorder(root->right)

Postorder traversal:
    1. Visit all the nodes in the left subtree
    2. Visit all the nodes in the right subtree
    3. Visit the root node
    i.e: 4 -> 5 -> 2 -> 3 -> 1
    postorder(root->left)
    postorder(root->right)
    print(root->data)

"""


class Node:
    """
    A Tree class
    """

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def in_order(root):
    """
    Inorder traversal
    :param root:
    :return:
    """
    if root:
        in_order(root.left)
        print(str(root.value) + "->", end='')
        in_order(root.right)


def pre_order(root):
    """
    Preorder traversal
    :param root:
    :return:
    """
    if root:
        print(str(root.value) + "->", end='')
        pre_order(root.left)
        pre_order(root.right)


def post_order(root):
    """
    Postorder traversal
    :param root:
    :return:
    """
    if root:
        post_order(root.left)
        post_order(root.right)
        print(str(root.value) + "->", end='')


def main():
    """
    Main function for drive code
    :return:
    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Inorder traversal ")
    in_order(root)

    print("\nPreorder traversal ")
    pre_order(root)

    print("\nPostorder traversal ")
    post_order(root)


if __name__ == '__main__':
    main()

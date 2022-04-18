#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : basic_binary_tree.py
@Time : 4/18/22 11:38 AM
@Desc: 
"""


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def main():
    root = Node(1)
    ''' following is the tree after above statement
            1
          /   \
         None  None'''

    root.left = Node(2)
    root.right = Node(3)

    ''' 2 and 3 become left and right children of 1
               1
             /   \
            2      3
         /    \    /  \
       None None None None'''

    root.left.left = Node(4)
    '''4 becomes left child of 2
               1
           /       \
          2          3
        /   \       /  \
       4    None  None  None
      /  \
    None None'''


if __name__ == '__main__':
    main()

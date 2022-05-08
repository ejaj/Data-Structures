#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : valid_bst.py
@Time : 5/8/22 11:05 PM
@Desc:
Input: [2,1,3]
Output: True
 2
/\
1 3
"""

from typing import Optional

import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.track = -sys.maxsize - 1

    def is_valid_bst(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if not self.is_valid_bst(root.left):
            return False
        if root.val <= self.track:
            return False
        self.track = root.val
        if not self.is_valid_bst(root.right):
            return False
        return True

    def is_valid_bst_inorder(self, root: TreeNode) -> bool:
        if not root:
            return True
        def in_order(root, order):
            if root is None:
                return
            in_order(root.left, order)
            order.append(root.val)
            in_order(root.right, order)

        order = []
        in_order(root, order)
        for i in range(1, len(order)):
            if order[i] <= order[i - 1]:
                return False
        return True

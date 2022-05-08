#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : valid_bst_2.py
@Time : 5/8/22 11:16 PM
@Desc: 
"""


class Solution(object):
    def is_valid_bst(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, float('-inf'), float('inf'))

    def helper(self, node, low, high):
        if node is None:
            return True

        if node.val <= low or node.val >= high:
            return False

        return self.helper(node.left, low, node.val) and self.helper(node.right, node.val, high)

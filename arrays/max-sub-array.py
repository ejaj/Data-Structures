#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : max-sub-array.py
@Time : 4/11/22 3:13 PM
@Desc: 
"""
from typing import List
from sys import maxsize

'''
Input:
    nums = [-2,1,-3,4,-1,2,1,-5,4]
Output:
    result = 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''


def max_sub_array(nums: List[int]) -> int:
    """
    Max sub array, using DP
    Time Complexity: O(n)
    :param nums:
    :return:
    """
    max_sum = total_sum = nums[0]
    for i in range(1, len(nums)):
        total_sum = max(nums[i], total_sum + nums[i])
        max_sum = max(max_sum, total_sum)
    return max_sum


def max_sub_array1(nums: List[int]) -> int:
    """
    Max sub array, using LOOP
    Time Complexity: O(n)
    :param nums:
    :return:
    """
    max_sum = -maxsize - 1
    total_sum = 0
    for i in range(len(nums)):
        total_sum = total_sum + nums[i]
        if max_sum < total_sum:
            max_sum = total_sum
        if total_sum < 0:
            total_sum = 0
    return max_sum


def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_sub_array(nums))
    print(max_sub_array1(nums))


if __name__ == '__main__':
    main()

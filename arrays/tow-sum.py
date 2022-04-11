#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : tow-sum.py
@Time : 4/11/22 2:42 PM
@Desc: 
"""
from typing import List

'''
Input:
    nums = [2,7,11,15]
    target = 9
Output:
    results = [0,1]
'''


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Two sum, using loop (brute force approach)
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    :param nums:
    :param target:
    :return:
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def two_sum_1(nums: List[int], target: int) -> List[int]:
    """
    Two sum, using dictionary/hasmap approach
    Time Complexity: O(n)
    Space Complexity: O(n)
    :param nums:
    :param target:
    :return:
    """
    values = {}
    for i, value in enumerate(nums):
        diff = target - value
        if diff in values:
            return [values[diff], i]
        values[value] = i
    return []


def main():
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))
    print(two_sum_1(nums, target))


if __name__ == '__main__':
    main()

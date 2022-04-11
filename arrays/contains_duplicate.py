#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : contains_duplicate.py
@Time : 4/11/22 4:21 PM
@Desc: 
"""
from typing import List

'''
Input: 
    nums = [1,2,3,1]
Output: 
    true
Input: 
    nums = [1,2,3,4]
Output: 
    false
'''


def contains_duplicate(nums: List[int]) -> bool:
    """
    Check Duplicate list value, using brute force approach
    :param nums:
    :return:
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


def contains_duplicate_1(nums: List[int]) -> bool:
    """
    Check Duplicate list value, using set method
    :param nums:
    :return:
    """
    return len(nums) != len(set(nums))


def contains_duplicate_2(nums: List[int]) -> bool:
    """
    Check Duplicate list value, using HashMap/Dictionary/Set
    :param nums:
    :return:
    """
    # stack = set()
    # for n in nums:
    #     if n in stack:
    #         return True
    #     else:
    #         stack.add(n)
    #
    # return False

    dic = {}
    for n in nums:
        if n in dic:
            return True
        else:
            dic[n] = 1
    return False


def main():
    nums = [1, 2, 3, 1]
    print(contains_duplicate(nums))
    print(contains_duplicate_1(nums))
    print(contains_duplicate_2(nums))


if __name__ == '__main__':
    main()

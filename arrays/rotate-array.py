#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : rotate-array.py
@Time : 4/11/22 4:51 PM
@Desc: 
"""
'''
Input: 
    nums = [1,2,3,4,5,6,7]
    k = 3
Output: 
    [5,6,7,1,2,3,4]
Explanation:
    rotate 1 steps to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]
    rotate 3 steps to the right: [5,6,7,1,2,3,4]
'''


def array_rotate(nums, k):
    """
    Rotate an array, using temp array
    :param nums:
    :param k:
    :return:
    """
    temp = []
    i = 0
    while i < k:
        temp.append(nums[i])
        i += 1
    i = 0
    while k < len(nums):
        nums[i] = nums[k]
        i += 1
        k += 1

    nums[:] = nums[:i] + temp
    return nums


def array_rotate_1(nums, k):
    """
    Rotate an array, using List
    :param nums:
    :param k:
    :return:
    """
    nums[:] = nums[k:len(nums)] + nums[0:k]
    return nums


def left_rotate_by_one(nums):
    temp = nums[0]
    for i in range(len(nums) - 1):
        nums[i] = nums[i + 1]
    nums[len(nums) - 1] = temp


def array_rotate_2(nums, k):
    for i in range(k):
        left_rotate_by_one(nums)
    return nums


def main():
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    # print(array_rotate(nums, k))
    # print(array_rotate_1(nums, k))
    print(array_rotate_2(nums, k))


if __name__ == '__main__':
    main()

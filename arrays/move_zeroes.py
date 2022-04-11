#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : move_zeroes.py
@Time : 4/11/22 3:43 PM
@Desc: 
"""
'''
Input:
    nums = [0, 1, 0, 3, 12]
Output:
    [1,3,12,0,o]
'''


def move_zeroes(nums):
    """
    :param nums:
    :return:
    """
    none_zero = []
    zeroes = []
    for i in range(len(nums)):
        if nums[i] == 0:
            zeroes.append(nums[i])
        else:
            none_zero.append(nums[i])
    none_zero.extend(zeroes)
    return none_zero


def move_zeroes_1(nums):
    """
    Time Complexity: O(n)
    :param nums:
    :return:
    """
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1

    while j < len(nums):
        nums[j] = 0
        j += 1
    return nums


def move_zeroes_2(nums):
    """
    Swapping approach
    :param nums:
    :return:
    """
    pos = 0
    for i in range(len(nums)):
        if nums[i]:
            nums[i], nums[pos] = nums[pos], nums[i]
            pos += 1
    return nums


def main():
    nums = [0, 1, 0, 3, 12]
    # print(move_zeroes(nums))
    # print(move_zeroes_1(nums))
    print(move_zeroes_2(nums))


if __name__ == '__main__':
    main()

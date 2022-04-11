#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : target_sum.py
@Time : 4/11/22 12:35 AM
@Desc: 
"""
'''
arr = [1, 3, 4, 5]
target = 7
output = True, if the target found for any pair of array sum, otherwise False
'''


def pair_sum(arr, target):
    """
    Sum each pair, using brute force approach
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    :param arr:
    :param target:
    :return:
    """
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return True
    return False


def pair_sum1(arr, target):
    """
    Sum each pair, using dictionary/hasmap approach
    Time Complexity: O(n+n)
    Space Complexity: O(n)
    :param arr:
    :param target:
    :return:
    """
    values = dict()
    for i, value in enumerate(arr):
        target_sub = target - arr[i]
        if target_sub in values:
            return True
        values[value] = i
    return False


def main():
    arr = [1, 3, 4, 5]
    target = 7
    print(pair_sum(arr, target))
    print(pair_sum1(arr, target))


if __name__ == '__main__':
    main()

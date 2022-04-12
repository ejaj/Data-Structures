#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : first_repeating.py
@Time : 4/12/22 1:22 PM
@Desc: 
"""
'''
Input:
    arr =  [2, 5, 1, 2, 4, 5, 3]
Output:
    result = 2
Input:
    arr =  [2, 1, 1, 2, 3, 5, 3]
Output:
    result = 1
Input:
    arr =  [2, 3, 4, 5]
Output:
    result = None
'''


def first_repeating(arr):
    """
    First Repeating, using brute force approach
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    :param arr:
    :return:
    """
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return arr[j]
    return None


def first_repeating_1(arr):
    """
    First Repeating, using set/hasmap
    Time Complexity: O(n)
    Space Complexity: O(1)
    :param arr:
    :return:
    """
    seen = set()
    for i in arr:
        if i in seen:
            return i
        seen.add(i)
    return None


def main():
    """
    Main function for drive code
    :return:
    """
    arr = [2, 5, 1, 2, 4, 5]
    print(first_repeating(arr))
    print(first_repeating_1(arr))


if __name__ == '__main__':
    main()

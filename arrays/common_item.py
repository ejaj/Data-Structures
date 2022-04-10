#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : common_items.py
@Time : 4/10/22 10:53 PM
@Desc: 
"""

'''
arr = ['a', 'b', 'c', 'x']
arr1 = ['d','e', 'x']
output = true if match at least one value, otherwise false
arr = ['a', 'b', 'c', 'x']
arr1 = ['d','e', 'y']
output = true if match at least one value, otherwise false
'''
import itertools


# brute force approach
def contain_common_item(arr, arr1):
    """
    Check common item, using brute force approach
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    :param arr:
    :param arr1:
    :return:
    """
    for i in range(len(arr)):
        for j in range(len(arr1)):
            if arr[i] == arr1[j]:
                return True
    return False


def contain_common_item2(arr, arr2):
    """
    Check common item, using dictionary/hasmap approach
    Time Complexity: O(n+n)
    Space Complexity: O(n)
    :param arr:
    :param arr2:
    :return:
    """
    values = {}
    for i in range(len(arr)):
        if arr[i] not in values:
            values[arr[i]] = True
    for j in range(len(arr2)):
        if arr2[j] in values:
            return True
    return False


def contain_common_item3(arr, arr1):
    """
    Check common item, using itertools built-in-function approach.
    Time Complexity: O(m*n)
    :param arr: 
    :param arr1: 
    :return: 
    """
    for arr_val, arr1_val in itertools.product(arr, arr1):
        if arr_val == arr1_val:
            return True
    return False


def main():
    arr = ['a', 'b', 'c', 'x']
    arr1 = ['d', 'e', 'x']
    print (contain_common_item(arr, arr1))
    print (contain_common_item2(arr, arr1))
    print(contain_common_item3(arr, arr1))


if __name__ == '__main__':
    main()

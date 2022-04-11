#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : merged_sorted_array.py
@Time : 4/11/22 2:02 PM
@Desc: 
"""
'''
Input:
    arr1 = [2, 3, 4, 31]
    arr2 = [4, 6, 30]
Output:
    results = [2,3,4,4,30,31]
'''


def merged_sorted_array(arr1, arr2):
    """
    Time Complexity : O(n1 + n2)
    Auxiliary Space : O(n1 + n2)
    :param arr1:
    :param arr2:
    :return:
    """
    if not arr1:
        return arr2
    if not arr2:
        return arr1
    merged_array = [None] * (len(arr1) + len(arr2))
    i, j, k = 0, 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array[k] = arr1[i]
            i += 1
            k += 1
        else:
            merged_array[k] = arr2[j]
            j += 1
            k += 1
    while i < len(arr1):
        merged_array[k] = arr1[i]
        k += 1
        i += 1
    while j < len(arr2):
        merged_array[k] = arr1[j]
        k += 1
        j += 1
    return merged_array


def main():
    arr1 = [2, 3, 4, 31]
    arr2 = [4, 6, 30]

    print(merged_sorted_array(arr1, arr2))


if __name__ == '__main__':
    main()

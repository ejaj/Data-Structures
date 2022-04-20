#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : duplicate_zeros.py
@Time : 4/20/22 2:18 PM
@Desc:
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
"""

from typing import List


def duplicate_zeros(arr: List[int]) -> List:
    """
    Do not return anything, modify arr in-place instead.
    """
    start = 0
    end = len(arr) - 1
    while start < end:
        if arr[start] == 0:
            arr.insert(start, 0)
            start += 1
            arr.pop()
        start += 1
    return arr


def main():
    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    print(arr)


if __name__ == '__main__':
    main()

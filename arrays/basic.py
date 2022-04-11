#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : basic.py
@Time : 4/11/22 2:20 AM
@Desc: 
"""

arr = ["a", "b", "c"]
arr.append('d')  # O(1)
print(arr)
arr.pop()  # O(1)
print(arr)
arr.insert(0, "x")  # O(1)
print(arr)
print(arr[1])  # O(1)


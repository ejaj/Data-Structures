#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : space.py
@Time : 4/10/22 8:37 PM
@Desc: 
"""


def space_complexity(arr):
    for i in range(len(arr)):
        print("Space complexity")


space_complexity([1, 2, 3, 4, 5])  # O(1)


def space_complexity_1(n):
    result = []
    for i in range(n):
        result.append("hi")
    print(result)


space_complexity_1(6)  # O(n)

arr = ["science", "math", "history"]
print(arr[0])  # O(1)
print (arr[len(arr) - 1])  # O(1)

arr1 = [
    {
        'tweet': "science",
        'date': 2012
    }, {
        'tweet': "math",
        'date': 2014
    }, {
        'tweet': "history",
        'date': 2018
    }
]

# time O(n^2)

a = "Hello"
len(a)  # time O(1)

#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : array_make.py
@Time : 4/11/22 2:45 AM
@Desc: 
"""


class MyArray:

    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)
        return self.data


new_array = MyArray()
print(new_array.push("hi"))

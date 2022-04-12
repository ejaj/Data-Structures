#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : basic.py
@Time : 4/12/22 12:50 PM
@Desc: 
"""

user = {
    'age': 590,
    'name': 'John',
    'magic': True,
    'classes': [1, 2, 3, 4, ]
}
print(user['age'])  # O(1)
user['address'] = 'Downtown'  # O(1)
print(user)
print(user.keys())
print(user.items())
print(user.values())

class DictClass:
    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        setattr(self, key, value)


name = DictClass()
name["key"] = "ejaj"
print(name["key"])

#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : fun.py
@Time : 4/10/22 5:55 PM
@Desc: 
"""


def another_function():
    pass


def fun_challenge(arr):
    """

    :param arr:
    :return:
    """
    a = 10  # O(1)
    a = 50 + 3  # O(1)
    for i in range(len(arr)):  # O(n)
        another_function()  # O(n)
        st = True  # O(n)
        a += 1  # O(n)
    return a  # 0(1)


def main():
    arr = [1, 2, 3]
    print (fun_challenge(arr))
    # Total
    # 3 + n+n+n+n = 3+4n
    # BIG O(3+4n)
    # BIG O(n)


if __name__ == '__main__':
    main()

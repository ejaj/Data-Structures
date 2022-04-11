#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : reverse.py
@Time : 4/11/22 3:21 AM
@Desc: 
"""


def reverse(s):
    """
    Reverse String, using loop
    Time Complexity: O(n)
    Space Complexity: O(n)
    :param s:
    :return:
    """
    r_s = ""
    for i in s:
        r_s = i + r_s
    return r_s


def create_stack():
    stack = []
    return stack


def stack_size(stack):
    return len(stack)


def is_empty(stack):
    if stack_size(stack) == 0:
        return True


def push_stack(stack, item):
    stack.append(item)


def pop(stack):
    if is_empty(stack):
        return
    return stack.pop()


def reverse_1(s):
    """
    Reverse String, using stack
    :param s:
    :return:
    """
    n = len(s)
    stack = create_stack()
    for i in range(0, n, 1):
        push_stack(stack, s[i])
    s = ""
    for i in range(0, n, 1):
        s += pop(stack)
    return s


def reverse_2(s):
    """
    Reverse String, using slice
    :param s:
    :return:
    """
    s = s[::-1]
    return s


def reverse_3(s):
    """
    Reverse String, using reversed
    :param s:
    :return:
    """
    s = "".join(reversed(s))
    return s


def reverse_4(s):
    """
    Reverse String, using loop
    :param s:
    :return:
    """
    st = ""
    for i in range(len(s), -1, -1):
        st += s[i - 1]
    return st


def main():
    s = "Kazi"
    print(reverse(s))
    print(reverse_1(s))
    print(reverse_2(s))
    print(reverse_3(s))
    print(reverse_4(s))
    print(reverse_4(s))


if __name__ == '__main__':
    main()

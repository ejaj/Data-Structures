#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : longest_word.py
@Time : 4/11/22 5:36 PM
@Desc: 
"""


def find_longest_word_length(s):
    """
    :param s:
    :return:
    """
    s_split = s.split(' ')
    longest_word = 0
    for i in range(len(s_split)):
        chunk_ln = len(s_split[i])
        if chunk_ln > longest_word:
            longest_word = chunk_ln
    return longest_word


def largest_word(s):
    """
    :param s:
    :return:
    """
    l = list(s.split(" "))
    sorted_s = sorted(l, key=len)
    return sorted_s[-1]


def main():
    s = "The quick brown fox jumped over the lazy dog"
    # print(find_longest_word_length(s))
    print(largest_word(s))


if __name__ == '__main__':
    main()

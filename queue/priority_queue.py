#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : priority_queue.py
@Time : 4/17/22 7:53 PM
@Desc:
 3
/ \
4  5
----
 5
/\
4 3
"""


def heapify(arr, n, i):
    """
    Heapify
    :param arr:
    :param n:
    :param i:
    :return:
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[i] > arr[left]:
        largest = left
    if right < n and arr[i] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def insert(arr, data):
    """
    Insert node
    :param arr:
    :param data:
    :return:
    """
    size = len(arr)
    if size == 0:
        arr.append(data)
    else:
        arr.append(data)
        for i in range((size // 2) - 1, -1, -1):
            heapify(arr, size, i)


def delete_node(array, num):
    """
    Delete Node
    :param array:
    :param num:
    :return:
    """
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break

    array[i], array[size - 1] = array[size - 1], array[i]

    array.remove(size - 1)

    for i in range((len(array) // 2) - 1, -1, -1):
        heapify(array, len(array), i)


def main():
    """
    Main function for drive code
    :return:
    """
    arr = []

    insert(arr, 3)
    insert(arr, 4)
    insert(arr, 9)
    insert(arr, 5)
    insert(arr, 2)

    print("Max-Heap array: " + str(arr))

    delete_node(arr, 4)
    print("After deleting an element: " + str(arr))


if __name__ == '__main__':
    main()

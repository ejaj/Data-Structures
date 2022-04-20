#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : adjacency_matrix.py
@Time : 4/21/22 12:13 AM
@Desc: 
"""


class Graph:
    """
    A Graph Class
    """
    def __init__(self, size):
        self.adj_matrix = []
        for i in range(size):
            self.adj_matrix.append([0 for i in range(size)])
        self.size = size

    def add_edge(self, v1, v2):
        """
        Add edge to graph
        :param v1:
        :param v2:
        :return:
        """
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adj_matrix[v1][v2] = 1
        self.adj_matrix[v2][v1] = 1

    def remove_edge(self, v1, v2):
        """
        Remove edge from graph
        :param v1:
        :param v2:
        :return:
        """
        if self.adj_matrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adj_matrix[v1][v2] = 0
        self.adj_matrix[v2][v1] = 0

    def __len__(self):
        """
        :return:
        """
        return self.size

    def print_matrix(self):
        """
        Print matrix
        :return:
        """
        for row in self.adj_matrix:
            for val in row:
                print('{:4}'.format(val))
            print()


def main():
    """
    Main function for run the code
    :return:
    """
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)

    g.print_matrix()


if __name__ == '__main__':
    main()

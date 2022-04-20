#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : edge_lists.py
@Time : 4/20/22 1:02 PM
@Desc:
  2
 / \
1   3
edge_list = [[1,2] [2,3] [3,1]
"""


class Graph:
    """
    A Graph Class
    """

    def __init__(self, edge_list, num_of_nodes):
        self.adjacency_list = [[] for _ in range(num_of_nodes)]
        for origin, dest in edge_list:
            self.adjacency_list[origin].append(dest)


def print_graph(graph):
    """
    Print the graph
    :param graph:
    :return:
    """
    for origin in range(len(graph.adjacency_list)):
        for dest in graph.adjacency_list[origin]:
            print(f"{origin} —> {dest} ", end="")
        print()


def main():
    """
    Main function for run the the code
    :return:
    """
    edge_list = [(0, 1), (1, 2), (2, 3), (0, 2), (3, 2), (4, 5), (5, 4)]
    num_of_nodes = 6
    graph = Graph(edge_list, num_of_nodes)
    print_graph(graph)


if __name__ == "__main__":
    main()

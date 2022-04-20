#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : adjacency_list.py
@Time : 4/20/22 1:21 PM
@Desc: 
"""


class AdjacencyNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [None] * self.v

    def add_edge(self, src, dest):
        node = AdjacencyNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        node = AdjacencyNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def print_graph(self):
        for i in range(self.v):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


def main():
    v = 5
    graph = Graph(v)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.print_graph()


if __name__ == "__main__":
    main()

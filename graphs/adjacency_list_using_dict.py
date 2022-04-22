#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : adjacency_list_using_dict.py
@Time : 4/22/22 11:05 AM
@Desc:
graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }
"""

from collections import defaultdict

graph = defaultdict(list)


def add_edge(graph, u, v):
    """
    Add edge to graph
    :param graph:
    :param u:
    :param v:
    :return:
    """
    graph[u].append(v)


def generate_edges(graph):
    """
    Generate a graph
    :param graph:
    :return:
    """
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges


def find_path(graph, start, end, path=[]):
    """
    Find path a node
    :param graph:
    :param start:
    :param end:
    :param path:
    :return:
    """
    path = path + [start]
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            new_path = find_path(graph, node, end, path)
            if new_path:
                return new_path


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_all_paths(graph, node, end, path)
        for new_path in new_paths:
            paths.append(new_path)
    return paths


def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    shortest = None
    for node in graph[start]:
        if node not in path:
            new_path = find_shortest_path(graph, node, end, path)
            if new_path:
                if not shortest or len(new_path) < len(shortest):
                    shortest = new_path
    return shortest


def main():
    add_edge(graph, 'a', 'c')
    add_edge(graph, 'b', 'c')
    add_edge(graph, 'b', 'e')
    add_edge(graph, 'c', 'd')
    add_edge(graph, 'c', 'e')
    add_edge(graph, 'c', 'a')
    add_edge(graph, 'c', 'b')
    add_edge(graph, 'e', 'b')
    add_edge(graph, 'd', 'c')
    add_edge(graph, 'e', 'c')

    print(generate_edges(graph))
    print(find_path(graph, 'd', 'c'))
    print(find_all_paths(graph, 'd', 'c'))
    print(find_shortest_path(graph, 'd', 'c'))


if __name__ == '__main__':
    main()

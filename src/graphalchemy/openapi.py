from src.graphalchemy.weighted import create_weighted_graph
from src.graphalchemy.directed import create_directed_graph
import networkx as nx


def _shortest_path(from_vertex, to_vertex) -> list:
    graph = create_weighted_graph()
    try:
        return nx.shortest_path(graph, from_vertex, to_vertex, weight='weight')
    except BaseException:
        return 'No path exists between given points'


def shortest_path(from_vertex, to_vertex) -> list:
    """
    takes input as to and from vertex and returns shortest path between them if exists
    input: str, str
    output: list
    """
    return _shortest_path(from_vertex, to_vertex)


def _successor(of_vertex) -> list:
    graph = create_directed_graph()
    try:
        return list(graph.successors(of_vertex))
    except BaseException:
        return 'No successor'


def successor(of_vertex) -> list:
    """
    takes input as to vertex and returns successor value
    input: str
    output: list
    """
    return _successor(of_vertex)


def _intersection(G, H) -> nx.Graph():
    try:
        return nx.intersection(G, H)
    except BaseException:
        return 'Exception creating intersection, both graphs must have same node set'


def intersection(G, H) -> nx.Graph():
    """
    takes input as two graphs and returns intersection graph
    input: Graph object, Graph object
    output: Graph object
    """
    return _intersection(G, H)


def _union(G, H) -> nx.Graph():
    try:
        return nx.union(G, H)
    except BaseException:
        return 'Specified graph must be disjoint'


def union(G, H) -> nx.Graph():
    """
    takes input as two graphs and returns union graph
    input: Graph object, Graph object
    output: Graph object
    """
    return _union(G, H)


def _difference(G, H) -> nx.Graph():
    try:
        return nx.difference(G, H)
    except BaseException:
        return 'Specified graph must be disjoint'


def difference(G, H) -> nx.Graph():
    """
    takes input as two graphs and returns difference of those two graphs
    input: Graph object, Graph object
    output: Graph object
    """
    return _difference(G, H)
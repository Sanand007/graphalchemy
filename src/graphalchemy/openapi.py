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
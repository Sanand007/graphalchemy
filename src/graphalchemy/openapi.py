from src.graphalchemy.weighted import create_weighted_graph
import networkx as nx


def _shortest_path(from_vertex, to_vertex):
    graph = create_weighted_graph()
    return nx.shortest_path(graph, from_vertex, to_vertex, weight='weight')


def shortest_path(from_vertex, to_vertex):
    return _shortest_path(from_vertex, to_vertex)
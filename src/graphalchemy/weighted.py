from src.graphalchemy.read_dbcfg import read_config
from src.graphalchemy.read_data import read_weighted_data
import networkx as nx


def _create_weighted_graph() -> nx.Graph():
    config = read_config()
    graph_data = read_weighted_data(config['database']['postgres']['table']['weighted'])
    G = nx.Graph();
    for connection in graph_data:
        G.add_edge(connection[1], connection[2], weight=connection[3])
    return G


def create_weighted_graph() -> nx.Graph():
    """
    create a networkx graph with weighted data and returns the graph object
    """
    return _create_weighted_graph()

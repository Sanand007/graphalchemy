from src.graphalchemy.read_dbcfg import read_config
from src.graphalchemy.read_data import read_directed_data
import networkx as nx


def _create_directed_graph() -> nx.Graph():
    config = read_config()
    graph_data = read_directed_data(config['database']['postgres']['table']['directed'])
    G = nx.DiGraph();
    for connection in graph_data:
        G.add_weighted_edges_from([(connection[1], connection[2], connection[3])])
    return G


def create_directed_graph() -> nx.Graph():
    """
    create a networkx graph with weighted data and returns the graph object
    """
    return _create_directed_graph()

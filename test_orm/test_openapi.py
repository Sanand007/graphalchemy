from src.graphalchemy.openapi import shortest_path, successor, intersection, union, difference
import networkx as nx


def test_shortest_path_b_f_pass():
    path = shortest_path('b', 'f')
    assert path == ['b', 'c', 'f']


def test_shortest_path_d_a_fail():
    path = shortest_path('d', 'a')
    assert path != ['b', 'c', 'f']


def test_shortest_path_d_a_pass():
    path = shortest_path('d', 'a')
    assert path == ['d', 'b', 'a']


def test_successor_b():
    next = successor('b')
    assert next == ['a', 'c']


def test_successor_c():
    next = successor('c')
    assert next == ['f']


def test_successor_d():
    next = successor('d')
    assert next == ['c', 'b']


def test_intersection():
    G = nx.Graph()
    G.add_node(1)
    G.add_node(2)
    G.add_node(3)
    G.add_edge(1, 2)
    G.add_edge(2, 3)

    H = nx.Graph()
    H.add_node(1)
    H.add_node(2)
    H.add_node(3)
    H.add_edge(2, 3)

    V = intersection(G, H)
    assert V.number_of_edges() == 1


def test_union():
    G = nx.Graph()
    G.add_node(1)
    G.add_node(2)
    G.add_node(3)
    G.add_edge(1, 2)

    H = nx.Graph()
    H.add_node(4)
    H.add_node(5)
    H.add_node(6)
    H.add_edge(4, 5)

    V = union(G, H)
    assert V.number_of_edges() == 2


def test_difference():
    G = nx.Graph()
    G.add_node(1)
    G.add_node(2)
    G.add_node(3)
    G.add_edge(1, 2)
    G.add_edge(2, 3)

    H = nx.Graph()
    H.add_node(1)
    H.add_node(2)
    H.add_node(3)
    H.add_edge(1, 2)

    V = difference(G, H)
    assert V.number_of_edges() == 1
from src.graphalchemy.openapi import shortest_path, successor


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
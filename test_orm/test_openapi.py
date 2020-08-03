from src.graphalchemy.openapi import shortest_path, successor


def test_shortest_path():
    path = shortest_path('b', 'f')
    assert path == ['b', 'c', 'f']


def test_successor():
    next = successor('b')
    assert next == ['a', 'c']
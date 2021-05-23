import pytest

from lesson02.advanced_topics import flatten, flatten_with_reference, get_from_matrix


def test_flatten_01():
    matrix = [
        [1, 2, 3, [ 3, 4 ] ],
        [5, [ 8, [ 7 ] ] ],
        [ 6 ],
    ]

    result = flatten(matrix)
    result.sort()

    expected = [ 1, 2, 3, 3, 4, 5, 8, 7, 6 ]
    expected.sort()

    assert result == expected

def test_flatten_02():
    matrix = [
        [1, 2, 3, [ 3, 4 ] ],
        [5, [ 8, [ [ [ [ [ [ 7 ], 9 ] ] ] ] ] ] ],
        [ 6 ],
    ]

    result = flatten(matrix)
    result.sort()

    expected = [ 1, 2, 3, 3, 4, 5, 8, 7, 9, 6 ]
    expected.sort()

    assert result == expected

def test_flatten_with_reference_01():
    matrix = [
        [1, 3, [ 3 ] ],
        [ 6 ],
    ]

    result = flatten_with_reference(matrix)

    expected = [
        { 'value': 1, 'index': [ 0, 0 ] },
        { 'value': 3, 'index': [ 0, 1 ] },
        { 'value': 3, 'index': [ 0, 2, 0 ] },
        { 'value': 6, 'index': [ 1, 0 ] },
    ]

    assert result == expected

def test_flatten_with_reference_02():
    matrix = [
        [1, 3, [ 3 ] ],
        [ 6, [ [ [ [ [ [ [ 7 ] ], 8 ] ] ] ] ] ],
    ]

    result = flatten_with_reference(matrix)

    expected = [
        { 'value': 1, 'index': [ 0, 0 ] },
        { 'value': 3, 'index': [ 0, 1 ] },
        { 'value': 3, 'index': [ 0, 2, 0 ] },
        { 'value': 6, 'index': [ 1, 0 ] },
        { 'value': 7, 'index': [ 1, 1, 0, 0, 0, 0, 0, 0, 0 ] },
        { 'value': 8, 'index': [ 1, 1, 0, 0, 0, 0, 1 ] },
    ]

    assert result == expected

def test_get_from_matrix_01():
    reference_list = [
        { 'value': 1, 'index': [ 0, 0 ] },
        { 'value': 3, 'index': [ 0, 1 ] },
        { 'value': 3, 'index': [ 0, 2, 0 ] },
        { 'value': 6, 'index': [ 1, 0 ] },
    ]

    matrix = [
        [1, 3, [ 3 ] ],
        [ 6 ],
    ]

    assert get_from_matrix(reference_list, matrix, 3) is 6

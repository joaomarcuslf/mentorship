import pytest

from lesson03.advanced_topics import search_unsorted, search_sorted


def test_search_unsorted_01():
    assert search_unsorted(
        [ 2, 1, 3, 9, 4, 5, 8, 7, 6 ],
        9
    ) is 3

def test_search_unsorted_02():
    assert search_unsorted(
        [ 2, 1, 3, 9, 4, 5, 8, 7, 6 ],
        10
    ) is -1

def test_search_sorted_01():
    assert search_sorted(
        [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ],
        9
    ) is 8

def test_search_sorted_02():
    assert search_sorted(
        [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ],
        10
    ) is -1

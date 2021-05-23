import pytest

from lesson03.deck import Deck

def test_queue_should_add_items_in_the_desired_direction():
    q1 = Deck()

    q1.add(1, 1)
    q1.add(2, -1)
    q1.add(3, -1)
    q1.add(4, 1)

    assert q1.first() is 3
    assert q1.last() is 4
    assert q1.get(1) is 2
    assert q1.elements() == [3, 2, 1, 4]


def test_queue_should_remove_items_in_the_desired_direction_1():
    q1 = Deck()

    q1.add(1, 1)
    q1.add(2, -1)
    q1.add(3, -1)
    q1.add(4, 1)

    q1.remove(1)

    assert q1.first() is 3
    assert q1.last() is 1
    assert q1.get(1) is 2
    assert q1.elements() == [3, 2, 1]

def test_queue_should_remove_items_in_the_desired_direction_2():
    q1 = Deck()

    q1.add(1, 1)
    q1.add(2, -1)
    q1.add(3, -1)
    q1.add(4, 1)

    q1.remove(-1)

    assert q1.first() is 2
    assert q1.last() is 4
    assert q1.get(1) is 1
    assert q1.elements() == [2, 1, 4]

def test_queue_should_remove_items_in_the_desired_direction_3():
    q1 = Deck()

    q1.add(1, 1)
    q1.add(2, -1)
    q1.add(3, -1)
    q1.add(4, 1)

    q1.remove(-1)
    q1.remove(-1)
    q1.remove(1)

    assert q1.first() is 1
    assert q1.last() is 1
    assert q1.get(1) is -1
    assert q1.elements() == [1]

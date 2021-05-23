import pytest

from lesson03.sorted_list import SortedList

def test_queue_should_add_sorting():
    q1 = SortedList()

    q1.add(3)
    q1.add(1)
    q1.add(1)
    q1.add(6)
    q1.add(4)
    q1.add(2)
    q1.add(5)
    q1.add(12)

    assert q1.first() is 1
    assert q1.last() is 12
    assert q1.get(1) is 1
    assert q1.get(2) is 2
    assert q1.elements() == [1,1,2,3,4,5,6,12]


def test_queue_should_remove_items_by_value_1():
    q1 = SortedList()

    q1.add(3)
    q1.add(1)
    q1.add(1)
    q1.add(6)
    q1.add(4)
    q1.add(2)
    q1.add(5)
    q1.add(12)

    q1.remove(12)

    assert q1.first() is 1
    assert q1.last() is 6
    assert q1.get(1) is 1
    assert q1.get(2) is 2
    assert q1.elements() == [1,1,2,3,4,5,6]

def test_queue_should_remove_items_by_value_2():
    q1 = SortedList()

    q1.add(3)
    q1.add(1)
    q1.add(1)
    q1.add(6)
    q1.add(4)
    q1.add(2)
    q1.add(5)
    q1.add(12)

    q1.remove(6)

    assert q1.first() is 1
    assert q1.last() is 12
    assert q1.get(1) is 1
    assert q1.get(2) is 2
    assert q1.elements() == [1,1,2,3,4,5,12]

def test_queue_should_remove_items_by_value_3():
    q1 = SortedList()

    q1.add(3)
    q1.add(1)
    q1.add(1)
    q1.add(6)
    q1.add(4)
    q1.add(2)
    q1.add(5)
    q1.add(12)

    q1.remove(1)

    assert q1.first() is 1
    assert q1.last() is 12
    assert q1.get(1) is 2
    assert q1.get(2) is 3
    assert q1.elements() == [1,2,3,4,5,6,12]



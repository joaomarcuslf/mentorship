import pytest

from lesson03.stack import Stack

def test_Stack_should_add_items_in_the_end():
    q1 = Stack()

    q1.add(1)
    q1.add(2)
    q1.add(3)
    q1.add(4)

    assert q1.first() is 1
    assert q1.last() is 4
    assert q1.get(1) is 2


def test_Stack_should_remove_items_in_the_end():
    q1 = Stack()

    q1.add(1)
    q1.add(2)
    q1.add(3)
    q1.add(4)

    q1.remove()

    assert q1.first() is 1
    assert q1.last() is not 4
    assert q1.last() is 3
    assert q1.get(1) is 2


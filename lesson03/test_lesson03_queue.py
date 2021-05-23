import pytest

from lesson03.queue import Queue

def test_queue_should_add_items_in_the_end():
    q1 = Queue()

    q1.add(1)
    q1.add(2)
    q1.add(3)
    q1.add(4)

    assert q1.first() is 1
    assert q1.last() is 4
    assert q1.get(1) is 2


def test_queue_should_remove_items_in_the_beginning():
    q1 = Queue()

    q1.add(1)
    q1.add(2)
    q1.add(3)
    q1.add(4)

    q1.remove()

    assert q1.first() is not 1
    assert q1.last() is 4
    assert q1.first() is 2
    assert q1.get(1) is 3


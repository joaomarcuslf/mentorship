import pytest

from lesson01.get_pick import get_pick

users = [
            {"name": "João", "id": 10},
            {"name": "Letícia", "id": 11},
            {"name": "Gualberto", "id": 12},
            {"name": "Thailani", "id": 13},
            {"name": "Mourinha", "id": 14},
            {"name": "Bárbara", "id": 15},
            {"name": "Marcela", "id": 16},
            {"name": "Rômulo", "id": 17},
        ]

queue = ["Letícia", "Gualberto", "Thailani", "João",
            "Marcela", "Mourinha", "Bárbara", "Rômulo"]

def test_get_pick_1():
    user = get_pick(users, 5, queue)

    assert user == {"name": "Mourinha", "id": 14}

def test_get_pick_2():
    user = get_pick(users, 0, queue)

    assert user == {"name": "Letícia", "id": 11}

def test_get_pick_3():
    user = get_pick(users, -1, queue)

    assert user == -1

def test_get_pick_4():
    user = get_pick(users, len(queue), queue)

    assert user == -1

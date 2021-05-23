import pytest

from lesson02.searches import get_user_index_by_name, get_room_index_by_name, get_room_and_user_indexes_name

list01 = ["Letícia", "Gualberto", "Thailani", "João",
            "Marcela", "Mourinha", "Bárbara", "Rômulo"]

matrix01 = [
    ["Letícia", "Gualberto"],
    ["Thailani", "João"],
    ["Marcela", "Mourinha", "Bárbara"],
    ["Rômulo"]
]


def test_get_user_index_by_name_1():
    assert get_user_index_by_name(
        list01,
        "Gualberto"
    ) is 1


def test_get_user_index_by_name_2():
    assert get_user_index_by_name(
        list01,
        "Limão"
    ) is -1


def test_get_room_index_by_name_1():
    assert get_room_index_by_name(
        matrix01,
        "Mourinha"
    ) is 2


def test_get_room_index_by_name_2():
    assert get_room_index_by_name(
        matrix01,
        "Thailani"
    ) is 1

def test_get_room_index_by_name_3():
    assert get_room_index_by_name(
        matrix01,
        "Jão"
    ) is -1

def test_get_room_and_user_indexes_name_1():
    assert get_room_and_user_indexes_name(
        matrix01,
        "Rômulo"
    ) == [3, 0]


def test_get_room_and_user_indexes_name_2():
    assert get_room_and_user_indexes_name(
        matrix01,
        "Bárbara"
    ) == [2, 2]

def test_get_room_and_user_indexes_name_3():
    assert get_room_and_user_indexes_name(
        matrix01,
        "Marcela"
    ) == [2, 0]

def test_get_room_and_user_indexes_name_4():
    assert get_room_and_user_indexes_name(
        matrix01,
        "Marcele"
    ) == [-1,-1]

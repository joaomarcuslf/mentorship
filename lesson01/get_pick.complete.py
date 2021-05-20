def get_pick(users_data: list, pick_index: int, pick_queue: list) -> map:
    if pick_index  > len(pick_queue) -1 or pick_index < 0:
        return -1

    user_name = pick_queue[pick_index]

    for user in users_data:
        if user["name"] == user_name:
            return user

    return -1

if __name__ == '__main__':
    user = get_pick(
        [
            {"name": "João", "id": 10},
            {"name": "Letícia", "id": 11},
            {"name": "Gualberto", "id": 12},
            {"name": "Thailani", "id": 13},
            {"name": "Mourinha", "id": 14},
            {"name": "Bárbara", "id": 15},
            {"name": "Marcela", "id": 16},
            {"name": "Rômulo", "id": 17},
        ],
        5,
        ["Letícia", "Gualberto", "Thailani", "João",
            "Marcela", "Mourinha", "Bárbara", "Rômulo"]
    )

    print(user == {"name": "Mourinha", "id": 14})

def get_user_index_by_name(data: list, name: str) -> int:
    for index in range(len(data)):
        if data[index] is name:
            return index
    return -1

def get_room_index_by_name(data: list, name: str) -> int:
    for room_index in range(len(data)):
        for user_index in range(len(data[room_index])):
            if data[room_index][user_index] is name:
                return room_index
    return -1

def get_room_and_user_indexes_name(data: list, name: str) -> list:
    for room_index in range(len(data)):
        for user_index in range(len(data[room_index])):
            if data[room_index][user_index] is name:
                return [room_index, user_index]
    return [-1, -1]



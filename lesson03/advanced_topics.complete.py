def search_unsorted(list: list, item: any) -> int:
    for index in range(len(list)):
        if list[index] == item:
            return index
    return -1

def search_sorted(list: list, item: any) -> int:
    for index in range(len(list)):
        if list[index] == item:
            return index
        elif list[index] > item:
            return -1
    return -1

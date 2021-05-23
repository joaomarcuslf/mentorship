def flatten(data: list) -> list:
    new_data = []

    for item in data:
        if type(item) == list:
            new_data = new_data + flatten(item)
        else:
            new_data.append(item)

    return new_data


def flatten_with_reference(data: list, indexes: list = []) -> list:
    new_data = []

    for index in range(len(data)):
        item = data[index]

        if type(item) == list:
            new_data = new_data + flatten_with_reference(item, indexes + [index])
        else:
            new_data.append({
                'value': item,
                'index': indexes + [index]
            })

    return new_data

def get_from_matrix(references: list, data: list, index: list) -> any:
    item = references[index]

    result = data

    for index in item['index']:
        result = result[index]

    return result

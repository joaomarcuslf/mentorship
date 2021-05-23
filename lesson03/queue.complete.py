class Queue(object):
    def __init__(self):
        self._data = []

    def first(self):
        return self.get(0)

    def last(self):
        return self.get(len(self._data) -1)

    def elements(self) -> list:
        return self._data

    def get(self, index: int) -> any:
        if index < len(self._data) and index < 0:
            return -1

        return self._data[index]

    def add(self, item: any) -> any:
        self._data = self._data + [item]

    def remove(self) -> any:
        new_list = []

        for index in range(len(self._data)):
            if index > 0:
                new_list = new_list + [self._data[index]]

        self._data = new_list



class Deck(object):
    def __init__(self):
        self._data = []

    def first(self):
        return self.get(0)

    def last(self):
        return self.get(len(self._data) -1)

    def elements(self) -> list:
        return self._data

    def get(self, index: int) -> any:
        if index < len(self._data) and index > -1:
            return self._data[index]

        return -1

    def add(self, item: any, direction: int) -> any:
        if direction == 1:
            self._data = self._data + [item]
        elif direction == -1:
            self._data = [item] + self._data
        else:
            return -1

    def remove(self, direction: int) -> any:
        if direction == 1:
            self._data = self._data[0:len(self._data) - 1]
        elif direction == -1:
            self._data = self._data[1:len(self._data)]
        else:
            return -1


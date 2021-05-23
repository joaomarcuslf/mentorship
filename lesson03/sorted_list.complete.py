class SortedList(object):
    def __init__(self):
        self._data = []

    def first(self):
        return self.get(0)

    def last(self):
        return self.get(len(self._data) - 1)

    def elements(self) -> list:
        return self._data

    def get(self, index: int) -> any:
        if index < len(self._data) and index < 0:
            return -1

        return self._data[index]

    def add(self, item: any) -> any:
        new_list = []

        if len(self._data) == 0:
            new_list = [item]
        else:
            for index in range(len(self._data)):
                elm = self._data[index]

                if elm < item:
                    if index + 1 == len(self._data):  # last
                        new_list = self._data[0:len(self._data)] + [item]
                    else:
                        pass
                else:
                    if index + 1 == len(self._data):  # last
                        if elm > item:
                            new_list = self._data[0:index] + [item] + \
                                self._data[index:len(self._data)]
                        else:
                            new_list = self._data[0:len(self._data)] + [item]
                    elif elm == item:  # equals
                        new_list = self._data[0:index + 1] + [item] + \
                            self._data[index + 1:len(self._data)]
                        break
                    else:
                        new_list = self._data[0:index] + [item] + \
                            self._data[index:len(self._data)]
                        break

        self._data = new_list

    def remove(self, value: any) -> any:
        new_list = []

        for index in range(len(self._data)):
            elm = self._data[index]

            if elm == value:
                if index + 1 == len(self._data):
                    new_list = self._data[0:index]
                else:
                    new_list = self._data[0:index] + self._data[index + 1:len(self._data)]

        self._data = new_list

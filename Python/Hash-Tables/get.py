def get_item(self, key):
    index = self.__hash(key)
    if self.data_map[index] is not None:
        for i in range(len(self.data_map[index])):
            if self.data_map[index][i][0] == key:
                return self.data_map[index][i][1]
    return None
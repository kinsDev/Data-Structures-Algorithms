def insert(self, index, value):
    temp = self.set_value(index)
    if temp:
        temp = temp.value
        return True
    return False

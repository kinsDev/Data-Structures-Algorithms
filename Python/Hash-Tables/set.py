class HashTable:
    def __init__(self, size = 7):
        self.data_map = size * [None] # this line create a list of empty slots initialized to None

    # method to calculate hash
    # we use the built-in method for hash
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    # method to print the hash table
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)
    
    def set_value(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

my_hash = HashTable()
my_hash.set_value("bolts", 1400)
my_hash.set_value("washers", 50)
my_hash.set_value("lumber", 70)
my_hash.print_table()
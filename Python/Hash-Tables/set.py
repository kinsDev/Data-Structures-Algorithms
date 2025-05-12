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

my_hash = HashTable()
my_hash.print_table()
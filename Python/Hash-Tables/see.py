class HashTable:
    def __init__(self, size=11):
        # this line create a list of empty slots initialized to None
        self.data_map = [None] * size
        print(self.data_map)
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

my_hashtable = HashTable()
my_hashtable.print_table()

# First we will create a constructor for a hash table
class HashTable:
    def __init__(self, size = 11):
        # this line create a list of empty slots initialized to None
        self.data_map = [None] * size

# The we create a hash table function
    def __hash(self, key): # we have used __hash to encapsulate the method only to this class
        # we need to initialize a variable to store the hash map
        # we should go through each letter in a key and calculate the hash map value
        # As we calculate that value we will add the current hash value to the ordinal(gets the ASCII number for each letter as we loop through)
        # we can use any other prime number other than 23
        # The modulo operator returns the remainder after a division
        # we are dividing by the length of the Key passed in
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    # the next thing is to create a hash table 
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

# And then we create an object for the HashTbale class
my_hashtable = HashTable()
my_hashtable.print_table()

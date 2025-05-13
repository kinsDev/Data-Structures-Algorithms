# For efficiency we have used dictionaries, which have led us to using two separate loops, hence O(n), 
# which is more optimized than using nested loops that would cause us to use O(n^2)

def item_in_common(list1, list2):
    # I will first create a dictionary where I will store all values in the first list and initialize them to list1
    my_dict = {}
    for i in list1:
        my_dict[i] = True

    # then create a second loop that will go through all values in j and will check whether the value in list2 is already in the dictionary
    for j in list2:
        if j in my_dict:
            return True
    return False


list1 = [1, 3, 5]
list2 = [2, 4, 5]


print(item_in_common(list1, list2))


"""
    EXPECTED OUTPUT:
    ----------------
    True

"""


"""
HT: Item In Common ( ** Interview Question)
Write a function item_in_common(list1, list2) that takes two lists as 
input and returns True if there is at least one common item between the two lists, False otherwise.

Use a dictionary to solve the problem that creates an O(n) time complexity.
"""
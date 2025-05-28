"""
# Easier
def find_duplicates(nums):
    duplicates = []
    my_dict = {}

    for i in nums:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1

    for key in my_dict:
        if my_dict[key] > 1:
            duplicates.append(key)
    return duplicates
"""

# More concise Python Approach using get.(i, 0) + 1


def find_duplicates(nums):
    my_dict = {}
    for i in nums:
        # we want to store in my dictionary a key, and it's count(curent default is 0)
        my_dict[i] = my_dict.get(i, 0) + 1

    duplicates = []  # this is where we will be storing the duplicates in a list
    for i, count in my_dict.items():
        if count > 1:
            duplicates.append(i)
    return duplicates


print(find_duplicates([1, 2, 3, 4, 5]))
print(find_duplicates([1, 1, 2, 2, 3]))
print(find_duplicates([1, 1, 1, 1, 1]))
print(find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]))
print(find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]))
print(find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]))
print(find_duplicates([]))


"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""

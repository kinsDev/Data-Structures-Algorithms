# We are given two lists, and the interviewer wants you to chack the two lists
# and return true whether a certain value appears twice in the two lists

# The common naive answer would be to loop on the first list
# then loop the second list checking whether there is a value in the second loop
# that was found in the first loop
# This would be bad because we would have nested loops that would actually be O(n^2)

def item_in_common(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

list1 = [1, 3, 5]
list2 = [2, 4, 5]

print(item_in_common(list1, list2))

# This however would be the most optimal answer
# Key secret is to not use nested loop, that way we can have two loops O(2n), ignoring the 2
# we remain with O(n)
# We create a dictionary, store values in first list there, and then loop through second list as we compare

def optimized_comparison(listed1, listed2):
    my_dict = {}
    for i in listed1:
        my_dict[i] = True # we are storing all values in the first list in the dictionary and assigning them True value
    for j in listed2:
        # if j in the second list is already stored in dict we return True, else False
        if j in my_dict:
            return True
    return False

listed1 = [1, 2, 3, 4, 6]
listed2 = [7, 8, 9, 10]

print(optimized_comparison(listed1, listed2))
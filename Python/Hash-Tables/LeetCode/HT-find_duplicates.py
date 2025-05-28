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
        my_dict[i] = my_dict.get(i, 0) + 1 # we want to store in my dictionary a key, and it's count(curent default is 0)
    
    duplicates = [] # this is where we will be storing the duplicates in a list
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


"""
HT: Find Duplicates ( ** Interview Question)
find_duplicates()

Problem: Given an array of integers nums, find all the duplicates in the array using a hash table (dictionary).

Input:
A list of integers nums.

Output:
A list of integers representing the numbers in the input array nums that appear more than once. If no duplicates are found in the input array, return an empty list [].

Input: nums = [4, 3, 2, 7, 8, 2, 3, 1]
Output: [2, 3]
Explanation: The numbers 2 and 3 appear more than once in the input array.
 
Input: nums = [1, 2, 3, 4, 5]
Output: []
Explanation: There are no duplicates in the input array, so the function returns an empty list [].
 
Input: nums = [3, 3, 3, 3, 3]
Output: [3]
Explanation: The number 3 appears more than once in the input array.
 
Input: nums = [-1, 0, 1, 0, -1, -1, 2, 2]
Output: [-1, 0, 2]
Explanation: The numbers -1, 0, and 2 appear more than once in the input array.
 
Input: nums = []
Output: []
Explanation: There are no numbers in the input array, so the function returns an empty list [].
"""
def two_sum(nums, target):
    # we create a dictionary to store our key-value pairs. Key is the number we've seen so far
    # value will be the index of that number in the list
    num_dict = {}
    
    # we use enumerate because it automatically picks the index of values as we iterate through them
    # i is the index, we store it at value; num is key
    for i, num in enumerate(nums): # we have picked the index of the first num, and its key
        # we want to find a complimentary number that we can use to get a target value
        compliment = target - num
        # now we want to check whether we have the compliment on our dictionary already, whether we have seen it
        if compliment in num_dict:
            return [num_dict[compliment], i]
        # if lets say the compliment wasn't in the dictionary, we store the current number and its index to the dictionary and assign is a value i
        num_dict[num] = i
    return [] # if no two values add up to the target
    
print(two_sum([5, 1, 7, 2, 9, 3], 10))  
print(two_sum([4, 2, 11, 7, 6, 3], 9))  
print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))  
print(two_sum([1, 3, 5, 7, 9], 10))  
print ( two_sum([1, 2, 3, 4, 5], 10) )
print ( two_sum([1, 2, 3, 4, 5], 7) )
print ( two_sum([1, 2, 3, 4, 5], 3) )
print ( two_sum([], 0) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 4]
    [1, 3]
    [0, 3]
    [1, 3]
    []
    [2, 3]
    [0, 1]
    []

"""


"""
HT: Two Sum ( ** Interview Question)
two_sum()

Problem:
Given an array of integers nums and a target integer target, find the indices of two numbers in the array that add up to the target.

The main challenge here is to implement this function in one pass through the array. This means you should not iterate over the array more than once. Therefore, your solution should have a time complexity of O(n), where n is the number of elements in nums.



Input:

A list of integers nums .

A target integer target.



Output:

A list of two integers representing the indices of the two numbers in the input array nums that add up to the target. If no two numbers in the input array add up to the target, return an empty list [].
"""
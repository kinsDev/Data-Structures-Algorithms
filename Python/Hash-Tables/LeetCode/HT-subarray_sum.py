def subarray_sum(nums, target):
    # we are loking for the indices of the continuous keys that when added give us the target
    # and then we print the beginning index and the ending index

    # we need to keep track of the sum of numbers as I loop through the list
    prefix_sum = 0

    # I need a dictionary to store previous prefix sums and the index they occured.
    # means that a sum of 0 exists just before the array starts - to handle edge cases like [1, 2, 3], target = 6 - sum from index 0 to 2
    sum_indices = {0: -1}
    for i, num in enumerate(nums):
        prefix_sum += num  # this is us keeping track of the sum of numbers as we loop through
        complement = prefix_sum - target

        if complement in sum_indices:
            return [sum_indices[complement] + 1, i]
        sum_indices[prefix_sum] = i
    return []


nums = [1, 2, 3, 4, 5]
target = 9
print(subarray_sum(nums, target))

nums = [-1, 2, 3, -4, 5]
target = 0
print(subarray_sum(nums, target))

nums = [2, 3, 4, 5, 6]
target = 3
print(subarray_sum(nums, target))

nums = []
target = 0
print(subarray_sum(nums, target))


"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""

"""
HT: Subarray Sum ( ** Interview Question)
Given an array of integers nums and a target integer target, write a Python function called subarray_sum that finds the indices of a contiguous subarray in nums that add up to the target sum using a hash table (dictionary).

Your function should take two arguments:

nums: a list of integers representing the input array

target: an integer representing the target sum


Your function should return a list of two integers representing the starting and ending indices of the subarray that adds up to the target sum. If there is no such subarray, your function should return an empty list.

For example:



nums = [1, 2, 3, 4, 5]
target = 9
print(subarray_sum(nums, target))  # should print [1, 3]


Note that there may be multiple subarrays that add up to the target sum, but your function only needs to return the indices of any one such subarray. Also, the input list may contain both positive and negative integers.
"""
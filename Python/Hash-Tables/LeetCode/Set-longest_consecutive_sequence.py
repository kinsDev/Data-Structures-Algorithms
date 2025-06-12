def longest_consecutive_sequence(arr):
    # we store all the array integers in a set
    myset = set(arr)
    # this is our current maximum_consecutive_sequence length
    maximum_consecutive_sequence = 0

    # we loop through the set looking at each number individually and checking it's sequence length
    for num in myset:
        if num - 1 not in myset:  # a number is the beginning of a new sequnce if when subtracted by 1, its result is not already in the set
            current_length = 1   # if not in the set, the current length of that sequence is 1
            # and the current number in our sequence is the number where we are in the loop
            current_number = num

            # we need to check whether the next number for our current sequence is in the array so that we can continue counting our sequence length
            while (current_number + 1) in myset:
                current_length += 1  # we add the current length if it is
                current_number += 1  # and we update our current number in the sequence for continuation as we check whether the current_number+1 is in the sequence so that we can continue in counting our sequence length
            # the while loop continues until it breaks
            # after it breaks we check whether the current length is longer than the current maximum than we have
            # if it is, we just replace out current maximum, if mot, no update is done

            if current_length > maximum_consecutive_sequence:
                maximum_consecutive_sequence = current_length
    return maximum_consecutive_sequence


print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))


"""
    EXPECTED OUTPUT:
    ----------------
    4

"""


"""
Set: Longest Consecutive Sequence ( ** Interview Question)
Given an unsorted array of integers, write a function that finds the length of the  longest_consecutive_sequence (i.e., sequence of integers in which each element is one greater than the previous element).

Use sets to optimize the runtime of your solution.

Input: An unsorted array of integers, nums.

Output: An integer representing the length of the longest consecutive sequence in nums.

Example:



Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive sequence in the input array is [4, 3, 2, 1], and its length is 4.

"""
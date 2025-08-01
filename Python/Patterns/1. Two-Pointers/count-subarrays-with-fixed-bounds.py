def countSubarrays(nums, minK, maxK):
    # we need pointers for the mink and maxk values
    # we also need to be able to set the position of mink and maxk and invalid index
    # we need to initialize count to 0
    # those can be set at -1 because we haven't seen them yet!
    # we also need to be able to iterate through the array nums, we can do that by creating a for loop
    # the loop will go through the entire range of the length of nums
    # as we loop, we can look for an element that is invalid
    # everytime we see an invalid element, we know that the sequence of elements forming a subarray has been ruined
    # that means that we have to reset the position of mink and maxk again
    # then look for a mink and maxk element
    # and then we can do the count
    # we can't count anything if the mink and maxk are at -1 because there is not consecutive subarray

    count = 0
    min_pos = max_pos = left_bound = -1
    n = len(nums)

    for i in range(n):
        if nums[i] < minK or nums[i] > maxK:
            left_bound = i
            min_pos = max_pos = -1

        if nums[i] == minK:
            min_pos = i

        if nums[i] == maxK:
            max_pos = i

        if min_pos != -1 and max_pos != -1:
            count += max(0, min(min_pos, max_pos) - left_bound)

    return count


"""
A brute-force approach of checking every subarray to see if it contains minK and maxK would be too slow, so instead, we take a more efficient, single-pass strategy. Moving through the array from left to right, we keep track of just enough information to determine the count of all the valid fixed-bound subarrays.

A subarray is only valid (fixed-bound) if it includes both minK and maxK, and contains no invalid numbers (i.e., numbers outside the range [minK, maxK]. So, to identify valid subarrays ending at a certain position in the list, we focus on three important markers:

The one where we last saw minK.

The one where we last saw maxK

The one where we last saw a number outside the range [minK, maxK].

While iterating over nums, we check whether we have seen both minK and maxK at each step. If we have, we look at the earlier of those two positions. This tells us the furthest back we can go while including both required values. But we also need to ensure the subarray doesn't include invalid numbers, so we compare this earliest position with the last invalid index.

Suppose the last invalid number appeared before the minK and maxK positions earlier. In that case, all subarrays that start after that invalid position and end at the current index will be valid. The number of such valid subarrays is simply the possible starting points between the index after the last invalid element and the earlier of the two bound positions (inclusive). Each start point gives one valid subarray ending at the current index. We accumulate that count as we go.


Let's look at the algorithm steps:

Initialize the variables:

min_pos, max_pos, and left_bound to -1 to indicate invalid positions initially.

count to 0 to keep track of the total number of valid subarrays.

Iterate through each element in the array nums using an index i:

If nums[i] is outside the range [minK, maxK], set left_bound to i and reset min_pos and max_pos to -1. This invalidates any subarray ending at or beyond this position.

If nums[i] equals minK, update min_pos to the current index i.

If nums[i] equals maxK, update max_pos to the current index i.

For each position i, if both min_pos and max_pos are valid (not -1), calculate the number of valid subarrays ending at i:

The earliest valid starting point for such a subarray is min(min_pos, max_pos) + 1.

Subtract left_bound from this value to get the number of valid subarrays.

Accumulate this count into count.

Return count after finishing the iteration.
"""
def count_pairs(nums, target):
    count = 0
    nums.sort()  # sorting in place. If I wanted to assign a variable: nums = sorted(nums)
    low, high = 0, len(nums) - 1

    while low < high:
        if nums[low] + nums[high] < target:
            count += high - low
            low += 1
        else:
            high -= 1

    return count


"""
The problem requires counting the number of valid pairs in an array where the sum of the pair is less than a given target. To solve this efficiently, we first sort the array to simplify pair comparisons. After sorting, we initialize two pointers: one at the beginning of the array and the other at the end. Sorting ensures that any element at a higher index is greater than or equal to the element at a lower index, allowing us to evaluate pairs in a structured manner. The two pointer approach leverages this property to efficiently identify valid pairs.

When the sum of the elements at the two positions is smaller than the given target, all pairs formed by fixing the lower position and combining it with values starting from the higher position down to the lower position are valid. This is because the sequence is sorted, and any pair created by moving the higher position downward results in a smaller sum, which is guaranteed to be less than the current sum of the two positions. The total number of such valid pairs is the difference between the higher and lower positions.

After counting these pairs, the lower position is incremented to check combinations involving larger values, allowing us to explore pairs with higher sums. If the sum of the elements at the two positions is not smaller than the given target, the higher position is moved backward to reduce the sum and potentially find valid pairs. This approach ensures efficient counting of all valid pairs without redundant checks.

The steps of the algorithm are as follows:

Sort the input array, nums, in an ascending order.

Initialize a variable count to 
0
0
 to keep track of the total number of valid pairs. Also, initialize two pointers, low and high, with low at the beginning of the array and high at the end.

Use the pointers to traverse the array until low < high, and check the sum of nums[low] + nums[high]:

If the sum is less than the target, all low and high (inclusive of high) pairs are valid because the array is sorted. Add high - low to count. Increment low to explore additional valid pairs with a larger first element.

Otherwise, decrement high to reduce the sum.

Once the pointers meet or cross, the iteration ends.

Return the value of count as the total number of valid pairs.
"""
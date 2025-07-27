def three_sum(nums):
    nums.sort()  # sort the input array in ascending order
    results = []
    n = len(nums)  # the length of the nput arrays that we will be iterating over

    for i in range(n - 2):  # this makes sure that we don't go out of bounds by ensuring that we still have two more numbers left after the current number to make a valid triplet
        if nums[i] > 0:  # we are breaking because, if the first value is more than 0, and the rest are greater values, then there's no way we can find the sum of zero!
            break
        # we need to ensure that the current number is the first element and is not a duplicate of the previous element
        if i == 0 or nums[i] != nums[i - 1]:
            low = i + 1  # the second value after our current number[i]
            high = n - 1  # this is the last value index

        while low < high:  # this makes sure that low and high don't overlap while going inwards
            # we are summing at the current number index, low pointer adn high pointer index
            sum = nums[i] + nums[low] + nums[high]

            if sum < 0:
                low += 1
            elif sum > 0:
                high -= 1
            else:
                results.append([nums[i], nums[low], nums[high]])

                low += 1  # we continue to move forward
                high -= 1  # we move backwards

                # we need to make sure that we are not dealing with duplicates so that we avoid adding the same triplets that we just got more than once to the results
                while low < high and nums[low] == nums[low - 1]:
                    low += 1
                while low < high and nums[high] == nums[high + 1]:
                    high -= 1

    return results

"""
The essence of the solution lies in first sorting the array, which makes it easier to find positive numbers that balance out negative ones to sum to zero, and also helps in skipping duplicates. Then, for each number in the array, we search for two other numbers to the right that, together with it, sum to zero. This is done using two pointers—low and high—starting just after the fixed number and at the end of the array, respectively. We calculate the sum of each triplet as nums[i] + nums[low] + nums[high]. If the total is less than zero, we move the low pointer forward to increase the sum; if it’s greater than zero, we move the high pointer backward to decrease the sum. When the sum is exactly zero, we add the triplet to the result and move both pointers inward, skipping duplicates to ensure all triplets are unique.

Using the intuition above, we implement the algorithm as follows:

Sort the input array nums in ascending order to make it easier to find triplets and skip duplicates.

Create an empty array, result, to store the unique triplets.

Store the length of nums in a variable n.

Iterate over the array from index i = 0 to n - 2 (as we are looking for triplets).

Break the loop if the current number nums[i] is greater than 0. As the array is sorted, all remaining numbers will be positive, and any triplet including nums[i] will have a sum greater than zero.

If i == 0 or nums[i] is not equal to nums[i - 1], this ensures that the current number is either the first element or not a duplicate of the previous element.

Initialize two pointers: low = i + 1 and high = n - 1.

Run a loop as long as low is less than high.

Calculate the sum: nums[i] + nums[low] + nums[high].

If the sum is less than 0, move the low pointer forward to increase the sum.

If the sum is greater than 0, move the high pointer backward to decrease the sum.

Otherwise, add [nums[i], nums[low], nums[high]] to the result, as this triplet sums to 0.

Move low and high to the next distinct values to avoid duplicate triplets. This is done by incrementing low while nums[low] == nums[low - 1], and decrementing high while nums[high] == nums[high + 1].

After iterating through the whole array, return the result that contains all unique triplets that sum to zero.
"""
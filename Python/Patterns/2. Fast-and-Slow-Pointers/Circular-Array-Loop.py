def circular_array_loop(nums):
    # Start iterating through the array, considering each element a potential starting position.
    n = len(nums)

    for i in range(n):
        slow = fast = i  # we start by making sure that bot fast and slow point to the same starting position
        # we move each pointer forward or backward according to the number at it's current step
        forward = nums[i] > 0
        # the reason why we do that is because, we move forward when a number is positive and backward otherwise

        while True:  # while the following below conditions are true, do the following
            # we move the next step for slow
            slow = next_step(slow, nums[slow], n)
            # and then we check whether slow's current iteration is a vaid cycle
            if is_not_cycle(nums, forward, slow):
                break

            fast = next_step(fast, nums[fast], n)
            if is_not_cycle(nums, forward, fast):
                break

            fast = next_step(fast, nums[fast], n)
            if is_not_cycle(nums, forward, fast):
                break

            if slow == fast:
                return True
    return False

# there is something that I need to remember, moving based on the value at a certain index


def next_step(pointer, value, n):
    return (pointer + value) % n

# avoiding self-loops, or at least starting from another iteration if there is one
# if the direction is not consistent, we know that, that is not a valid loop, and it is okay for me to start looking for a valid loop from another iteration
# so, I need to perform validation checks to make sure that current iteration is a valid cycle or not


def is_not_cycle(nums, previous_direction, pointer):
    current_direction = nums[pointer] >= 0

    # we are first checking whether the previous direction boolean value is equal to the current direction boolean value - this is one way of checking whether a loop cycle is valid
    # if the direction has a mismatch based on different boolean values, then that's a false
    # another way to check whether a cycle is valid is making sure that we don't have a self loop e.g [3, 1, 2] - in this case, 3 would move three times forward and come back to itself, if it has, not valid
    if (previous_direction != current_direction) or nums[pointer] % len(nums) == 0:
        return True  # this is not a cycle
    else:
        return False  # this is a cycle


"""
We can use the fast and slow pointers technique, where traversing at different speeds enables efficient cycle detection. Comparing the signs of values during traversal facilitates correct navigation in both forward and backward directions within the array.

For each element of the array, two pointers, initialized at that specific element, traverse the array, with one taking one step at a time and the other advancing by two steps. The position of each pointer for the next step is determined by the value it is currently pointing to. If any movement results in the pointer pointing to a value with a different sign (indicating a change in direction) or pointing to the same index it was previously pointing to (indicating a self-loop), move to the next element of the array. Do the same if the fast pointer has reached the end of the array and no cycle is detected. However, if there’s a cycle, both pointers eventually catch up. This is because, in the non-cyclic part, the distance between them increases by one index in each iteration. However, upon entering the cyclic part, the fast pointer rapidly closes the gap on the slow pointer, decreasing the distance by one index in each iteration until they meet.

Let's see the workflow of the algorithm. The algorithm involves iterating through each index of nums. For every index, i, perform the following steps:

Initialize fast and slow pointers to the current index i.

Move the slow pointer, either forward or backward, depending on the current value it is pointing to, nums[i]. For example, if the value is −3, the slow pointer is moved three indexes backward. Similarly, if the value is 2, the slow pointer is moved two indexes forward.

Now, check if a valid cycle can be formed. For this, we have two primary checks:If any of the conditions above fail, move to step 4.

If the index of the new value pointed to by slow is the same as the index of the previous value pointed to by slow, that is, the pointer is forming a self-loop, then the next iteration starts.

Observe the sign of the previous value pointed to by slow and the sign of the new value it points to. If both values have different signs, that is, the pointer is not moving in a single direction, then the next iteration starts.

Move the fast pointer twice in a similar fashion, and after every move, check for the validity of the cycle using the same checks as above. If a valid cycle can’t be formed, move to the next index of nums.

Now, check for the existence of the cycle. If the slow and fast pointers meet at the same index, a cycle is detected. Return TRUE in this case. Otherwise, continue moving the pointers until we determine whether or not a cycle exists.
"""
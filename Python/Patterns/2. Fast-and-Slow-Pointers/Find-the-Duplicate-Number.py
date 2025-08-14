def find_duplicate(nums):
    # traverse in nums array using fast and slow pointers
    # the first element where fast and slow are pointing to
    slow = fast = nums[0]

    # move the pointers until they meet, slow once and fast once
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    # if they meet, we need to put slow back to the beginning and they have to move at the same pace again
    # after detecting slow == fast, the slow pointer should be reset outside the loop, then both pointers move at the same pace until they meet again, which identifies the duplicate.
    slow = nums[0]

    # a loop should be used here too!
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return fast

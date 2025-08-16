# The first input of the test case is an array of values representing a linked list.
# The second input is the index where the tail connects to form a cycle (or −1 if there's no cycle).
# This index is used only to construct the linked list and is not passed to the function.

# Definition for a Linked List node
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from ds_v1.LinkedList.LinkedList import ListNode


def count_cycle_length(head):
    slow, fast = head, head  # set slow and fast pointers to the beginning of the LL

    # we traverse until we reach the end. If we reach the end, no cycle exists in the LL!
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        # if the fast and slow pointers meet as we traverse, we begin the cycle length count, and we initialize it to 1 to include the first meeting point
        if fast == slow:
            cycle_length = 1
            slow = slow.next  # now we continue to move the slow pointer forward as we count the the length of the cycle

            # as we move slow pointer, we will leave fast pointer at the meeting point, and count until we get back to fast, and that will be the length of the cycle
            while slow != fast:
                cycle_length += 1
                slow = slow.next
            return cycle_length
    return 0  # this return statement basically says, I checked and there was no cycle!

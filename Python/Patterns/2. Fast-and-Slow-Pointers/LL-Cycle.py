# The first input of the test case is an array of values representing a linked list.
# The second input is the index where the tail connects to form a cycle (or −1 if there's no cycle).
# This index is used only to construct the linked list and is not passed to the function.

# Definition for a Linked List node
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from ds_v1.LinkedList.LinkedList import ListNode


def detect_cycle(head):
    slow_pointer, fast_pointer = head, head

    while fast_pointer != None and fast_pointer.next != None:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

        if fast_pointer != None and fast_pointer == slow_pointer:
            return True
    return False

"""
The following steps can be performed to implement the algorithm above:

We initialize two pointers, fast and slow, which point to the head of the linked list.

We traverse the linked list using these two pointers. They move in the following way:

The slow pointer moves only one node forward in each iteration.

The fast pointer moves two nodes forward in each iteration, which means that it skips a node.

If the fast pointer becomes NULL, we have reached the end of the linked list. Since no cycle exists, return FALSE.

If both slow and fast pointers become equal to each other, return TRUE, since a cycle exists in the linked list.
"""
# Definition for a Linked List node
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from ds_v1.LinkedList.LinkedList import ListNode


def get_middle_node(head):
    slow_pointer, fast_pointer = head, head

    while fast_pointer != None and fast_pointer.next != None:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

        if fast_pointer == None or fast_pointer.next == None:
            return slow_pointer
    return head  # this is the case where we only have one element!


"""
Let's go over the workflow of the algorithm:

Initialize two pointers, slow and fast, at the head of the linked list, slow = head and fast = head.

Traverse the linked list by moving the slow pointer one step forward, slow = slow.next, and the fast pointer two steps forward, fast = fast.next.next.

When the fast pointer reaches the last element of the linked list, or becomes equal to NULL, the slow pointer, at that time, will point to the middle node. Return the node that the slow pointer points to.
"""
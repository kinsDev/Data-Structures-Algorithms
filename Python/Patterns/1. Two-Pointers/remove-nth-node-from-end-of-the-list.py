# Definition for a Linked List node
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from ds_v1.LinkedList.LinkedList import ListNode


def remove_nth_last_node(head, n):
    left = head
    right = head

    for _ in range(n):
        right = right.next

    if right == None:
        return head.next

    while right.next is not None:
        left = left.next
        right = right.next

    left.next = left.next.next
    return head


"""
Solution
So far, you have probably brainstormed some approaches and have an idea of how to solve this problem. Let’s explore some of these approaches and figure out which one to follow based on considerations such as time complexity and any implementation constraints.

Optimized approach using two pointers
We can use the two pointer technique to remove the target node in a single traversal. To start with, place both pointers at the head of the list. Next, we move one of the pointers ahead by n steps. Once the first pointer is at the nth node, we move both pointers together until the first one reaches the end. At that point, the second pointer will be right before the node we need to remove. Remove the target node and return the head of the modified list.

Why does this work? When the first pointer is moved n steps ahead, a gap of n nodes is created between the two pointers. As they move together, that gap is maintained. So, when the first pointer reaches the end of the list, the second is n steps behind, i.e., just before the node we want to remove.

Let’s go over the steps of the algorithm:

Initialize left and right pointers pointing to the linked list’s head.

Move the right pointer n steps forward.

If the right pointer has reached the end of the list, i.e., NULL, it means the head is the target node for removal. In this case, return head.next as the new head of the linked list. This effectively removes the original head of the list.

Otherwise, move left and right pointers forward one step at a time.

Once the right pointer reaches the end of the linked list, update left.next to left.next.next. This is to skip the target node, effectively removing it from the linked list.

Finally, return the head, pointing to the updated linked list with the nth node removed.
"""
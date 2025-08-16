# Definition for a Linked List node
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from ds_v1.LinkedList.LinkedList import ListNode


def split_circular_linked_list(head):
    slow, fast = head, head

    while fast.next != head and fast.next.next != head:  # we are iterating untll fast points to head
        slow = slow.next
        fast = fast.next.next

    # the moment fast points to head, we want to divide the LL into two
    # slow is currently at the middle
    head1 = head  # first, we clarify that the head of the first half points to the original head
    # we set head2(head of the second half to the node after middle node)
    head2 = slow.next
    slow.next = head1  # and then we set the middle node to point to head1, forming a cycle for the first half of the LL

    # now we need to form a second cycle, and remember, fast is pointing to the original head
    # pointing fast to the beginning of the second half and then iterating on the second half step by step until fast points to head2
    # once fast points to head2, we update fast.next = head2; to form the second half of LL cycle, just the same way we updated slow.next to head1
    fast = head2

    while fast.next != head:
        fast = fast.next
    fast.next = head2

    # returning the two heads as an array as per the requirements
    return [head1, head2]

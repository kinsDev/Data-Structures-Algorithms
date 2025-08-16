# The first input of the test case is an array of values representing a linked list.
# The second input is the index where the tail connects to form a cycle (or −1 if there's no cycle).
# This index is used only to construct the linked list and is not passed to the function.

# Definition for a Linked List node
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from ds_v1.LinkedList.LinkedList import ListNode


def remove_cycle(head):
    # edge case, what if there is no list?
    if head == None:
        return None

    # we initialize the two pointers at head
    slow, fast = head, head

    # we traverse the whole LL
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        # if fast meets slow, before fast reaches None, it means that there is a cycle, so we need to remove that cycle
        if slow == fast:
            break  # we break so that we can be able to stop moving fast and slow pointers after they meet, this is because the while loop is still active

    # if fast reaches None, return the LL as it is
    if fast == None or fast.next == None:
        return head

    # Now we need to find the entry point of the cycle - since we are sure that a cycle exists
    # we do that by reseting slow to the beginning(head), leaving fast pointer to the meeting point, and moving one step at a time for both
    # until slow pointer and fast pointer meet again, now, this time they will meet at the cycle's entry point
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    # once they meet at the entry point, we want fast to traverse  all the way to slow, because, it's a cycle, but, when we reach fast == slow
    # we set fast.next to None to break the cycle
    while fast.next != slow:
        fast = fast.next
    # once it becomes points to slow, we want to say at that point that fast is pointing to slow, we want it to point to None
    fast.next = None  # fast ne

    return head  # now this is the head of the modified LL, basically returning the new modified LL with no cycle!

# Definition for a Linked List node
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from ds_v1.LinkedList.LinkedList import ListNode


def twin_sum(head):
    # let's find the middle node - remember, we are only dealing with even length LL
    slow, fast = head, head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

    # after finding the middle node, we reverse te second list
    second_half = reverse_list(slow)

    # initialize the maximum twin sum to 0 and the start adding the pointer at the first half with the pointer to the second half
    max_sum = 0
    curr, prev = head, second_half

    # to add we can say, while second half pointer is not equal to None
    while prev:
        if curr.val + prev.val > max_sum:
            max_sum = curr.val + prev.val
        curr = curr.next
        prev = prev.next

    return max_sum

# now we have our reverse helper function


def reverse_list(head):
    before = None
    current = head
    while current:
        after = current.next
        current.next = before
        before = current
        current = after
    return before  # at the end of the loop, current will be pointing to None, and before will be pointing to the new head of the reverse list

"""
The main idea behind finding the maximum twin sum in a linked list is to reverse the second half of the list and sum the corresponding values from both halves. The algorithm first locates the middle node using fast and slow pointers to achieve this. Then, it reverses the second half of the linked list, starting from the middle node. After that, it calculates the twin sums by adding the values of the nodes from the start of the list and the reversed second half while keeping track of the maximum sum found so far. Finally, it returns the maximum sum encountered during the traversal.

Using the above intuition, the solution can be implemented as follows:

The first step is to find the middle node of the linked list:

Initialize two pointers, slow and fast, at the head of the linked list. The slow pointer will move one node at a time, while the fast pointer will move two nodes at a time.

Iterate through the linked list using these pointers as long as the fast pointer and its next node are not NULL. The slow pointer moves one step, and the fast pointer moves two steps. By the time the fast pointer reaches the end, the slow pointer will be in the middle of the list.

The next step is to reverse the second half of the linked list:

Start iterating the linked list from the middle by initializing a pointer, curr, at the node where slow points.

Initialize another pointer prev with NULL.

Continue the loop as long as the curr is not NULL.

Inside the loop, modify the pointers as follows:

First, save curr.next to temp for later use.

Update curr.next to prev.

Update prev to curr.

Update curr to temp.

The final step is to find the twin sum for all twin nodes in the linked list:

First, initialize max_sum with 0 to keep track of the maximum twin sum found so far.

Initialize the curr pointer at the head of the linked list. Due to the reversing algorithm, the prev pointer would already be pointing at the head of the reversed second half.

Iterate through the list until prev reaches NULL.

Find the twin sum inside the loop by adding the data of the curr node and the prev node.

If this sum is greater than max_sum, update max_sum with this sum.

Move both prev and curr pointers forward.

Finally, return max_sum as the maximum twin sum of the given linked list.
"""
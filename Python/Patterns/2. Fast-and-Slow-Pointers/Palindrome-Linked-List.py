# Definition for a Linked List node
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from ds_v1.LinkedList.LinkedList import ListNode
from LinkedListReversal import reverse_linked_list

def palindrome(head):
    # initialize
    slow, fast = head, head
    
    # find middle
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    
    # position to reverse from
    # now that we have reached middle we need to consider odd-length and even-length LL
    if fast !=  None:
        slow = slow.next # this is because, when fast reaches the end and it's not pointing to None, then the LL is odd-length and we should reverse from the second element after middle
    
    # reverse second half and assign a pointer of reversed second half
    second_half = reverse_list(slow) # we are reversing from where slow is pointing
    
    # after that we need to compare the first and second half
    # we cxompare them using pointers
    pointer1, pointer2 = head, second_half
    
    # we need to set a boolean value to True
    result = True
    
    # we need only to check the second half
    while pointer2 is not None:
        # we need to compare the values not the node pointers between the two halves
        if pointer1.val != pointer2.val:
            result = False
            break
        # and then we proceed to the next values to compare between first and second half
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    
    # once the comparison between pointers 1 and 2 is done after we get to the end of second half's pointer, pointer2
    # we reverse the second half again to it's original arrangement
    reverse_list(second_half)
    return result

# helper method for the reverse functions
def reverse_list(head):
    prev = None
    current = head
    while current is not None:
        after = current.next
        current.next = prev
        prev = current
        current = after
    return prev
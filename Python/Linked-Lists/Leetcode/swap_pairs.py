class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True

    def print_list(self):
        values = []
        temp = self.head
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        result = " -> ".join(values) if values else "Empty"
        print(result + " -> None")
        return result

    def make_empty(self):
        self.head = None
        self.length = 0

    def swap_pairs(self):
        if self.length <= 1:
            return

        dummy_node = Node(0)
        dummy_node.next = self.head
        prev = dummy_node

        first = self.head

        while first and first.next != None:
            second = first.next

            # the Swapping
            prev.next = second
            first.next = second.next
            second.next = first

            # move pointers
            prev = first
            first = first.next
        self.head = dummy_node.next


# Test case 1: Swapping pairs in a list with an even number of nodes (1->2->3->4)
print("\nTest case 1: Swapping pairs in a list with an even number of nodes.")
ll1 = LinkedList(1)
ll1.append(2)
ll1.append(3)
ll1.append(4)
print("BEFORE: ", end="")
ll1.print_list()
print("AFTER:  ", end="")
ll1.swap_pairs()
ll1.print_list()
print("-----------------------------------")

# Test case 2: Swapping pairs in a list with an odd number of nodes (1->2->3->4->5)
print("\nTest case 2: Swapping pairs in a list with an odd number of nodes.")
ll2 = LinkedList(1)
ll2.append(2)
ll2.append(3)
ll2.append(4)
ll2.append(5)
print("BEFORE: ", end="")
ll2.print_list()
print("AFTER:  ", end="")
ll2.swap_pairs()
ll2.print_list()
print("-----------------------------------")

# Test case 3: Swapping pairs in a list with a single node (1)
print("\nTest case 3: Swapping pairs in a list with a single node.")
ll3 = LinkedList(1)
print("BEFORE: ", end="")
ll3.print_list()
print("AFTER:  ", end="")
ll3.swap_pairs()
ll3.print_list()
print("-----------------------------------")

# Test case 4: Swapping pairs in an empty list
print("\nTest case 4: Swapping pairs in an empty list.")
ll4 = LinkedList(1)
ll4.make_empty()
print("BEFORE: ", end="")
ll4.print_list()
print("AFTER:  ", end="")
ll4.swap_pairs()
ll4.print_list()
print("-----------------------------------")

# Test case 5: Swapping pairs in a list with two nodes (1->2)
print("\nTest case 5: Swapping pairs in a list with two nodes.")
ll5 = LinkedList(1)
ll5.append(2)
print("BEFORE: ", end="")
ll5.print_list()
print("AFTER:  ", end="")
ll5.swap_pairs()
ll5.print_list()
print("-----------------------------------")


"""
LL: Swap Nodes in Pairs ( ** Interview Question)
Write a method called swap_pairs inside the LinkedList class.

This method should swap every two adjacent nodes in the linked list by adjusting the pointers, not the node values.

You must modify the list in-place and update the head accordingly.

If the list has an odd number of nodes, the final node remains in its original position.

You should use a dummy node to simplify the pointer adjustments.

For example, if the list is 1 -> 2 -> 3 -> 4, the method should transform it to 2 -> 1 -> 4 -> 3.

If the list has an odd number of nodes, the last node remains in place (e.g., 1 -> 2 -> 3 becomes 2 -> 1 -> 3).





Input:

The method operates on the linked list via self.head, which points to the first node or is None for an empty list.

Each node has an integer value and a next pointer to the next node or None.



Output:

No return value (None); the method modifies the linked list in place.

The self.head attribute must be updated to point to the head of the modified list after swapping.





Examples:

Example 1:

Input List: 1 -> 2 -> 3 -> 4

Output List: 2 -> 1 -> 4 -> 3

Explanation: Swap the first pair (1, 2) to get 2 -> 1 -> 3 -> 4, then swap the second pair (3, 4) to get 2 -> 1 -> 4 -> 3.

Example 2:

Input List: 1 -> 2 -> 3

Output List: 2 -> 1 -> 3

Explanation: Swap the first pair (1, 2) to get 2 -> 1 -> 3. The last node (3) has no pair, so it stays in place.

Example 3:

Input List: 1

Output List: 1

Explanation: A single node has no pair to swap, so the list remains unchanged.

Example 4:

Input List: [] (empty list)

Output List: []

Explanation: An empty list has no nodes to swap, so it remains empty.

Example 5:

Input List: 1 -> 2

Output List: 2 -> 1

Explanation: Swap the only pair (1, 2) to get 2 -> 1.



Notes:

Ensure self.head is correctly updated to point to the new first node after all swaps.

Handle edge cases like empty lists, single nodes, and lists with odd or even node counts.

Consider using a dummy node to simplify swapping the head node.
"""
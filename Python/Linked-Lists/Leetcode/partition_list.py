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
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

#   +===================================================+
#   |               WRITE YOUR CODE HERE                |
#   | Description:                                      |
#   | - This method partitions a linked list around a   |
#   |   value `x`.                                      |
#   | - It rearranges the nodes so that all nodes less  |
#   |   than `x` come before all nodes greater or equal |
#   |   to `x`.                                         |
#   |                                                   |
#   | Tips:                                             |
#   | - We use two dummy nodes, `dummy1` and `dummy2`,  |
#   |   to build two separate lists: one for elements   |
#   |   smaller than `x` and one for elements greater   |
#   |   or equal to `x`.                                |
#   | - `prev1` and `prev2` help us keep track of the   |
#   |   last nodes in these lists.                      |
#   | - Finally, we merge these two lists by setting    |
#   |   `prev1.next = dummy2.next`.                     |
#   | - The head of the resulting list becomes          |
#   |   `dummy1.next`.                                  |
#   +===================================================+

    def partition_list(self, x):
        # I was thinking that first of all if the linked list if empty then we should definitely return None
        if self.head is None:
            return None
        # Another thing that I thought was, if the linked list has only 1 element, whatever value of x we are given, we should only return that value in the linked list
        if self.head.next is None:
            return self.head
        # right here I wanted to go through the list picking values less than x and putting them in a chain linked list stored in object list1 and so on for list2
        # I also figured that I could place a pointer to self.head to represent the value that we will be comparing with x.
        temp = self.head
        list1 = LinkedList()
        list2 = LinkedList()
        # I'm not sure whether this will even work, but I was betting on the the fact that the chained values could be stored in separate linked lists in this manner
        # while the self.head from the original Linked List is not None, I want to perform the following if statements
        while temp:
            if x < temp.value:
                list1.append(temp.value)
            else:
                list2.append(temp.value)
            temp = temp.next
        # there's another edge case that I hadn't looked at yet.
        # If list one was actually empty, we would have to return list prev2
        if list1.head is None:
            return list2.head
        # We are going to set the head of list1 to prev1
        # as long as prev.next is not None, we want to move prev1 to the next nodes
        # once we reach to end of list1, we will have prev1 positioned to the last nodes\
        # we will connect the last node of list1 with the first node of list2(list2.head)
        # and form a single linked list called list1
        if list1.head is None:  # if list1 was empty we should simply return list2
            return list2.head

        prev1 = list1.head
        while prev1.next is not None:
            prev1 = prev1.next  # moving to the last node of list1

        if list2.head is None:
            return list1.head  # this way I will be returning all elemnts of list1 if list2 is empty
        prev1.next = list2.head
        # return the head of the new partitioned list
        return list1.head


#  +=====================================================+
#  |                                                     |
#  |          THE TEST CODE BELOW WILL PRINT             |
#  |              OUTPUT TO "USER LOGS"                  |
#  |                                                     |
#  |  Use the output to test and troubleshoot your code  |
#  |                                                     |
#  +=====================================================+


# Function to convert linked list to Python list
def linkedlist_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result

# Function to test partition_list


def test_partition_list():
    test_cases_passed = 0

    print("-----------------------")

    # Test 1: Normal Case
    print("Test 1: Normal Case")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    ll.append(5)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 2, 3, 4, 5]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 2: All Equal Values
    print("Test 2: All Equal Values")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(3)
    ll.append(3)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [3, 3, 3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 3: Single Element
    print("Test 3: Single Element")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(1)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 4: Already Sorted
    print("Test 4: Already Sorted")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 2, 3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 5: Reverse Sorted
    print("Test 5: Reverse Sorted")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(2)
    ll.append(1)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 3, 2]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 6: All Smaller Values
    print("Test 6: All Smaller Values")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(1)
    ll.append(1)
    ll.append(1)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 1, 1]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 7: Single Element, Equal to Partition
    print("Test 7: Single Element, Equal to Partition")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Summary
    print(f"{test_cases_passed} out of 7 tests passed.")


# Run the test function
test_partition_list()



"""
LL: Partition List ( ** Interview Question)
⚠️ CAUTION: Advanced Challenge Ahead!

Now, here is the exercise:
___________________________________

Implement the partition_list member function for the LinkedList class, which partitions the list such that all nodes with values less than x come before nodes with values greater than or equal to x.

Note:  This linked list class does NOT have a tail which will make this method easier to implement.

The original relative order of the nodes should be preserved.



Details:
The function partition_list takes an integer x as a parameter and modifies the current linked list 
in place according to the specified criteria. If the linked list is empty (i.e., head is null), 
the function should return immediately without making any changes.


Example 1:
Input:
Linked List: 3 -> 8 -> 5 -> 10 -> 2 -> 1 x: 5

Process:
Values less than 5: 3, 2, 1
Values greater than or equal to 5: 8, 5, 10

Output:
Linked List: 3 -> 2 -> 1 -> 8 -> 5 -> 10


Example 2:
Input:
Linked List: 1 -> 4 -> 3 -> 2 -> 5 -> 2 x: 3

Process:
Values less than 3: 1, 2, 2
Values greater than or equal to 3: 4, 3, 5

Output:
Linked List: 1 -> 2 -> 2 -> 4 -> 3 -> 5

Tips:
- While traversing the linked list, maintain two separate chains: one for values less than x and one for values greater than or equal to x.
- Use dummy nodes to simplify the handling of the heads of these chains.
- After processing the entire list, connect the two chains to get the desired arrangement.

Note:
The solution must maintain the relative order of nodes. For instance, in the first example, 
even though 8 appears before 5 in the original list, the partitioned list must still have 8 before 5 
as their relative order remains unchanged.

"""
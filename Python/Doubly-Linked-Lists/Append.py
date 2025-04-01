class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)


print('Head:', my_doubly_linked_list.head.value)
print('Tail:', my_doubly_linked_list.tail.value)
print('Length:', my_doubly_linked_list.length, '\n')

print('Doubly Linked List:')
my_doubly_linked_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Head: 1
    Tail: 2
    Length: 2 

    Doubly Linked List:
    1
    2
    
"""

"""
DLL: Append
Extend the previously implemented DoublyLinkedList class by adding an append method that inserts a new node with a given value at the end of the list.

The method should perform the following tasks:

Create a new instance of the Node class with the provided value.

If the list is empty (i.e., the head is None), set the head and tail of the list to the newly created node.

If the list is not empty, perform the following steps:

Set the next attribute of the current tail node to the new node.

Set the prev attribute of the new node to the current tail node.

Update the tail of the list to the new node.

Increment the length attribute of the list by 1.

Return True to indicate that the operation was successful.

"""
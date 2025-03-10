# We are going to focus on writing a method that appends a new node to the end of a Linked List.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    # Constructor for Linked Lists
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    # Method to print the Linked List
    def printer(self):
        printer = self.head
        while printer is not None:
            print(printer.value)
            printer = printer.next
    
    # Method to append a new node to the end of the Linked List
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0: # case when the LL is empty
            return None
        # If there's only one element in the LL
        if self.length == 1:
            popped_node = self.head
            self.head = None
            self.tail = None
        else:
            # Traverse to the second last node
            current_node = self.head
            while current_node.next != self.tail:
                current_node = current_node.next
            
            # update and discpnnect the last node
            popped_node = self.tail
            self.tail = current_node
            self.tail.next = None
        self.length -= 1
        return popped_node.value

my_linked_list = LinkedList(4)
my_linked_list.append(5)
my_linked_list.printer()
print("\n")
my_linked_list.pop()
my_linked_list.printer()
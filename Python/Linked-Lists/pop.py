# Create a constructor for the Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def printer(self):
        printer = self.head
        while printer != None:
            print(printer.value)
            printer = printer.next
    
    def append(self, value):
        new_node = Node(value)
        if self.head is Node:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            popped_node = self.head
            self.head = None
            self.tail = None
        else:
            # we will need to go to the previous node
            current_node = self.head
            while current_node.next != self.tail:
                current_node = current_node.next

            # update and disconnect the last node
            popped_node = self.tail
            self.tail = current_node
            self.tail.next = None
        self.length -= 1
        return popped_node.value



my_linked_list = LinkedList(4)
my_linked_list.append(5)
my_linked_list.printer()
print("Popped value:", my_linked_list.pop())
my_linked_list.printer()
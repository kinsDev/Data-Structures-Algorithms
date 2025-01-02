# Class for creating Nodes
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Class for creating and manipulating linked list using nodes


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # lets print the LinkedList and view it
    def printer(self):
        printer = self.head
        while printer != None:
            print(printer.value)
            printer = printer.next

    # lets append a value to the LinkedList
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

    # lets pop a value to the linkedlist
    def pop(self):
        if self.length == 0:
            return None

        temp = self.head
        pre = self.tail
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
           self.head = new_node
           self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    # We are going to pop the first item from a LL

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail == None
        return temp.value
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.printer()
print("\n")
print("Popped value is", my_linked_list.pop())
my_linked_list.printer()
print("\n")
my_linked_list.prepend(2)
my_linked_list.printer()
print("\n")
my_linked_list.pop_first()
my_linked_list.printer()
print("\n")
print(my_linked_list.get(1))
my_linked_list.printer()

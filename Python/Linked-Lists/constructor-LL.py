# Contructor for Linked Lists

# We are going to create a class that creates nodes
# So whenever we want to create a new node, we can just call this class on our LinkedList class

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

my_linked_list = LinkedList(4)
print(my_linked_list.head.value)
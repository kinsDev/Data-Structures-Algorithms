class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1


my_stack = Stack(2)

print('Stack before push(1):')
my_stack.print_stack()

my_stack.push(1)

print('\nStack after push(1):')
my_stack.print_stack()


"""
    EXPECTED OUTPUT:
    ----------------
    Stack before push(1):
    2

    Stack after push(1):
    1
    2   

"""


"""
Stack:Push
Implement the push method for the Stack class that adds a new node with a given value to the top of the stack.

The method should perform the following tasks:

Create a new instance of the Node class using the provided value.

Set the next attribute of the new node to point to the current top node.

Update the top attribute of the Stack class to point to the new node.

Increment the height attribute of the Stack class by 1.
"""
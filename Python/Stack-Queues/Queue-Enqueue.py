class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1


my_queue = Queue(1)

print('Queue before enqueue(2):')
my_queue.print_queue()

my_queue.enqueue(2)

print('\nQueue after enqueue(2):')
my_queue.print_queue()


"""
    EXPECTED OUTPUT:
    ----------------
    Queue before enqueue(2):
    1

    Queue after enqueue(2):
    1
    2

"""


"""
Queue:Enqueue
Implement the enqueue method for the Queue class that adds a new node with a given value to the end of the queue.

The method should perform the following tasks:

Create a new instance of the Node class using the provided value.

If the queue is empty (i.e., self.first is None), set the first and last attributes of the Queue class to point to the new node.

If the queue is not empty, perform the following steps:

Set the next attribute of the current last node to point to the new node.

Update the last attribute of the Queue class to point to the new node.

Increment the length attribute of the Queue class by 1.
"""
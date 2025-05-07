class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()


def sort_stack(input_stack):
    # Step 1: Create a new stack to hold sorted elements
    sorted_stack = Stack()

    # Step 2: Sort the stack using only stack operations
    while not input_stack.is_empty():
        # Pop the top element from input_stack
        temp = input_stack.pop()

        # Step 3: Compare with sorted_stack's top and move elements back if needed
        while (not sorted_stack.is_empty()) and (sorted_stack.peek() > temp):
            # Move elements from sorted_stack back to input_stack
            input_stack.push(sorted_stack.pop())

        # Step 4: Push temp to its correct position in sorted_stack
        sorted_stack.push(temp)

    # Step 5: Move elements back to input_stack so it's in ascending order
    while not sorted_stack.is_empty():
        input_stack.push(sorted_stack.pop())


my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()


"""
    EXPECTED OUTPUT:
    ----------------
    Stack before sort_stack():
    2
    4
    5
    1
    3

    Stack after sort_stack:
    1
    2
    3
    4
    5

"""


"""
This was the high-level information:
Pseudo Code:
1. Create a new temporary stack for sorting, called 'sorted_stack'.
2. While the input stack is not empty:
   a. Pop the top element from the input stack, store it in 'temp'.
   b. While the 'sorted_stack' is not empty and its top element is greater than 'temp':
       i. Pop the top element from 'sorted_stack' and push it back onto the input stack.
   c. Push 'temp' onto the 'sorted_stack'.
3. Transfer elements back from 'sorted_stack' to the input stack:
   a. While 'sorted_stack' is not empty:
       i. Pop the top element from 'sorted_stack' and push it onto the input stack.
"""

"""
Stack: Sort Stack ( ** Interview Question)
The sort_stack function takes a single argument, a Stack object.  The function should sort the elements in the stack in ascending order (the lowest value will be at the top of the stack)
using only one additional stack. 
The function should use the pop, push, peek, and is_empty methods of the Stack object.
Note: This is a new function, not a method within the Stack class. So, your indent should be all the way to the LEFT.


The function should perform the following tasks:
Create a new instance of the Stack class called sorted_stack.
While the input stack is not empty, perform the following:
Pop the top element from the input stack and store it in a variable temp.
While the sorted_stack is not empty and its top element is greater than temp, pop the top element from sorted_stack and push it back onto the input stack.
Push the temp variable onto the sorted_stack.
Once the input stack is empty, transfer the elements back from sorted_stack to the input stack. 
To do this, while sorted_stack is not empty, pop the top element from sorted_stack and push it onto the input stack.

You can also click on "Hints" (above) to see the pseudo-code.
Overall, the function should have a time complexity of O(n^2), where n is the number of elements in the original stack, due to the nested loops used to compare the elements.  
However, the function should only use one additional stack, which could be useful in situations where memory is limited.
"""
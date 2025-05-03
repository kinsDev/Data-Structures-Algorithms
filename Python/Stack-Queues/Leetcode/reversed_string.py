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


# we include parameter input_string to stand for the string that we weill be keying in
def reverse_string(input_string):
    stack = Stack()  # we initialize a stack where we will place the characters from our input string one by one

    for char in input_string:
        stack.push(char)

    # we then need to start popping the characters and placing in reversed order
    # in that case we need to initialize a variable to store the reverse_string
    reversed_string = ""

    # we need to make sure that before we start one character at a time from our input string that it is not a empty string stored in our stack
    while not stack.is_empty():
        # now we need to add the popped characters into the reversed_string variable
        reversed_string += stack.pop()
    return reversed_string  # And then we return the reversed string


my_string = 'hello'

print(reverse_string(my_string))


"""
    EXPECTED OUTPUT:
    ----------------
    olleh

"""


"""
Stack: Reverse String ( ** Interview Question)
The reverse_string function takes a single parameter string, which is the string you want to reverse.

Return a new string with the letters in reverse order.
"""
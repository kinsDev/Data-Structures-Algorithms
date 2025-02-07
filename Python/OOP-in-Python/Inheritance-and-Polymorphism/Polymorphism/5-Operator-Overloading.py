# Operator Overloading

# Whenever an operator is used in Python, its corresponding method is invoked to perform its 
# predefined function. For example, when the + operator is called, it invokes the special function,
#  __add__, in Python, but this operator acts differently for different data types.

print(5 + 3)
print("Money" + "Maker")


# Overloading operators for a user-defined class
# We are going to implement a class that represents a complex number.“ A complex number consists of a real part and an imaginary part.
# When we add a complex number, the real part is added to the real part, and the imaginary part is added to the imaginary part.
# Similarly, when we subtract a complex number, the real part is subtracted from the real part, and the imaginary part is subtracted from the imaginary part.

class Com:
    def __init__(self, real = 0, imag = 0):
        self.real = real
        self.imag = imag
    
    def __add__(self, other): # overloading the + operator
        temp = Com(self.real + other.real, self.imag + other.imag)
        return temp
    
    def __sub__(self, other): # overloading the - operator
        temp = Com(self.real - other.real, self.imag - other.imag)
        return temp

obj1 = Com(3, 7)
obj2 = Com(2, 5)

obj3 = obj1 + obj2
obj4 = obj1 - obj2

print("real of obj3:", obj3.real)
print("imag of obj3:", obj3.imag)
print("real of obj4:", obj4.real)
print("imag of obj4:", obj4.imag)


#    '+'	        __add__(self, other)            add
#    '-'	        __sub__(self, other)            subtract
#    '/'	        __truediv__(self, other)        divide
#    '*'	        __mul__(self, other)            multiplication
#    '<'	        __lt__(self, other)             less than
#    '>'	        __gt__(self, other)             greater than
#    '=='         __eq__(self, other)               equal to

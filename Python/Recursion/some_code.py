functions = []

for i in range(3):
    def func():
        return i
    functions.append(func)

for f in functions:
    print(f())

# explain what is actually happening here?
"""
- Each func is capturing the variable i, not its current value.
- So all functions in functions refer to the same i, which ends up being 2 after the loop completes.
- When you later call each function, they all return 2.

This is called late binding, where the value of variables used in closures is looked up when the function is called, not when it is defined.
"""

print("\n")
# and how you would fix it to get the expected output!
functions = []
for i in range(3):
    def func(i = i):
        return i
    functions.append(func)

for f in functions:
    print(f())
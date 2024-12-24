def print_items(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)

print_items(10)

# This code run n + n times, so the Big-O notation is O(n + n) = O(2n) = O(n)
# We simplified the Big-O notation to O(n) because the constant 2 is not important
# It doesn't matter if the code runs 2n times or 100n times, the Big-O notation is O(n) because the constant is not important

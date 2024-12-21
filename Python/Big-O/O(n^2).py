# Nested O(n^2) loop
# This code runs n times inside another n times, so the Big-O notation is O(n * n) = O(n^2)
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
print_items(10)

# O(n^2) is not efficient at a time complexity point of view because on the graph it is actually steeper
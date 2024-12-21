# Different Terms for Inputs interview question
# we will illustrate this by having two for loops, each with a different Big O
# So it will be something like:
# O(a) * O(b) = O(a * b)
#          or
# O(a) + O(b) = O(a + b)

# The example below is for: O(a + b)
def different_terms(a, b):
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)
different_terms(4, 6)

# We will have another example for: O(a * b):
def diff_terms(n, m):
    for i in range(n):
        for j in range(m):
            print(i, j)
diff_terms(4, 6)
def has_unique_chars(my_string):
    # we have an input string to our function
    # we need to check whether a specific character has been stored in a set
    # if we have a certain character in the set already we return False
    # we contiue by adding the next character into the set, we make the check, if already present return early False, otherwise
    # ...continue adding characters
    # eventually after we are done, we just return True
    my_set = set([])
    for char in my_string:
        if char in my_set:
            return False
        my_set.add(char)
    return True


print(has_unique_chars('abcdefg'))  # should return True
print(has_unique_chars('hello'))  # should return False
print(has_unique_chars(''))  # should return True
print(has_unique_chars('0123456789'))  # should return True
print(has_unique_chars('abacadaeaf'))  # should return False


"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    True
    True
    False

"""


"""
Set: Has Unique Chars ( ** Interview Question)
Write a function called has_unique_chars that takes a string as input and returns True if all the characters in the string are unique, and False otherwise.

For example, has_unique_chars('abcdefg') should return True, while has_unique_chars('hello') should return False.
"""
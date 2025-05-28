def first_non_repeating_char(string):
    # Loop through the string and store the count of each character in a dictionary.
    char_dict = {}
    for char in string:
        char_dict[char] = char_dict.get(char, 0) + 1

    # Then, loop through the string again, and for each character, check if its count is 1 in the dictionary
    # The first character with a count of 1 is the first non-repeating character.
    # If none is found, return None.
    for char in string:
        if char_dict[char] == 1:
            return char
    return None
    pass


print(first_non_repeating_char('leetcode'))

print(first_non_repeating_char('hello'))

print(first_non_repeating_char('aabbcc'))


"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""


"""
HT: First Non-Repeating Character ( ** Interview Question)
You have been given a string of lowercase letters.

Write a function called first_non_repeating_char(string) that finds the first non-repeating character in the given string using a hash table (dictionary). If there is no non-repeating character in the string, the function should return None.

For example, if the input string is "leetcode", the function should return "l" because "l" is the first character that appears only once in the string. Similarly, if the input string is "hello", the function should return "h" because "h" is the first non-repeating character in the string.
"""
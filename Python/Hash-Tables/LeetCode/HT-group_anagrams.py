def group_anagrams(strings):
    # dictionary to store values of anagrams
    anagram_groups = {}

    for string in strings:
        # Create a Key by sorting the characters in the string
        # All anagrams will have the same sorted keys
        sorted_key = ''.join(sorted(string))

        # we create a new list if a certain key doesn't exist
        if sorted_key not in anagram_groups:
            anagram_groups[sorted_key] = []

        # we add the original string to the appropriate group
        anagram_groups[sorted_key].append(string)

    # convert dictionary values to a list of lists
    return list(anagram_groups.values())

print("1st set:")
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

print("\n2nd set:")
print(group_anagrams(["abc", "cba", "bac", "foo", "bar"]))

print("\n3rd set:")
print(group_anagrams(
    ["listen", "silent", "triangle", "integral", "garden", "ranged"]))


"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""


"""
HT: Group Anagrams ( ** Interview Question)
You have been given an array of strings, where each string may contain only lowercase English letters. You need to write a function group_anagrams(strings) that groups the anagrams in the array together using a hash table (dictionary). The function should return a list of lists, where each inner list contains a group of anagrams.

For example, if the input array is ["eat", "tea", "tan", "ate", "nat", "bat"], the function should return [["eat","tea","ate"],["tan","nat"],["bat"]] because the first three strings are anagrams of each other, the next two strings are anagrams of each other, and the last string has no anagrams in the input array.

You need to implement the group_anagrams(strings) function and return a list of lists, where each inner list contains a group of anagrams according to the above requirements
"""

"""
def demonstrate_join_sorted():
    print("Breking down ''.join(sorted(string))")

    example_string = "eat"
    print(f"original string: '{example_string}'")
    print()

    # Step 1: what happens when we call sorted on a string
    print("Step 1: sorted(string)")
    sorted_chars = sorted(example_string)
    print(f"sorted('{example_string}') = {sorted_chars}")
    print(f"Type: {type(sorted_chars)}")
    print("Note: sorted() returns a LIST of characters, not a string!")
    print()

    # Step 2: What join() does
    print("Step 2: ''.join(list_of_chars)")
    result = ''.join(sorted_chars)
    print(f"''.join({sorted_chars}) = '{result}'")
    print(f"Type: {type(result)}")
    print()

    # Step 3: All 3 together
    print("Step 3: All in one line")
    one_line_result = ''.join(sorted(example_string))
    print(f"''.join(sorted('{example_string}')) = '{one_line_result}'")
    print()

demonstrate_join_sorted()


def compare_different_examples():
    print("=== Examples with different strings ===\n")

    examples = ["eat", "tea", "ate", "listen", "silent", "abc", "cba"]

    for string in examples:
        sorted_result = ''.join(sorted(string))
        print(f"'{string}' → sorted: {sorted(string)} → joined: '{sorted_result}'")

    print()
    print("Notice how anagrams produce the same result:")
    print("'eat', 'tea', 'ate' all become 'aet'")
    print("'listen', 'silent' both become 'eilnst'")
    print("'abc', 'cba' both become 'abc'")


compare_different_examples()
"""
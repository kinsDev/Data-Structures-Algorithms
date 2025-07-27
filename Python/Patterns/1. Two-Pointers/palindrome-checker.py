def is_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:

        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


def main():

    test_cases = [
        ("A man, a plan, a canal: Panama"),
        ("race a car"),
        ("1A@2!3 23!2@a1"),
        ("No 'x' in Nixon"),
        ("12321"),
    ]

    for i in test_cases:
        print("\tstring: ", i)
        result = is_palindrome(i)
        print("\n\tResult:", result)
        print("-"*100)


if __name__ == "__main__":
    main()


"""
Initialize two pointers: one at the beginning (left) and one at the end (right) of the string.

Move both pointers toward the center, skipping any characters that are not alphanumeric.

At each step, compare the characters at the left and right positions after converting them to lowercase.

If a mismatch is found, return False, indicating that the string is not a palindrome.

If the entire string is traversed without mismatches, return True, indicating that the string is a valid palindrome.
"""
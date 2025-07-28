def reverse_words(sentence):
    # we need to remove any extra spaces from the string — this includes leading, trailing, and multiple spaces between words.
    sentence = sentence.strip()
    # and then, to be able to access this sentence as a list, we can split it according to spaces
    results = sentence.split()

    left, right = 0, len(results) - 1
    while left <= right:
        results[left], results[right] = results[right], results[left]
        left += 1
        right -= 1

    # joins the reversed list of words, with spaces between the words!
    return " ".join(results)

"""
To reverse the words in a sentence, we first remove any extra spaces at the beginning and end to ensure we only deal with the words. Then, we extract all the words in a separate list. This step is helpful because strings are immutable, meaning we can’t change them directly. By working with a list, which is mutable, we can easily process the words.

Next, we use two pointers to work from both ends of the list of words. One pointer starts from the beginning, and the other starts from the end. We swap the words at these two positions, then move the first pointer forward and the second pointer backward, continuing this process until all the words are reversed. Extracting words in a list helped us easily swap elements without creating new strings each time.

Finally, we combine the words with a single space between each, resulting in the sentence with its words in the correct reversed order. The method ensures that there is no unnecessary space before the first word or after the last word, and only one space separates each word. Return the reversed sentence.

Here’s how we can implement the approach above:

Remove any extra spaces from the beginning and end of the sentence.

Split the sentence into words based on spaces, and store it in the list result. This automatically removes multiple spaces between words.

Initialize two pointers:

The left pointer starts from the first word in result, index 0.

The right pointer starts from the last word in result.

Next, we iterate over result until the left pointer becomes greater than or equal to the right pointer. In each iteration:

Swap the words at positions left and right.

Increment the left pointer by 1 to move it one step forward.

Decrement the right pointer by 1 to move it one step backward.

Join the words in result into a sentence with a single space between each word. Return the final reversed sentence.
"""
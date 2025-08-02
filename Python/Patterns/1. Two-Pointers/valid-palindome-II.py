def is_palindrome(string):
  left, right = 0, len(string) - 1

  while left < right:
    if string[left] != string[right]:
      # we try skipping the left character and check
      i, j = left + 1, right
      skipping_left_character = True
      while i < j:
        if string[i] != string[j]:
          skipping_left_character = False
          break
        i += 1
        j -= 1

      # we try skipping the right character and check remaining ones
      i, j = left, right - 1
      skipping_right_character = True
      while i < j:
        if string[i] != string[j]:
          skipping_right_character = False
          break
        i += 1
        j -= 1

      # we are checking which one returns True here
      return skipping_left_character or skipping_right_character

    # what happens if left and right are equal?
    left += 1
    right -= 1

  return True

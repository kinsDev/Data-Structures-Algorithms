def is_strobogrammatic(num):

  rotated_map = {
      "0": "0",
      "1": "1",
      "6": "9",
      "8": "8",
      "9": "6"
  }
  start, end = 0, len(num) - 1

  # I am thinking of creating a loop that iterates through the string; num
  # check whether start pointer and end pointer are present in rotated_map dictionary, if not, we return False
  # the second thing is to check whether, when start pointer is rotated, it is equal to the current end pointer, if not, return False - rotated_map[num[start]] != num[end]
  # If they are equal we move the start pointer forward and the end pointer inwards

  while start <= end:
      if num[start] not in rotated_map or num[end] not in rotated_map:
          return False

      # we want to check whether the start pointer when rotated to 180 degrees, matches the current end digit that we have
      if rotated_map[num[start]] != num[end]:
          return False
      start += 1
      end -= 1
  return True

"""
The solution uses a two pointer approach to determine whether a given string num is a strobogrammatic number by checking its digits from both ends toward the center. It uses a set of valid digit mappings that remain unchanged when rotated 
180
180
 degrees or transform into each other when flipped (such as 
′
0
′
′
 0 
′
 
 to 
′
0
′
′
 0 
′
 
, 
′
1
′
′
 1 
′
 
 to 
′
1
′
′
 1 
′
 
, 
′
8
′
′
 8 
′
 
 to 
′
8
′
′
 8 
′
 
, 
′
6
′
′
 6 
′
 
 to 
′
9
′
′
 9 
′
 
, and 
′
9
′
′
 9 
′
 
 to 
′
6
′
′
 6 
′
 
). The key idea is to verify that each digit on the left side of the string correctly matches its mirrored counterpart on the right side. This means checking if the digit at the start aligns correctly with the corresponding digit at the end when viewed upside down. If all such pairs match according to the defined mappings, the number is considered strobogrammatic.

Now, let’s walk through the steps of the solution:

We initialize a map, dict, to store the valid mappings of digits that either remain the same or transform correctly when rotated 180 degrees:

'0' maps to '0'

'1' maps to '1'

'8' maps to '8'

'6' maps to '9'

'9' maps to '6'

We set two pointers:

left starts at the beginning of the string.

right starts at the end of the string.

We iterate from both ends of the string using left and right pointers toward the middle. In each iteration, we compare the pair of digits pointed by left and right pointers. For each pair, we do the following:

We check whether num[left] exists in dict. If not, we return FALSE because it is not a valid strobogrammatic digit. Otherwise, we retrieve the expected rotated value of num[left] from dict. If this expected value does not match num[right] pointer, we return FALSE because it means the number is not strobogrammatic.

We increment the left pointer by 
1
1
 and decrement the right pointer by 
1
1
, moving toward the center of the string.

We keep iterating until the left pointer crosses the right pointer.

After iterating, if all pairs are valid according to the strobogrammatic rules, we return TRUE, indicating that the number is strobogrammatic.
"""
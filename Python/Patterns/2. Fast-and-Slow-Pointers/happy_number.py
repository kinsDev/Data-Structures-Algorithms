def is_happy_number(n):
    # we need a method to calculate the sum of digits
    def sum_of_digits(number):
        total = 0
        while number > 0:
            digit = number % 10
            total += digit * digit
            number = number//10
        return total

    # now that we have a sum of squared digits method, we set slow_pointer to n and fast_pointer to sum of square of n
    slow_pointer = n
    fast_pointer = sum_of_digits(n)

    while fast_pointer != 1 and slow_pointer != fast_pointer:
        # this is how the logic works here:
        # take the current number at slow_pointer, add the squares of it's digit to find the next number that slow_pointer will point to
        slow_pointer = sum_of_digits(slow_pointer)  # move one step
        fast_pointer = sum_of_digits(
            sum_of_digits(fast_pointer))  # move two steps

    if fast_pointer == 1:
        return True
    return False

"""
To determine whether a number is a happy number, it is iteratively replaced by the sum of the squares of its digits, forming a sequence of numbers. 
This sequence either converges to 1
 (if the number is happy) or forms a cycle (if the number is not happy). We use the fast and slow pointers technique to detect such cycles efficiently. 
 This technique involves advancing two pointers through the sequence at different speeds: one moving one step at a time and the other two at a time.

The pointer moving slower is initialized to the given number, and the faster one starts at the sum of the squared digits of the given number. 
Then, in each subsequent iteration, the slow pointer updates to the sum of squared digits of itself, while the fast pointer advances two steps ahead: 
first by updating to the sum of squared digits of itself and then to the sum of squared digits of this recently calculated sum. If the number is happy, 
the fast pointer will eventually reach 1. However, if the number is not happy, indicating the presence of a cycle in the sequence, both pointers will eventually meet. 
This is because, in the noncyclic part of the sequence, the distance between the pointers increases by one number in each iteration. Once both pointers enter the cyclic part, 
the faster pointer starts closing the gap on the slower pointer, 
decreasing the distance by one number in each iteration until they meet. This way, we can efficiently determine whether a number is a happy number or not.
"""

"""
We will start off our solution by constructing a helper function to calculate the squared sum of digits of the input number.
We know that we need to isolate the digits in our number to calculate the squared sum. This can be achieved by repeatedly removing the last digit of the number and adding 
its squared value to the total sum.

The helper function will find the last digit of the given number by taking its modulus with 10. We’ll store this in a variable digit. Now, since we’ve already separated the last digit, 
we can get the remaining digits by dividing the number by 10. Lastly, we’ll store the squared sum of digit in a variable named total_sum. We’ll repeat this until our number becomes 0.
"""
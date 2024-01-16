'''
Write an algorithm to determine if a number n is a happy number.
We use the following process to check if a given number is a happy number:

Starting with the given number n ,replace the number with the sum of the squares of its digits.
Repeat the process until:
    - The number equals 1, which will depict that the given number n is a happy number.
    - It enters a cycle, which will depict that the given number n is not a happy number.
Return TRUE if n is a happy number, and FALSE if not.
Plan
Example 1
n = 10
  => sum(1^2 + 0^2)  => 1
  n is a happy number since sum of digits == 1

n = 2
 => sum(2 ^ 2) => 4^2 => 16 => 37 => 58 => 89 => 145 => 42 => 20 => 4

Steps
1. Initialize slow pointer to be the input number and fast pointer to be the sum of the squared digits.
2. If fast is not 1 and also not equal to slow.
    3. increment slow by one iteration and fast by two iterations
5. if fast results to 1
    6. return True(happy number)
7. return false happy number not found

'''
def is_happy_number(n):
    # calculate the sum of squared digits
    def sum_of_squared_numbers(n):
        total_sum = 0
        while n > 0:
            n, remainder = divmod(n , 10)
            total_sum += remainder ** 2
        return total_sum

    slow = n
    fast = sum_of_squared_numbers(n)

    while fast != 1 and slow != fast:
        slow = sum_of_squared_numbers(n)
        fast = sum_of_squared_numbers(sum_of_squared_numbers(fast))
    if fast == 1:
        return True
    return False

#test_cases
test_1 = 23
print(is_happy_number(test_1))

test_2 = 4
print(is_happy_number(4))


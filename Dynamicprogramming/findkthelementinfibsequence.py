"""
Write a function which returns the Kth element of the Fibonacci sequence.
The Fibonacci sequence is defined as a sequence in which each number is the
sum of the preceding two numbers in the sequence.
For the purpose of this question, the first two terms of the sequence
are both 1, i.e. fib(0) = fib(1) = 1.

Examples:
Input: k = 2
Output: 2
Explanation:
fib(2) = fib(0) + fib(1) = 1 + 1 = 2
 1 , 1 , 2,4

 0 1 2 3 4 5
 1,1,2
"""


def fib(k: int) -> int:
    if k <= 1:
        return 1
    answer = [1, 1]
    for i in range(2, k + 1):
        num = answer[i - 1] + answer[i - 2]
        answer.append(num)
    return answer[-1]



# Test Cases
print(fib(0))  # 1
print(fib(5))  # 8
print(fib(11))  # 144
